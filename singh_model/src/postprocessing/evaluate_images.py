
# coding: utf-8

# # im2latex
# 
# &copy; Copyright 2017-2018 Sumeet S Singh
# 
#     This file is part of im2latex solution by Sumeet S Singh.
# 
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the Affero GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
# 
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     Affero GNU General Public License for more details.
# 
#     You should have received a copy of the Affero GNU General Public License
#     along with this program.  If not, see <http://www.gnu.org/licenses/>.

# In[1]:


import sys
sys.path.extend(['../commons'])


# In[2]:


from IPython.core.display import display, HTML
display(HTML("<style>.container { width:90% !important; }</style>"))


# In[3]:


import pandas as pd
import os
import re
import codecs
from IPython.display import display, Math, Latex
from IPython.display import Image as ipImage
from six.moves import cPickle as pickle
import string
from PIL import Image
import numpy as np
import h5py
import matplotlib as mpl
from matplotlib import pyplot as plt
from mpl_toolkits.axes_grid1 import ImageGrid
# Config the matplotlib backend as plotting inline in IPython
get_ipython().magic('matplotlib inline')


# In[4]:


pd.options.display.max_rows = 50
pd.options.display.max_colwidth = 600
pd.options.display.expand_frame_repr = False
pd.options.display.colheader_justify = 'left'


# In[5]:


import data_commons as dtc
import dl_commons as dlc
import viz_commons as viz
from viz_commons import VisualizeDir, DiffParams, VisualizeStep


# ### Notebook Arguments
# ----------------------

# In[7]:


# storedir = '/zpool_3TB/i2l/tb_metrics/2017-12-21 02-20-10 PST 140K_score_89.0/test_runs/step_00168100_score89.0_publish/store_2'
storedir = '/zpool_3TB/i2l/tb_metrics/2017-12-25 21-04-15 PST 140K_noRegroup_score89.09/test_runs/step_00167526_score89.0_publish/store_2'
# storedir = '/zpool_3TB/i2l/tb_metrics/2017-12-16 18-51-38 PST pLambda=0_score_88.86/test_runs/step_00132200_score88.19_publish/store_2'

clobber = False
dump = False

original_image_dir = '/zpool_3TB/i2l/data/dataset5/formula_images'
rel_dumpdir = 'eval_images'
dumpdir = os.path.join(storedir, rel_dumpdir)
rendered_dir = os.path.join(storedir, rel_dumpdir, 'rendered_images')


# ____________________________________

# In[8]:


vd = VisualizeDir(os.path.expanduser(storedir))
last_step = vd.view_steps()[1][-1]
print('last_step = %d' % last_step)
vs = VisualizeStep(vd, 'test', last_step)
df, df_result, df_data, sr_label = vs.get_preds(rel_dumpdir=rel_dumpdir, dump=dump, clobber=clobber)
# df = vs.dump_preds(rel_dumpdir=rel_dumpdir, dump=dump)


# In[11]:


df


# In[12]:


df_result


# In[13]:


df_data


# In[14]:


sr_label


# ### Render Images
# Render images using render_latex.py (https://github.com/untrix/im2latex/blob/master/thirdparty/harvardnlp_im2markup/scripts/evaluation/render_latex.py) which is derived from harvardnlp code base (https://github.com/harvardnlp/im2markup). See their github page for details on how to run the script.

# In[14]:


# for image in df.image_name:
#     os.symlink(os.path.join(original_image_dir, image), os.path.join(golden_image_dir, image))


# ### Evaluate images
# Evaluate image match using evaluate_image.py (https://github.com/untrix/im2latex/blob/master/thirdparty/harvardnlp_im2markup/scripts/evaluation/evaluate_image.py) also from harvard nlp code base. See their github page for details on how to run the script. However, make sure to use the code from this repository because it has been modified to produce an unmatched_files.txt output.
