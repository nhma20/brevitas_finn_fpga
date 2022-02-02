from pycocotools.coco import COCO
import requests

# instantiate COCO specifying the annotations json path
coco = COCO('/home/nm/Downloads/coco_dataset_person/annotations/instances_train2017.json')
# Specify a list of category names of interest
catIds = coco.getCatIds(catNms=['person'])
# Get the corresponding image ids and images using loadImgs
imgIds = coco.getImgIds(catIds=catIds)
images = coco.loadImgs(imgIds)

# Save the images into a local folder
for im in images:
    img_data = requests.get(im['coco_url']).content
    print(im)
    with open('/home/nm/Downloads/coco_dataset_person/coco_person_images/' + im['file_name'], 'wb') as handler:
        handler.write(img_data)
