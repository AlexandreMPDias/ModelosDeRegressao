from src.models.heartDisease.shaper import DataFrameShaper
from src.models.heartDisease.graph import DataFrameGraph
from src.models.heartDisease.columns import HeartColumn
from scipy.stats import skew

import pandas as pd


from src.services.mixins import DictClass

class Description(DictClass):
	def __init__(self, shaper: DataFrameShaper, graph: DataFrameGraph):
		self.__graph = graph
		self.__describe = shaper.data.describe()
		self.__shaper = shaper

		self.count_all = [self.__describe[col]['count'] for col in HeartColumn.options]
		self.mean_all = [self.__describe[col]['mean'] for col in HeartColumn.options]
		self.std_all = [self.__describe[col]['std'] for col in HeartColumn.options]
		self.max_all = [self.__describe[col]['max'] for col in HeartColumn.options]
		self.min_all = [self.__describe[col]['min'] for col in HeartColumn.options]

	def count(self, col = None):
		if col is None:
			return self.count_all
		return self.__describe[col]['count']

	def mean(self, col = None):
		if col is None:
			return self.mean_all
		return self.__describe[col]['mean']

	def std(self, col = None):
		if col is None:
			return self.std_all
		return self.__describe[col]['std']

	def min(self, col = None):
		if col is None:
			return self.min_all
		return self.__describe[col]['min']

	def max(self, col = None):
		if col is None:
			return self.max_all
		return self.__describe[col]['max']

	def kurtosis(self, col = None):
		data = self.__shaper.data
		if col is None:
			out = {}
			for p in HeartColumn.options:
				out[p] = self.kurtosis(p)
			return out
		return data[col].kurtosis()

	def skew(self, col = None):
		data = self.__shaper.data
		if col is None:
			out = {}
			for p in HeartColumn.options:
				out[p] = self.skew(p)
			return out
		return skew(data[col].values)

	def all(self, transpose = False):
		data = []

		cols = ['count', 'mean', 'std', 'max', 'min', 'kurtosis', 'skew']
		rows = HeartColumn.options

		for p in rows:
			data.append([
				self.count(p),
				self.mean(p),
				self.std(p),
				self.max(p),
				self.min(p),
				self.kurtosis(p),
				self.skew(p),
			])

		return pd.DataFrame(data, columns = cols, index = rows)
		

	def histogram(self, col = None, **histOptions):
		self.__graph.histogram(col, histOptions=dict(
			save = True,
			output = "histograms/" + self._access(histOptions, 'output', ""),
			transform = self._access(histOptions, 'transform', None),
		))
	
	
