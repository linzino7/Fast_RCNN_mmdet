# The new config inherits a base config to highlight the necessary modification
#_base_ = 'mask_rcnn/mask_rcnn_r50_caffe_fpn_mstrain-poly_1x_coco.py'
_base_ = '../../mmdetection/configs/mask_rcnn/mask_rcnn_r50_caffe_fpn_mstrain-poly_3x_coco.py'

# We also need to change the num_classes in head to match the dataset's annotation
model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=20),
        mask_head=dict(num_classes=20)))

# Modify dataset related settings
#dataset_type = 'COCODataset'
classes = ('aeroplane','bicycle','bird','boat','bottle',
               'bus','car','cat','chair','cow','diningtable',
               'dog','horse','motorbike','person','pottedplant',
               'sheep','sofa','train','tvmonitor',)
data = dict(
    samples_per_gpu = 1,
    workers_per_gpu = 0,
    train=dict(
        img_prefix='data/train_images/',
        classes=classes,
        ann_file='data/pascal_train90.json'),
    val=dict(
        img_prefix='data/train_images/',
        classes=classes,
        ann_file='data/pascal_train10.json'),
    test=dict(
        img_prefix='data/test_images/',
        classes=classes,
        ann_file='data/test.json'))

total_epochs = 2

# We can use the pre-trained Mask RCNN model to obtain higher performance
#load_from = 'checkpoints/mask_rcnn_r50_caffe_fpn_mstrain-poly_3x_coco_bbox_mAP-0.408__segm_mAP-0.37_20200504_163245-42aa3d00.pth'
