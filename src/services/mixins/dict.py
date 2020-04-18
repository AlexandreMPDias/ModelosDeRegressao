class DictClass:
	def __getitem__(self, name):
		return getattr(self, name)

	def __setitem__(self, name, value):
		return setattr(self, name, value)

	def __delitem__(self, name):
		return delattr(self, name)

	def __contains__(self, name):
		return hasattr(self, name)


class Serializable(DictClass):
	def __init__(self):
		self.name = ""
		self.__serial = ""

	def __serialize_key(self, key, value):
		if value:
			if value is True:
				return key
			return f"{key}:{value}"
		return ''

	def serialize(self, __dict):
		srt_key = []

		str_key = [self.__serialize_key(key, __dict[key]) for key in __dict if __dict[key]]
		self.__serial = "/".join([self.name] + str_key)

		return self.getSerial()

	def getSerial(self):
		return self.__serial