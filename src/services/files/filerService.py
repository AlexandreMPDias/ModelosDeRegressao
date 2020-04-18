import os
import io
import numpy
from src.services.debug import chalk, Log

log = Log()

class ReadService():
	def read_dir(self, path):
		return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

	def read_csv(self, path):
		import pandas as pd
		return numpy.array(pd.read_csv(filePath))

	def read_txt(self, path):
		with open(path, 'r') as f:
			return f.read()

	def read_json(self, path):
		import json
		with open(path, 'r') as f:
			datastore = json.load(f)
			return datastore

class WriteService():
	def write_csv(self, path, content):
		import pandas as pd
		return numpy.array(pd.read_csv(filePath))

	def write_txt(self, path):
		with write(path, 'r') as f:
			return f.read()

	def writeJSON(self, path, content):
		import json
		with open(path, "w") as outjsonfile:
			json.dump(content, outjsonfile)

class FilerServiceHelp():
	def __init__(self):
		self.supported_extensions = ['.txt', '.json', '.csv', '']

	def get_extension(self, path):
		base, ext = os.path.splitext(path)
		if ext not in self.supported_extensions:
			raise KeyError(f"Extension {ext} is not a supported extension")
		return ext


class FilerService:
	def __init__(self):
		self.help = FilerServiceHelp()
		self.readService = ReadService()

	def read(self, path):
		try:
			ext = self.help.get_extension(path)
			if(ext == '.txt'):
				return self.readService.read_txt(path)
			if(ext == '.json'):
				return self.readService.read_json(path)
			if(ext == '.csv'):
				return self.readService.read_csv(path)
			if(ext == ''):
				return self.readService.read_dir(path)
		except FileNotFoundError as fileNotFoundError:
			log.error(f"File: {chalk.lightred(filePath)} was not found")
			log.skip()
			exit(1)
		except Exception as exp:
			raise exp

Filer = FilerService()