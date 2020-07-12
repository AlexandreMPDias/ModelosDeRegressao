import pandas as pd
import numpy as np
import statsmodels.api as sm
import scipy.stats as st
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import matplotlib.mlab as mlab
from src.services.files import Filer

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
				# self.__drawSingleHistogram(self.shaper.data[features], title = features, outputDir = "next/")
				hist.drawSingle(self.shaper.data[features], title = features)
			except:
				for feat in features:
					# self.__drawSingleHistogram(self.shaper.data[feat], title = feat, outputDir = "next/")
					hist.drawSingle(self.shaper.data[feat], title = feat)
					break
		return self

	def draw(self, x,y, title, key):
		fig = plt.figure()
		plt.title(title)
		plt.plot(x,y, "ro")
		Filer.write(f"histograms/dispersion/{key}.fig", plt)
		# plt.show()

	def __loadHistogram(self, kwargs = {}):
		return Histogram(labelMap = self.shaper.langMap, **kwargs)
