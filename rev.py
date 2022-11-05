def reverse_list(myList):
	return reverse_list_recursive(myList, 0)

def reverse_list_recursive(myList, index):
	if index >= len(myList)/2:
		return myList
	else:
		temp = myList[index]
		myList[index] = myList[len(myList) - 1 - index]
		myList[len(myList) - 1 - index] = temp
		return reverse_list_recursive(myList, index+1)


