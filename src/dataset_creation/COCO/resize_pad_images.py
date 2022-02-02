import numpy as np
import cv2
import os
import math
	
for j in range(1): # train and test	
	if j == 0:
		read_folder = '/home/nm/Downloads/coco_dataset_person/coco_person_images2/'
		read_label = '/home/nm/Downloads/coco_dataset_person/coco_person_labels/'
	for filename in os.listdir(read_folder):
		img = cv2.imread(os.path.join(read_folder,filename)) # read img
		
		top = math.floor((640 - img.shape[0]) / 2)
		bottom = math.ceil((640 - img.shape[0]) / 2)
		left = math.floor((640 - img.shape[1]) / 2)
		right = math.ceil((640 - img.shape[1]) / 2)
		
		if j == 0:
			label_to_correct = read_label + filename.replace('.jpg', '.txt')
			#print(label_to_correct)
			f = open(label_to_correct, "r")
			
			temp_label = (f.read().split(","))
			#print(temp_label)
			for k in range (4):
				temp_label[k] = round(float(temp_label[k]))
			
			scaling = 500/640
			# xmin, ymin, xmax, ymax
			temp_label[0] = int(round((temp_label[0] + left) * scaling))
			temp_label[1] = int(round((temp_label[1] + top) * scaling))
			temp_label[2] = int(round((temp_label[2] + left) * scaling))
			temp_label[3] = int(round((temp_label[3] + top) * scaling))
			
			corrected_label = str(int(temp_label[0])) + ', ' + str(int(temp_label[1])) + ', ' + str(int(temp_label[2])) + ', ' + str(int(temp_label[3])) 
			
			f.close()
			open(label_to_correct, "w").close()
			f = open(label_to_correct, "w")
			f.write(corrected_label)
			f.close()
		
		#print(img.shape)
		
		img = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT)

		#print(img.shape)
		dims = (500, 500)
		img = cv2.resize(img, dims, interpolation = cv2.INTER_AREA)
		cv2.imwrite(os.path.join(read_folder,filename), img)
