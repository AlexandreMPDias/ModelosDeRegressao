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

	def all(self, transpose = False, rows = None):
		data = []

		cols = ['count', 'mean', 'std', 'max', 'min', 'kurtosis', 'skew']
		rows = HeartColumn.options if rows is None else rows

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

	def getSliceMethod(self, col):
		if(col == HeartColumn.SEX):
			return self.__slice_binary
		elif(col == HeartColumn.AGE):
			return self.__slice_continuous
		elif(col == HeartColumn.EDUCATION):
			return self.__slice_continuous
		elif(col == HeartColumn.CURRENT_SMOKER):
			return self.__slice_binary
		elif(col == HeartColumn.CIGSPER_DAY):
			return self.__slice_continuous
		elif(col == HeartColumn.BPMEDS):
			return self.__slice_binary
		elif(col == HeartColumn.PREVALENT_STROKE):
			return self.__slice_binary
		elif(col == HeartColumn.PREVALENT_HYP):
			return self.__slice_binary
		elif(col == HeartColumn.DIABETES):
			return self.__slice_binary
		elif(col == HeartColumn.TOT_CHOL):
			return self.__slice_continuous
		elif(col == HeartColumn.SYS_BP):
			return self.__slice_continuous
		elif(col == HeartColumn.DIA_BP):
			return self.__slice_continuous
		elif(col == HeartColumn.BMI):
			return self.__slice_continuous
		elif(col == HeartColumn.HEART_RATE):
			return self.__slice_continuous
		elif(col == HeartColumn.GLUCOSE):
			return self.__slice_continuous
		return None

	def slice(self, col):
		method = self.getSliceMethod(col)
		if(method is not None):
			return method(self.__shaper.data, col)
		print(method)
		return []

	def slice_avg(self, col):
		dfs = self.slice(col)
		avgs = [i[col].mean() for i in dfs]
		ys = [i["TenYearCHD"].mean() for i in dfs]
		
		return avgs, ys



	def __slice_continuous(self, data, col):
		dfs = []

		_max = data[col].max()
		_min = data[col].min()
		delta = (_max - _min)/20


		for i in range(0, 20):
			lower_bounded = data[data[col] < (i+1) * delta]
			upper_bounded = lower_bounded[lower_bounded[col] > i * delta]

			dfs.append(upper_bounded)

		return dfs

	def __slice_binary(self, data, col):
		x = data[col]

		x_1 = data[x == 1]
		x_0 = data[x == 0]

		return x_0, x_1
		
	def histogram(self, col = None, **histOptions):
		self.__graph.histogram(col, histOptions=dict(
			save = True,
			output = "output/histograms/" + self._access(histOptions, 'output', ""),
			transform = self._access(histOptions, 'transform', None),
		))
	
	
