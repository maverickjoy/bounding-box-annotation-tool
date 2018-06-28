# -*- coding: utf-8 -*-
import os
from os import walk, getcwd
from PIL import Image
import config


class YoloConvertor():

	def __init__(self):
		self.imageFormat = config.YOLO['imageFormat']
		self.annotationDir = os.path.join(
			config.PARAMS['annotationDirectory'], config.YOLO['sourceDirectory'])
		self.imgPath = os.path.join(
			config.PARAMS['sourceImageDirectory'], config.YOLO['sourceDirectory'])
		self.outPath = os.path.join(
			config.YOLO['outputDirectory'], config.YOLO['sourceDirectory'])
		self.annotationFilesList = []

	def _conversion(self, size, box):
		dw = 1. / size[0]
		dh = 1. / size[1]
		x = (box[0] + box[1]) / 2.0
		y = (box[2] + box[3]) / 2.0
		w = box[1] - box[0]
		h = box[3] - box[2]
		x = x * dw
		w = w * dw
		y = y * dh
		h = h * dh
		return (x, y, w, h)

	def _process(self):
		for annotationFileName in self.annotationFilesList:
			annotationFilePath = os.path.join(
				self.annotationDir, annotationFileName)
			print "Annotation File Path : ", annotationFilePath

			annotationFile = open(annotationFilePath, "r")
			lines = annotationFile.read().split("\n")

			outputFilePath = os.path.join(self.outPath, annotationFileName)
			print "Output File Path : ", outputFilePath

			outputFile = open(outputFilePath, "w")

			cnt = 0
			for line in lines:
				if(len(line) >= 2):
					cnt += 1
					print "Line : ", line, " \n"
					elems = line.split(' ')
					xmin = elems[0]
					xmax = elems[2]
					ymin = elems[1]
					ymax = elems[3]
					classNo = elems[4]

					if self.imageFormat == "PNG":
						image = self.imgPath + \
							"/%s.png" % (os.path.splitext(annotationFileName)[0])
					else:
						image = self.imgPath + \
							"/%s.jpg" % (os.path.splitext(annotationFileName)[0])


					im = Image.open(image)
					w = int(im.size[0])
					h = int(im.size[1])

					b = (float(xmin), float(xmax), float(ymin), float(ymax))
					bb = self._conversion((w, h), b)
					outputFile.write(str(classNo) + " " +
									 " ".join([str(a) for a in bb]) + '\n')


					if self.imageFormat == "PNG":
						image_name = self.outPath + \
							"/%s.png" % (os.path.splitext(annotationFileName)[0])
						im.save(image_name, "PNG")
					else:
						image_name = self.outPath + \
							"/%s.jpg" % (os.path.splitext(annotationFileName)[0])
						im.save(image_name, "JPEG")

		return

	def start(self):
		if not os.path.exists(self.outPath):
			os.mkdir(self.outPath)

		filesPresent = False
		for (dirpath, dirnames, filenames) in walk(self.annotationDir):
			self.annotationFilesList.extend(filenames)
			if self.annotationDir:
				filesPresent = True
				print self.annotationFilesList
			break
		if not filesPresent:
			print "No Annotated Files Present in the Directory : ", self.annotationDir
			return

		self._process()
		return


if __name__ == "__main__":
	convertorObj = YoloConvertor()
	convertorObj.start()
