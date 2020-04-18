import os
import io
import numpy
from src.services.debug import chalk, Log, Status

log = Log()

class WithLog():
	def __init__(self, log):
		self.log = log

class ReadService(WithLog):

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
	def __init__(self, log):
		self.log = log
		self.supported_extensions = ['.txt', '.json', '.csv', '']

	def get_extension(self, path):
		base, ext = os.path.splitext(path)
		if ext not in self.supported_extensions:
			raise KeyError(f"Extension {ext} is not a supported extension")
		return ext


class FilerService:
	def __init__(self, debug_level = 0):
		self.log = Log(debug_level)
		self.help = FilerServiceHelp(self.log)
		self.readService = ReadService(self.log)

	def read(self, path):
		try:
			ext = self.help.get_extension(path)
			pretty_path = path[2:]

			log.info(f"read {chalk.lightred(pretty_path)}")
			content = None
			if(ext == '.txt'):
				content = self.readService.read_txt(path)
			elif(ext == '.json'):
				content = self.readService.read_json(path)
			elif(ext == '.csv'):
				content = self.readService.read_csv(path)
			elif(ext == ''):
				content = self.readService.read_dir(path)

			log.success(f"read {chalk.lightred(pretty_path)}")
			return content
		except FileNotFoundError as fileNotFoundError:
			log.error(f"File: {chalk.lightred(pretty_path)} was not found")
			log.skip()
			exit(1)
		except Exception as exp:
			raise exp

Filer = FilerService()