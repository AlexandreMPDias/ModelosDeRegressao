import src.services.files as files
import src.services.debug as debug

class HeartDiseaseModel():
	def __init__(self):
		self.data = files.Filer.read(files.paths.DATA_SET)

heartDisease = HeartDiseaseModel()