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
After downloading images and spliting json file, the data directory is structured as:
```
 data/
  | +- train_images/
  | +- test_images/
  | -- pascal_train10.json
  | -- pascal_train90.json
  | -- test.json
```

#### Download Classes Image
Smaill SVHN Dataset: https://drive.google.com/drive/u/1/folders/1Ob5oT9Lcmz7g5mVOcYH3QugA7tV3WsSl

Download and extract *tain.tar.gz* and *test.tar.gz* to *data* directory.

### Splited training and validation json used coco style
Use split8020.py to make train.txt .


## Training
### Setting
You can setting detail Hyperparameters in [configs/mask_rcnn/mask_rcnn_r50_zino.py](https://github.com/linzino7/Fast_RCNN_mmdet/configs/mask_rcnn/mask_rcnn_r50_zino.py)

```
total_epochs = 100
checkpoint_config = dict(interval=1)
log_config = dict(interval=50, hooks=[dict(type='TextLoggerHook')])
dist_params = dict(backend='nccl')
log_level = 'INFO'
load_from = None
resume_from = None
workflow = [('train', 1)]
classes = ('aeroplane', 'bicycle', 'bird', 'boat', 'bottle', 'bus', 'car',
           'cat', 'chair', 'cow', 'diningtable', 'dog', 'horse', 'motorbike',
           'person', 'pottedplant', 'sheep', 'sofa', 'train', 'tvmonitor')
work_dir = './work_dirs/mask_rcnn_r50_caffe_fpn_mstrain-poly_1x_coco_posk_pretrain_200'
gpu_ids = range(1, 1)
```

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
$ python3 mmtosummit.py
```

# mmdetection Modify

# Reference:
[Mask R-CNN](https://arxiv.org/abs/1703.06870) Paper
[open-mmlab/mmdetection](https://github.com/open-mmlab/mmdetection)

