import src.services.files as files
import src.services.debug as debug
from src.models.heartDisease.shaper import DataFrameShaper
from src.models.heartDisease.graph import DataFrameGraph
from src.models.heartDisease.columns import HeartColumn
from src.models.heartDisease.description import Description



from src.services.graph import Histogram

class HeartDiseaseModel(HeartColumn):
	def __init__(self):
		self.shaper = DataFrameShaper()
		self.data = self.shaper.data
		self.__graph = DataFrameGraph(self.shaper)
		self.describe = Description(self.shaper, self.__graph)

	def histogram(self, features = None):
		self.__graph.histogram(features, multi=True)

heartDisease = HeartDiseaseModel()