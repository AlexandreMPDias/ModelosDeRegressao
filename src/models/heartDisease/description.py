from src.models.heartDisease.shaper import DataFrameShaper
from src.models.heartDisease.graph import DataFrameGraph
from src.models.heartDisease.columns import HeartColumn

class Description:
	def __init__(self, shaper: DataFrameShaper, graph: DataFrameGraph):
		self.__graph = graph
		self.__describe = shaper.data.describe()

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

	def histogram(self, col = None):
		self.__graph.histogram(col, histOptions=dict(
			save = True,
			output = "histograms",
		))
	
	
