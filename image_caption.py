# code to write to a json a dictionary containing captions image-wise. Data taken from coco caption jsons
# (captions_train2017.json, captions_val2017.json)


import json


with open('captions_train2017.json') as in_file:
	data = json.load(in_file)

with open('captions_val2017.json') as in_file2:
	data2 = json.load(in_file2)

annotations = data['annotations'] + data2['annotations']

dict_cap = {}

count = 0

for item in annotations:
	image_id = item['image_id']
	caption = item['caption']
	if(image_id in dict_cap.keys()):
		dict_cap[image_id].append(caption)
	else:
		dict_cap[image_id] = [caption]
	print count
	count += 1

print len(dict_cap)
print len(data['images'])
print dict_cap[118113]

with open('captions.json', 'w') as out_file:
	out_file.write(json.dumps(dict_cap))
