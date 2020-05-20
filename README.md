Project Title
=============

Our title is *Hunter TeXNet* following the tradition of LeCun's *LeNet*
Neural Network architecture [@lecun1998gradient 7] but our investigation
will not be limited to these models.

[Demo Video](https://www.youtube.com/watch?v=ew6JG2c3M24&feature=youtu.be)

[Complete Dataset](https://drive.google.com/file/d/1mwUwoyhcz63mTd3s1v4Q8QoRBPBSzGEi/view?usp=sharing)

Description
===========

The prospect of accurately transcribing mathematical expression into a
markup representation is enticing because it opens the doors for
bringing new life to old mathematical texts or those for which the
source code is unavailable.

Directory Structure (points of focus)
==========

```
TEXNET
│   
│      
│
└───data -> has to be made by the user (extract data folder in there)
│   │   
│   │   
│   │
│   └───formula_images
│       │   *.png    
│   
└───src -> main directory of where model will be ran
│   │   
│   │   
│   │
│   └───tools
│   │   │   prepareData.py -> run first when images are placed in inference folder
│   │   │   predict.py -> run this script after running the model based on the script outputted from prepareData.py
│   │   │   predictions.csv -> outputted csv with filenames and LaTeX predictions
│   │   
│   │   
│   │
│   └───tb_metrics -> main logging directory where logs from model training will be stored
│   │
│   │
│   │  run.py -> main file that runs the model, has settable hyperparameters and variables that need to be specified based on the training machine
|
└───predictions
│   │   
│   │   
│   │
│   └───formula_images -> paste images to perform inference on here before running inference scripts

```
For More Model Information, Scripts to Run, and Downloadable Datasets checkout Singh's repo page:
https://github.com/untrix/im2latex
