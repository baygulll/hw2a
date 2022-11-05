def sort_dictionary(myDict):
	output = []
	while len(myDict) > 0:
		minAge = list(myDict.values())[0][1]
		minKey = list(myDict.keys())[0]
		for key in myDict:
			if(myDict.get(key)[1] < minAge):
				minKey = key

		output.append((minKey, myDict.get(key)[0]))
		myDict.pop(minKey)

	return output
