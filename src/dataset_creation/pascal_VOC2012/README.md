Extracting single-person images from Pascal_VOC2012
----------------------------------------------------------------------------

## Flow
1. Download Pascal VOC 2012 dataset: http://host.robots.ox.ac.uk/pascal/VOC/voc2012/VOCtrainval_11-May-2012.tar
2. Update paths in `create_single_person_dataset.py` and run to save images with only single persons and create label files.
3. Update paths in `resize_pad_images.py` and run to resize and pad all images to same dimensions and fix label files.
4. (Optional) After manual pruning of bad images, update paths in and run `remove_ununsed_labels.py` to remove labels without matching images.



## TODO
- Find optimal bounding box size in `create_single_person_dataset.py` to avoid manual sorting of dataset afterwards.
