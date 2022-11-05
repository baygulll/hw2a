def swap_list(myList):
	if len(myList) < 2:
		return myList
	middle = int((len(myList)-1)/2)
	temp = myList[middle]
	myList[middle] = myList[len(myList)-1]
	myList[len(myList)-1] = temp
	return myList

