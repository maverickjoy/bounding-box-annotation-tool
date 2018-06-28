# ============================== Config ========================================

PARAMS = dict(
	imageFormat	      = 'JPG',                  # Specify Image format [JPG / JPEG / PNG ], Default will be taken as JPG
	sourceImageDirectory  = './Images',  		# Source Directory where all images for annotation are kept
	annotationDirectory   = './Annotation',		# Export Directory where annotations will be stored
	classNames            = '0 1 2'			# Class Names spererated with spaces
)

YOLO = dict(
	imageFormat	      = 'JPG',                  # Specify Image format [JPG / JPEG / PNG ], Default will be taken as JPG
	sourceDirectory       = '009', 			# Directory from which you want to convert annotations
	outputDirectory       = './Output'		# Directory where Yolo annotation output will be saved
)

# ==============================================================================
