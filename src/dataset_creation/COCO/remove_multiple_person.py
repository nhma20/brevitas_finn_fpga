import IPython
import os
import json
import random
import shutil
import numpy as np
import requests
from io import BytesIO
import base64
from math import trunc
from PIL import Image as PILImage
from PIL import ImageDraw as PILImageDraw

        
## Derived from: https://gist.github.com/akTwelve/dc79fc8b9ae66828e7c7f648049bc42d
  
def main():
	annotation_path = '/home/nm/Downloads/coco_dataset_person/annotations/instances_train2017.json'
	#annotation_path = '/home/nm/Downloads/coco_dataset_person/annotations/instances_val2017.json'
	image_dir = "/home/nm/Downloads/coco_dataset_person/coco_person_images_copy/"
	label_dir = "/home/nm/Downloads/coco_dataset_person/coco_person_labels/"

	coco_dataset = CocoDataset(annotation_path, image_dir)
	
	
	img_id = ""
	filename_no_jpg = ""
	its = 0
	for filename in os.listdir(image_dir):
		img_id = filename.replace(".jpg", "")
		for i in range(len(filename)):
			if filename[i] == "0":
				img_id = img_id[1 : :]
			else:
				break
			
		img_id = int(img_id)
		print("ID: ", img_id)	
		coco_dataset.display_image(img_id, filename)
		
		its += 1
		#if its > 10:
		#	break
	

    
    
# Load the dataset json
class CocoDataset():
    def __init__(self, annotation_path, image_dir):
        self.annotation_path = annotation_path
        self.image_dir = image_dir
        self.colors = colors = ['blue', 'purple', 'red', 'green', 'orange', 'salmon', 'pink', 'gold',
                                'orchid', 'slateblue', 'limegreen', 'seagreen', 'darkgreen', 'olive',
                               'teal', 'aquamarine', 'steelblue', 'powderblue', 'dodgerblue', 'navy',
                               'magenta', 'sienna', 'maroon']
        
        print("Opening annotation .json...")
        json_file = open(self.annotation_path)
        self.coco = json.load(json_file)
        json_file.close()
        
        self.process_info()
        self.process_licenses()
        self.process_categories()
        self.process_images()
        self.process_segmentations()

    
    def display_image(self, image_id, filename):
        """
        print('Image:')
        print('======')

        # Print the image info
        image = self.images[image_id]
        for key, val in image.items():
            print('  {}: {}'.format(key, val))
            
        
        # Create list of polygons to be drawn
		
        print('  segmentations ({}):'.format(len(self.segmentations[image_id])))
        """
        num_people = 0
        for i, segm in enumerate(self.segmentations[image_id]):
            polygons_list = []
            if segm['category_id'] == 1:
            	if segm['iscrowd'] != 0:
            		num_people = 2
            		
            	num_people += 1
            	bbox = segm['bbox']
            	
            if num_people == 0:
            	print("No people in annotation \n")
            if num_people > 1:
            	print("More than 1 person in annotation \n")
            	break


        if num_people < 2:
            temp_label = [round(bbox[0]),round(bbox[1]),round(bbox[0]+bbox[2]),round(bbox[1]+bbox[3])]
            # remove very small bounding box images
            if (abs(temp_label[0] - temp_label[2]) > 85) and (abs(temp_label[1] - temp_label[2]) > 100):
                # remove very wide bounding boxes
                if (abs(temp_label[0] - temp_label[2]) < 300):
                    # remove bounding box images wider than higher
                    if (abs(temp_label[0] - temp_label[2]) < abs(temp_label[1] - temp_label[3])):
					
                        bbox_string = str(round(bbox[0])) + ", " + str(round(bbox[1])) + ", " + str(round(bbox[0]+bbox[2])) + ", " + str(round(bbox[1]+bbox[3]))
                        print("Bbox: ", bbox_string, "\n")

                        dst = "/home/nm/Downloads/coco_dataset_person/coco_person_labels/" + filename.replace(".jpg", ".txt")
                        f = open(dst, "a")
                        f.write(bbox_string)
                        f.close()
						
                        src_path = "/home/nm/Downloads/coco_dataset_person/coco_person_images_copy/" + filename
                        dst_path = "/home/nm/Downloads/coco_dataset_person/coco_person_images2/" + filename
                        shutil.move(src_path, dst_path)
        
       
    def process_info(self):
       	print("Processing info...")
       	self.info = self.coco['info']
    
    def process_licenses(self):
       	print("Processing licences...")
        self.licenses = self.coco['licenses']
    
    def process_categories(self):
       	print("Processing categories...")
        self.categories = {}
        self.super_categories = {}
        for category in self.coco['categories']:
            cat_id = category['id']
            super_category = category['supercategory']
            
            # Add category to the categories dict
            if cat_id not in self.categories:
                self.categories[cat_id] = category
            else:
                print("ERROR: Skipping duplicate category id: {}".format(category))

            # Add category to super_categories dict
            if super_category not in self.super_categories:
                self.super_categories[super_category] = {cat_id} # Create a new set with the category id
            else:
                self.super_categories[super_category] |= {cat_id} # Add category id to the set
                
    def process_images(self):
       	print("Processing images...")
       	its = 0
        self.images = {}
        for image in self.coco['images']:
            image_id = image['id']
            if image_id in self.images:
                print("ERROR: Skipping duplicate image id: {}".format(image))
            else:
                self.images[image_id] = image
            its = its + 1
        print("Images in annotation: ", its)
                
                
    def process_segmentations(self):
       	print("Processing segmentations...")
        self.segmentations = {}
        for segmentation in self.coco['annotations']:
            image_id = segmentation['image_id']
            if image_id not in self.segmentations:
                self.segmentations[image_id] = []
            self.segmentations[image_id].append(segmentation)
    
    
if __name__ == "__main__":
    main()
