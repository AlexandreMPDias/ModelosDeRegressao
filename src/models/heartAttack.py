import src.services.files as files
import src.services.debug as debug

class DataFrameShaper():
	def __init__(self):
		self.__readFile()
		self.__dropUnecessaryColumns()
		self.__dropNA() 
		self.__balanceTenYearCHD()

	def __readFile(self):
		self.data = files.Filer.read(files.paths.DATA_SET)

	def __dropUnecessaryColumns(self):
		self.data = self.data.drop(columns = [
			'male',
			'age',
			'education',
			'currentSmoker',
			'cigsPerDay',
			'BPMeds',
			'prevalentStroke',
			'prevalentHyp',
			'diabetes',
			'totChol',
			'sysBP',
			'diaBP',
			'BMI',
			'heartRate',
			'glucose',
		])

	def __dropNA(self):
		self.data = self.data.dropna()

	def __getBalanceRatio(self):
		up_count = 0
		down_count = 0
		for entry in self.data['TenYearCHD']:
			if entry is 1:
				up_count = up_count + 1
			else:
				down_count = down_count + 1

		return min(up_count, down_count)

	def __balanceTenYearCHD(self):
		minCount = self.__getBalanceRatio()

		up_count = 0
		down_count = 0
		indexToRemove = []

		for i in range(0,len(self.data.index)):
			entry = self.data['TenYearCHD'][i]

			if entry == 1:
				up_count = up_count + 1
				if up_count >= minCount:
					indexToRemove.append(i)
			else:
				down_count = down_count + 1
				if down_count >= minCount:
					indexToRemove.append(i)

		self.data = self.data.drop(indexToRemove)

class HeartDiseaseModel():
	def __init__(self):
		shaper = DataFrameShaper()
		self.data = shaper.data

heartDisease = HeartDiseaseModel()