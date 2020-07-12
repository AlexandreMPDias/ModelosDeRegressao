import numpy as np
import statsmodels.api as sm

class LogisticReg:
	def __init__(self, data):
		x = data.drop(columns=["TenYearCHD"]).values
		y = data["TenYearCHD"]
		self.__x = sm.add_constant(x)
		self.__y = y

	def Logit(self):
		model = sm.Logit(self.__y,self.__x)
		result = model.fit(method = 'newton')
		print(result.summary())

	def Probit(self):
		model = sm.Probit(self.__y,self.__x)
		result = model.fit(method = 'newton')
		print(result.summary())




