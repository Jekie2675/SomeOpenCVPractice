from ImgSearch.ColorDescriptor import ColorDescriptor
from ImgSearch.searcher import Searcher
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--index", required = True,
                help = "path to where the computed index will be stored")
ap.add_argument("-q", "--query", required = True,
                help = "Path to the query image")
ap.add_argument("-r", "--result-path", required = True,
                help = "path to the result path")
args = vars(ap.parse_args())

cd = ColorDescriptor((8, 12, 3))

# load and describe the querry image

query = cv2.imread(args["query"])
features = cd.describe(query)

# perform the search
searcher = Searcher(args["index"])
results = searcher.search(features)

# display the query
cv2.imshow("Query", query)

# loop over the results
for (score, resultID) in results:
    # load the result image and display it
    result = cv2.imread(args["result_path"] + "/" + resultID)
    cv2.imshow("Result", result)
    cv2.waitKey(0)