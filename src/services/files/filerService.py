import os
import io
import numpy as np
from src.services.debug import chalk, Log, Status

class WithLog():
	def __init__(self, __log):
		self.__log = __log

class ReadService(WithLog):

	def read_dir(self, path):
		return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

	def read_csv(self, path):
		import pandas as pd
		return pd.read_csv(path)

	def read_txt(self, path):
		with open(path, 'r') as f:
			return f.read()

	def read_json(self, path):
		import json
		with open(path, 'r') as f:
			datastore = json.load(f)
			return datastore

class WriteService(WithLog):
	def write_json(self, path, content):
		import json
		with open(path, "w") as outjsonfile:
			json.dump(content, outjsonfile, indent=4)

class FilerServiceHelp():
	def __init__(self, __log):
		self.__log = __log
		self.supported_extensions = ['.txt', '.json', '.csv', '']

	def get_extension(self, path):
		base, ext = os.path.splitext(path)
		if ext not in self.supported_extensions:
			raise KeyError(f"Extension {ext} is not a supported extension")
		return ext


class FilerService:
	def __init__(self, debug_level = 0):
		self.__log = Log(debug_level)
		self.__help = FilerServiceHelp(self.__log)
		self.__readService = ReadService(self.__log)
		self.__writeService = WriteService(self.__log)

	def read(self, path):
		try:
			ext = self.__help.get_extension(path)
			pretty_path = path[2:]

			self.__log.info(f"read {chalk.lightred(pretty_path)}")
			content = None
			if(ext == '.txt'):
				content = self.__readService.read_txt(path)
			elif(ext == '.json'):
				content = self.__readService.read_json(path)
			elif(ext == '.csv'):
				content = self.__readService.read_csv(path)
			elif(ext == ''):
				content = self.__readService.read_dir(path)

			self.__log.success(f"read {chalk.lightred(pretty_path)}")
			return content
		except FileNotFoundError as fileNotFoundError:
			self.__log.error(f"File: {chalk.lightred(pretty_path)} was not found")
			self.__log.skip()
			raise
		except Exception as exp:
			raise exp

	def write(self, path, content):
		try:
			ext = self.__help.get_extension(path)
			pretty_path = path[2:]

			self.__log.info(f"write {chalk.lightred(pretty_path)}")
			if(ext == '.json'):
				self.__writeService.write_json(path,content)
			self.__log.success(f"write {chalk.lightred(pretty_path)}")
			return content

		except Exception as exp:
			raise exp

Filer = FilerService()