import os

def data(*names):
	base = os.path.join(".","data")
	relative = os.path.join(*names)
	return os.path.join(base, relative)

class PathResolver:
	DATA_SET = data("dataset", "heart-disease-prediction-using-logistic-regression.csv")

paths = PathResolver()