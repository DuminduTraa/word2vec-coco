import numpy as np 
import json
np.set_printoptions(suppress=True)

cosine_sim_thres = 0.3

embedding_file = open("coco_embeddings", 'r')
coco_embeddings = np.loadtxt(embedding_file)


#Calculating cosine similarity matrix and saving to file
cosine_sim = np.matmul(coco_embeddings, coco_embeddings.T)

cosine_sim_file = open("cosine_sim", "w")
np.savetxt(cosine_sim_file, cosine_sim)


# find anomal word from user input words
word_file =  open("words", "r")
labels_str = word_file.read()
labels = labels_str.split()

with open("coco_embeddings.json") as f:
		coco_emb_dict = json.load(f)

input_labels = raw_input("input labels: ").split()

for label in input_labels:
	avg_cosine_sim = 0
	for label2 in input_labels:
		avg_cosine_sim += np.dot(coco_emb_dict[label], coco_emb_dict[label2])
	avg_cosine_sim -= 1  	# to remove 1 from dot product of same class
	avg_cosine_sim /= len(input_labels) - 1

	print avg_cosine_sim
	if avg_cosine_sim < cosine_sim_thres:
		print (label)
