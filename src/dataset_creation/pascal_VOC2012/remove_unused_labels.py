import os

image_dir = "./single_person_images/"
label_dir = "./single_person_txt/"

removed = 0

for filename in os.listdir(label_dir):
	label_path = label_dir + filename
	img_path = image_dir + filename.replace('.txt','.jpg')
	if os.path.isfile(img_path) == False:
		removed = removed + 1
		print("Image ", filename.replace('.txt','.jpg'), " does not exist")
		print("Removed: ", filename)
		os.remove(label_path)

print("\n")
print("Removed ", removed, " unused labels.")

