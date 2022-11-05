import time

def timeme(func):
	def wrapper():
		initialTime = time.time()
		func()
		finalTime = time.time() - initialTime
		print("Total time " + str(finalTime))
	return wrapper


