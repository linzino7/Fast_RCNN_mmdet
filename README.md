# Mask_RCNN_mmdet
Selected Topics in Visual Recognition using Deep Learning Homework 3 announcement HW3

This Rep is base on [open-mmlab/mmdetection](https://github.com/open-mmlab/mmdetection). 

More detail can see [mmdetection getting start](https://github.com/open-mmlab/mmdetection#getting-started).

## Hardware
- Ubuntu 18.04 LTS
- Intel(R) Core(TM) i7-7820X CPU @ 3.60GHz
- 31 RAM
- NVIDIA GTX 1080 12G *1

## ENV
- CUDA 10.2
- Pytorch 1.6.0  
- mmcv-full latest+torch1.7.0+cu110
- mmdetection master(2020/12/11)

## Install env
```
# getting start mmdectation
# https://github.com/open-mmlab/mmdetection/blob/master/docs/get_started.md

# Pytorch 1.6.0  CUDA 10.2
pip3 install torch==1.7.0+cu110 torchvision==0.8.1+cu110 torchaudio===0.7.0 -f https://download.pytorch.org/whl/torch_stable.html

# Install mmcv-full, we recommend you to install the pre-build package as below.
pip3 install mmcv-full==latest+torch1.7.0+cu110 -f https://download.openmmlab.com/mmcv/dist/index.html

# Clone the MMDetection repository.
git clone https://github.com/open-mmlab/mmdetection.git
cd mmdetection

# Install build requirements and then install MMDetection.
pip3 install -r requirements/build.txt
pip3 install -v -e .  # or "python setup.py develop"
```

## Reproducing Submission
To reproduct my submission without retrainig, do the following steps:

1.  [Dataset Preparation](#Dataset-Preparation)
2.  [Training](#Training)
3.  [Inference](#Inference)

## Dataset Preparation
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
Dataset: https://drive.google.com/drive/folders/1nglaZBJJ_Amonndw4nIVBh_UuCpp4gee?usp=sharing

Download and extract *train_images.zip* and *test_images.zip* to *data* directory.

#### Splited training and validation json used coco style
Use split8020.py to make train.txt .
```
$ python3 split8020.py
```

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
This project used Pre-train model. But according the mmdetection doc, it used pre-train backbone restnet-50 on ImageNet.

The expected training times are:

Model | GPUs | Image size | Training Epochs | Training Time | mAP|
------------ | ------------- | ------------- | ------------- | ------------- | ------------- | 
Fast_RCNN | 1x NVIDIA GTX 1080 | 1333, 800 | 100 | 6 hours | 0.


### Muti-GPU Training
I didn't test muti-GPU training.

## Inference

### Inference single images
you need open mmtosummit.py to change model path and output name
```
$ python3 mmtosummit.py
```
## result
![](https://github.com/linzino7/Fast_RCNN_mmdet/blob/main/imgresult/in_2009_003123.jpg)
![](https://github.com/linzino7/Fast_RCNN_mmdet/blob/main/imgresult/in_2009_003938.jpg)

# mmdetection Modify

# Reference:
- [Mask R-CNN](https://arxiv.org/abs/1703.06870) Paper
- [open-mmlab/mmdetection](https://github.com/open-mmlab/mmdetection)

