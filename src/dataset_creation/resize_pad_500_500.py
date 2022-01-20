import numpy as np
import cv2
import os
import math
	
for j in range(2): # train and test	
	if j == 0:
		read_folder = '/home/nm/Downloads/VOCdevkit/VOC2012/single_or_no_person_dataset/single_person_images/'
		read_label = '/home/nm/Downloads/VOCdevkit/VOC2012/single_or_no_person_dataset/single_person_txt/'
	if j == 1:
		read_folder = '/home/nm/Downloads/VOCdevkit/VOC2012/single_or_no_person_dataset/no_person_images/'
		read_label = '/home/nm/Downloads/VOCdevkit/VOC2012/single_or_no_person_dataset/no_person_txt/'
	for filename in os.listdir(read_folder):
		img = cv2.imread(os.path.join(read_folder,filename)) # read img as grayscale
		
		top = math.floor((500 - img.shape[0]) / 2)
		bottom = math.ceil((500 - img.shape[0]) / 2)
		left = math.floor((500 - img.shape[1]) / 2)
		right = math.ceil((500 - img.shape[1]) / 2)
		
		if j == 0:
			label_to_correct = read_label + filename.replace('.jpg', '.txt')
			#print(label_to_correct)
			f = open(label_to_correct, "r")
			
			temp_label = (f.read().split(","))
			#print(temp_label)
			for k in range (4):
				temp_label[k] = round(float(temp_label[k]))
			
			# xmin, ymin, xmax, ymax
			temp_label[0] = temp_label[0] + left
			temp_label[1] = temp_label[1] + top
			temp_label[2] = temp_label[2] + left
			temp_label[3] = temp_label[3] + top
			
			corrected_label = str(int(temp_label[0])) + ', ' + str(int(temp_label[1])) + ', ' + str(int(temp_label[2])) + ', ' + str(int(temp_label[3])) 
			
			f.close()
			open(label_to_correct, "w").close()
			f = open(label_to_correct, "w")
			f.write(corrected_label)
			f.close()
		
		#print(img.shape)
		
		img = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT)

		#print(img.shape)
		
		cv2.imwrite(os.path.join(read_folder,filename), img)
