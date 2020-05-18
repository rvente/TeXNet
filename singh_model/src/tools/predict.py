import sys
sys.path.extend(['../commons'])
import data_commons as dtc
import os
import dl_commons as dlc
import viz_commons as vc
from viz_commons import VisualizeDir, DiffParams, VisualizeStep

preds_vd = VisualizeDir(os.path.expanduser('/home/vente_ralph_d/TeXNet.ai/singh_model/predictions/logdir/store'))
preds_vs = VisualizeStep(preds_vd, 'test', 58220)
df = preds_vs.strs(key='predicted_ids', trim=True, sortkey='prediction_prob', keys=['image_name', 'prediction_log_prob'], sort_ascending=False, wrap_strs=True)
df = df[['image_name', 'prediction_log_prob', 'prediction_prob', 'predicted_ids']].rename(columns={'predicted_ids':'latex'})
print(df.shape)
df.drop_duplicates(inplace=True)
print(df.shape)
df = df.set_index('image_name')
print(df)

df.to_csv('predictions.csv')
