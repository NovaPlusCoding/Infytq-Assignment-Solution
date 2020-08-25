#PF-Prac-12
def generate_sentences(subjects,verbs,objects):
	sentence_list = []
	for sub in subjects:
	    for verb in verbs:
	        for obj in objects:
	            sentence_list.append(sub + ' ' + verb + ' ' + obj)
	return sentence_list

subjects=["I","You"]
verbs=["love", "play"]
objects=["Hockey","Football"]
print(generate_sentences(subjects,verbs,objects))
