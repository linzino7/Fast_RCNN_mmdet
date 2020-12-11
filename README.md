# Fast_RCNN_mmdet
Selected Topics in Visual Recognition using Deep Learning Homework 3 announcement HW3

This Rep is base on [open-mmlab/mmdetection](https://github.com/open-mmlab/mmdetection). 
More detail can see [mmdetection eetting start](https://github.com/open-mmlab/mmdetection#getting-started).

## Hardware
- Ubuntu 18.04 LTS
- Intel(R) Core(TM) i7-7820X CPU @ 3.60GHz
- 31 RAM
- NVIDIA GTX 1080 12G *1

## Reproducing Submission
To reproduct my submission without retrainig, do the following steps:

1.  [Dataset Preparation](#Dataset-Preparation)
2.  [Training](#Training)
3.  [Inference](#Inference)

## Dataset Preparation
All required files except images are already in data directory.
If you generate CSV files (duplicate image list, split, leak.. ), original files are overwritten. The contents will be changed, but It's not a problem.

### Prepare Images
After downloading images, the data directory is structured as:
```
train.txt
  +- data/
  | +- train/
  | +- test/
  | +- training_labels.csv
  | +- val.txt

```

#### Download Classes Image
Smaill SVHN Dataset: https://drive.google.com/drive/u/1/folders/1Ob5oT9Lcmz7g5mVOcYH3QugA7tV3WsSl

Download and extract *tain.tar.gz* and *test.tar.gz* to *data* directory.

### Splited training and validation json used coco style
Use split8020.py to make train.txt .

```
# train.txt and val.txt  
# left(x1) top(y1)  right(x2) bottom(y2) label
image_path1 x1,y1,x2,y2,id x1,y1,x2,y2,id x1,y1,x2,y2,id ...
image_path2 x1,y1,x2,y2,id x1,y1,x2,y2,id x1,y1,x2,y2,id ...
...
```

Names file  example is in [data/SVHN.names](https://github.com/linzino7/pytorch-YOLOv4/blob/master/data/SVHN.names)
```
# names file
Label1
Label2
Label3
...
```

## Training
### Setting
You can setting bach size and epoch in [cfg.py](https://github.com/linzino7/pytorch-YOLOv4/blob/master/cfg.py)

### Train models
To train models, run following commands.
```
$ python3 mmdetection/tools/train.py configs/mask_rcnn/mask_rcnn_r50_zino.py
```
The expected training times are:

Model | GPUs | Image size | Training Epochs | Training Time | Bach Size |
------------ | ------------- | ------------- | ------------- | ------------- | -------------|
Fast_RCNN | 1x NVIDIA GTX 1080 | 608x608 | 1 | 2.5 hours | 4 |


### Muti-GPU Training
I didn't test muti-GPU training.

## Inference

### Inference single images
```
$ 
```

# mmdetection Modify

# Reference:


