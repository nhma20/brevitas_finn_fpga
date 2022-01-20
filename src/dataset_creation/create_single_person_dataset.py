import xml.etree.ElementTree as ET
import os
from shutil import copyfile

annotations_dir = "./Annotations/"


for filename in os.listdir(annotations_dir):
	annot_xml = os.path.join(annotations_dir,filename)
	tree = ET.parse(annot_xml)
	root = tree.getroot()

	n_person = 0
	for name in root.iter('object'):
		#print(name.find('name').text)
		if name.find('name').text == 'person':
			n_person += 1



	if n_person == 0:
	
		bbox_string = "0, 0, 0, 0"
		dst = "./single_or_no_person_dataset/no_person_txt/" + filename.replace(".xml", ".txt")
		f = open(dst, "a")
		f.write(bbox_string)
		f.close()
		
		src = "./JPEGImages/" + filename.replace(".xml", ".jpg")
		dst = "./single_or_no_person_dataset/no_person_images/" + filename.replace(".xml", ".jpg")
		copyfile(src, dst)


	if n_person == 1:
		
		bbox_string = ""
		for name in root.iter('object'):
			#print(name.find('name').text)
			if name.find('name').text == 'person':
				for vals in name.iter('bndbox'):
					bbox_string += vals.find('xmin').text + ", "
					bbox_string += vals.find('ymin').text + ", "
					bbox_string += vals.find('xmax').text + ", "
					bbox_string += vals.find('ymax').text
					break
			
		temp_label = bbox_string.split(",")
		for k in range (4):
		    temp_label[k] = round(float(temp_label[k]))
            
        # remove very small bounding box images
		if (abs(temp_label[0] - temp_label[2]) > 50) and (abs(temp_label[1] - temp_label[2]) > 100):
		    # remove very wide bounding boxes
		    if (abs(temp_label[0] - temp_label[2]) < 300):
		        # remove bounding box images wider than higher
		        if (abs(temp_label[0] - temp_label[2]) < abs(temp_label[1] - temp_label[3])):
	
		            dst = "./single_or_no_person_dataset/single_person_txt/" + filename.replace(".xml", ".txt")
		            f = open(dst, "a")
		            f.write(bbox_string)
		            f.close()
				
		            src = "./JPEGImages/" + filename.replace(".xml", ".jpg")
		            dst = "./single_or_no_person_dataset/single_person_images/" + filename.replace(".xml", ".jpg")
		            copyfile(src, dst)



	#print(n_person)
	
	#quit()

