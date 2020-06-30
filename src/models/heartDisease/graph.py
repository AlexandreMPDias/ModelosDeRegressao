from src.models.heartDisease.shaper import DataFrameShaper
from src.services.graph import Histogram

class DataFrameGraph:
	def __init__(self, shaper: DataFrameShaper):
		self.shaper = shaper

	def histogram(self, features = None, multi = False, histOptions = {}):
		features = features if features is not None else self.shaper.data.columns

		hist = self.__loadHistogram(histOptions)

		if multi:
			hist.drawMulti(self.shaper.data, features)
		else:
			try:
				hist.drawSingle(self.shaper.data[features], title = features)
			except:
				for feat in features:
					hist.drawSingle(self.shaper.data[feat], title = feat)
		return self

	def __loadHistogram(self, kwargs = {}):
		return Histogram(labelMap = self.shaper.langMap, **kwargs)
