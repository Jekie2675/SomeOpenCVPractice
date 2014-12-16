from ImgSearch.ColorDescriptor import ColorDescriptor
import argparse
import glob
import cv2

# construct the argument parser and parse them
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required = True,
                help = "Path to the directory")
ap.add_argument("-i", "--index", required = True,
                help = "Path the where the computed index will be sortered")
args = vars(ap.parse_args())

# initialize the color descriptor
# 8 Hue bins - 12 Saturation bins - 3 Value bins
cd = ColorDescriptor((8, 12, 3))

# open the output index file for writig
output = open(args["index"], "w")

# use glob to grab the image paths and loop over them
for imagePath in glob.glob(args["dataset"] + "/*.png"):
    # extract filename
    # path and load image itself
    imageID = imagePath[imagePath.rfind("/") + 1:]
    image = cv2.imread(imagePath)

    # describe the image & write to the file
    features = cd.describe(image)

    features = [str(f) for f in features]
    output.write("%s,%s\n" % (imageID[len(args["dataset"]) + 1 :], ",".join(features)))
    print imageID, "---", imagePath
output.close()