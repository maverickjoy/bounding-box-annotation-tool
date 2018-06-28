import glob, os

# ============================== Config ========================================

DATA_PATH       = 'data/obj/'			# Directory where the data will reside, relative to 'darknet.exe'
TEST_PERCENTAGE = 30				# Test Image Percentage
IMAGE_FORMAT    = 'jpg'				# Image Format of your data [jpg / png / jpeg]

# ============================== Config ========================================



def process():
	# Create and/or truncate train.txt and test.txt
	file_train = open('train.txt', 'w')
	file_test = open('test.txt', 'w')

	# Populate train.txt and test.txt
	counter = 1
	index_test = round(100 / TEST_PERCENTAGE)
	filesPresent = False

	for pathAndFilename in glob.iglob(os.path.join(DATA_PATH, str("*." + IMAGE_FORMAT) )):
		title, ext = os.path.splitext(os.path.basename(pathAndFilename))
		filesPresent = True
		if counter == index_test:
			counter = 1
			file_test.write(DATA_PATH + title + '.' + IMAGE_FORMAT + "\n")
		else:
			file_train.write(DATA_PATH + title + '.' + IMAGE_FORMAT + "\n")
			counter = counter + 1

	if not filesPresent:
		print "No Files Present in the Directory : ", DATA_PATH

	return

if __name__ == "__main__":
	process()
