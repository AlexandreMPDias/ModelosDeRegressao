import pandas as pd
import numpy as np
import statsmodels.api as sm
import scipy.stats as st
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import matplotlib.mlab as mlab

from src.services.files import Filer
from src.services.mixins import DictClass

class Histogram( DictClass):

	def __init__( self, labelMap = None, save = True, output = "", transform = None, **kwargs):
		self.labelMapping = labelMap
		self.save = save
		self.output = output
		self.transform = transform

	def drawMulti( self, dataframe, features, rows = 6, cols = 3):
		self.__beforePlot()

		fig = plt.figure( figsize = ( 20, 20))
		for i, feature in enumerate( features):
			ax = fig.add_subplot( rows, cols, i + 1)
			df = dataframe[feature]
			for df_row in len(df[feature]):
				df.set_value(feature, df_row, self.__transform([df[feature][df_row]])[0])
			dataframe[ feature ].hist( bins = 20, ax = ax, facecolor = 'midnightblue')
			ax.set_title( f"{self.__mapLabel(feature)}", color = 'DarkRed')
			
		fig.tight_layout( pad = 5.0)  
		
		self.__plot("all_metrics")

	def drawSingle( self, values, **kwargs):
		self.__beforePlot()

		accessor = self._accesor(kwargs)

		rawTitle = accessor('title', 'NotAvailable')
		title = self.__mapLabel(rawTitle)
		fileName = accessor('fileName', rawTitle)

		fig = plt.figure()
		plt.title(title)

		counts, bins = np.histogram(self.__transform(values))
		plt.hist(bins[:-1], bins, weights = counts)

		self.__plot(fileName)

	def __transform(self, data):
		if(self.transform == "log"):
			return np.log(data)
		if(self.transform == "percent"):
			return np.multiply(data, 1/max(data))
		if(self.transform is None):
			return data
		return self.transform(data)

	def __beforePlot(self):
		pass


	def __plot(self, fileName):
		if(self.save):
			out = f"{self.output}/{fileName}.fig"
			Filer.write(out, plt)
		else:
			plt.show()

		plt.clf()
		plt.close()


	def __mapLabel( self, feature):
		if self.labelMapping is not None:
			return self._access( self.labelMapping, feature, f"NotAvailable ( {feature})")
		return feature

	def __transparent(self, plot, alpha = 0.25):
		ax = plot.gca()
		for line in ax.get_lines():
			line.set_alpha(alpha)