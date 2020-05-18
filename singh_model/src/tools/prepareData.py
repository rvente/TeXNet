import os
import math
import numpy as np
from IPython.display import display, Image as ipImage
import PIL
from PIL import Image
from scipy import ndimage
from sklearn.linear_model import LogisticRegression
from six.moves import cPickle as pickle
from mpl_toolkits.axes_grid1 import ImageGrid
import pandas as pd
import matplotlib.pyplot as plt

predictions_dir = '/home/vente_ralph_d/TeXNet.ai/singh_model/predictions'
predictions_image_dir = predictions_dir + '/formula_images'
HYPER_batch_size = 1
training_raw_data_dir = '../../data/training_56'
training_restore_logdir = '../tb_metrics/2020-05-07 15-53-51 UTC NOPOOL/test_run'

predictions_dir = os.path.expanduser(predictions_dir)
predictions_image_dir = os.path.expanduser(predictions_image_dir)
preds_raw_data_dir = os.path.join(predictions_dir, 'inferencing_%d'%HYPER_batch_size)
preds_logdir = os.path.expanduser(os.path.join(predictions_dir, 'logdir'))
src_dir = os.getcwd()
print('Predictions dir = %s'%predictions_dir)
print('Predicted images are at %s'%predictions_image_dir)
data_props = pd.read_pickle(os.path.join(training_raw_data_dir, 'data_props.pkl'))
data_props['padded_image_dim']
data_props['word2id']['x']

data_dict = {'image':[], 'height':[], 'width':[], 'word2id_len':[], u'bin_len':[], u'word2id':[], u'padded_seq':[], u'padded_seq_len':[], u'seq_len':[], u'squashed_len':[], u'squashed_seq':[]}
df_train_squashed = pd.DataFrame(data_dict)[['image', 'height', 'width', 'word2id_len', u'bin_len', u'word2id', u'padded_seq', u'padded_seq_len', u'seq_len', u'squashed_len', u'squashed_seq']]
df_valid_squashed = pd.DataFrame(data_dict)[['image', 'height', 'width', 'word2id_len', u'bin_len', u'word2id', u'padded_seq', u'padded_seq_len', u'seq_len', u'squashed_len', u'squashed_seq']]

data_props = pd.read_pickle(os.path.join(training_raw_data_dir, 'data_props.pkl'))
max_im_size = data_props['padded_image_dim']

# Set max target sequence length. This is just needed to retrofit the inferencing into the
# training data-frames
l = 300
# Set target sequence to anything. It will be used to generate edit-distance and BLEU score
# in the training cycle, but in the case of inferencing cycle, those values don't mean anything.
# Again, it is needed because the data-frame is supposed to have it for training and validation.
Y = [pd.read_pickle(os.path.join(training_raw_data_dir, 'data_props.pkl'))['word2id']['x']]*l
padded_seq = Y + [0]
padded_len = l + 1
for f in (os.path.basename(p) for p in os.listdir(predictions_image_dir) if os.path.splitext(p)[1] == ".png"):
    im = Image.open(os.path.join(predictions_image_dir,f))
    w = im.size[0]
    h = im.size[1]
    print(max_im_size['width'], max_im_size['height'])
    if (w <= max_im_size['width'] and h <= max_im_size['height']):
        data_dict['image'].append(f)
        data_dict['height'].append(h)
        data_dict['width'].append(w)
        data_dict['word2id_len'].append(l)
        data_dict['bin_len'].append(padded_len)
        data_dict['word2id'].append(Y)
        data_dict['padded_seq'].append(padded_seq)
        data_dict['padded_seq_len'].append(padded_len)
        data_dict['seq_len'].append(padded_len)
        data_dict['squashed_len'].append(padded_len)
        data_dict['squashed_seq'].append(padded_seq)
    else:
        print('Discarding image {im} of size {h}x{w}'.format(im=f, h=h, w=w))
df_test_squashed = pd.DataFrame(data_dict)[['image', 'height', 'width', 'word2id_len', u'bin_len', u'word2id', u'padded_seq', u'padded_seq_len', u'seq_len', u'squashed_len', u'squashed_seq']]
print(df_test_squashed.shape)
display(df_test_squashed)
if df_test_squashed.shape[0] % HYPER_batch_size > 0:
    shortfall = HYPER_batch_size - (df_test_squashed.shape[0]%HYPER_batch_size)
    print('Duplicating image ' + df_test_squashed.iloc[-1].image + ' ' + str(shortfall) + ' times')
    df_test_squashed = pd.concat([df_test_squashed] + [df_test_squashed.iloc[-1:]]*shortfall)
assert (df_test_squashed.shape[0]%HYPER_batch_size) == 0

