Extracting single-person images from COCO
----------------------------------------------------------------------------

## Flow
1. Download COCO annotations .json: `wget http://images.cocodataset.org/annotations/annotations_trainval2017.zip`.
2. Update paths in `get_person_images.py` and run to download images with people (takes many hours @ ~2 images/sec).
3. Update paths in `remove_multiple_person.py` and run to save images with only single persons and create label files.
4. Update paths in `resize_pad_images.py` and run to resize and pad all images to same dimensions and fix label files.
5. (Optional) After manual pruning of bad images, update paths in and run `remove_ununsed_labels.py` to remove labels without matching images.



## TODO
- Fix `get_person_images.py` such that only images with single persons are downloaded.
- Find optimal bounding box size in `remove_multiple_person.py` to avoid manual sorting of dataset afterwards.