def displayRandImage(df, root):
    filename = df.image.sample(1).values[0]
    path = os.path.join(root, filename);
    image_data = Image.open(path)
    print('{name} {shape} dpi={dpi}'.format(name=filename, shape=image_data.size,
                                            dpi=image_data.info["dpi"] if 'info' in image_data.info else 'None'))
    #     print(path, ' ', image_data.size, image_data.info['dpi'])
    display(ipImage(filename=path, format='png'))
                        #     print(ipImage)
    return [path, image_data, image_data.size]

image_details = [displayRandImage(df_test_squashed, predictions_image_dir) for _ in range(10)]
def make_seq_bins(df_):
    """
    Creates ndarrays of (padded) sequence bins from df_*_squashed / df_*_padded 
    and pickles them as a dictionary of ndarrays wrapped in dataframes.
    This preprocessing is needed in order to quickly obtain an ndarray of
    token-sequences at training time.
    """
    bin_lens = df_.bin_len.unique()
    bins = {}
    bins_squashed = {}
    for len_ in bin_lens:
        df_slice = df_[df_.padded_seq_len == len_]
        bin_ = np.array(df_slice.padded_seq.values.tolist(), dtype=np.int32)
        bin_squashed = np.array(df_slice.squashed_seq.values.tolist(), dtype=np.int32)
        assert bin_.shape[1] == len_
        assert bin_.shape[0] == df_slice.shape[0]
        bins[len_] = pd.DataFrame(bin_, index=df_slice.index)
        bins_squashed[len_] = pd.DataFrame(bin_squashed, index=df_slice.index)
    return bins, bins_squashed

bins_test, bins_sq_test = make_seq_bins(df_test_squashed)
bins_train, bins_sq_train = make_seq_bins(df_train_squashed)
bins_valid, bins_sq_valid = make_seq_bins(df_valid_squashed)

dump_to_disk = True
if dump_to_disk:
        if not os.path.exists(preds_raw_data_dir):
            os.makedirs(preds_raw_data_dir)
        with open(os.path.join(preds_raw_data_dir, 'batch_size.pkl'), 'wb') as f:
            pickle.dump(HYPER_batch_size, f, pickle.HIGHEST_PROTOCOL)

        df_train_squashed.to_pickle(os.path.join(preds_raw_data_dir, 'df_train.pkl'))
        df_test_squashed.to_pickle(os.path.join(preds_raw_data_dir, 'df_test.pkl'))
        df_valid_squashed.to_pickle(os.path.join(preds_raw_data_dir, 'df_valid.pkl'))

        for t in [('train', bins_train, bins_sq_train),
                  ('test', bins_test, bins_sq_test),
                  ('valid', bins_valid, bins_sq_valid)]:
            with open(os.path.join(preds_raw_data_dir, 'raw_seq_%s.pkl'%t[0]), 'wb') as f:
                pickle.dump(t[1], f, pickle.HIGHEST_PROTOCOL)
            with open(os.path.join(preds_raw_data_dir, 'raw_seq_sq_%s.pkl'%t[0]), 'wb') as f:
                pickle.dump(t[2], f, pickle.HIGHEST_PROTOCOL)
        data_props = pd.read_pickle(os.path.join(training_raw_data_dir, 'data_props.pkl'))
        data_props['MaxSeqLen'] = df_test_squashed.padded_seq_len.max()
        with open(os.path.join(preds_raw_data_dir, 'data_props.pkl'), 'wb') as f:
            pickle.dump(data_props, f, pickle.HIGHEST_PROTOCOL)

data_props = pd.read_pickle(os.path.join(preds_raw_data_dir, 'data_props.pkl'))
print(data_props)
import shutil
import glob
from os.path import join as joinpath
shutil.rmtree(preds_logdir, ignore_errors=True)
os.makedirs(preds_logdir)
for f in glob.glob(os.path.join(training_restore_logdir, 'snapshot*')):
    print('copying ' + os.path.basename(f) + ' to ' + preds_logdir)
    shutil.copy2(f, preds_logdir)
print('copying checkpoints_list to ' + preds_logdir)
shutil.copy2(joinpath(training_restore_logdir, 'checkpoints_list'), preds_logdir)

print('sudo python3 run.py -a 0.0001 -e -1 -b 1 -v -1 -i 2 --r-lambda 0.00005 --raw-data-folder {preds_raw_data_dir} --test --save-all-eval --restore {preds_logdir} --image-folder {predictions_image_dir}'\
      .format(preds_raw_data_dir=preds_raw_data_dir, preds_logdir=preds_logdir, predictions_image_dir=predictions_image_dir))
