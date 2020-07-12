import pandas as pd
import numpy as np
import statsmodels.api as sm
import scipy.stats as st
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
from sklearn.metrics import confusion_matrix
import matplotlib.mlab as mlab
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from src.models.heartDisease.logistic import LogisticReg

class Klass:
	def __init__(self, data):
		x = self.prepare_x(data)
		y = data["TenYearCHD"]
		self.split_x(data)
		self.__x = sm.add_constant(x.values)
		self.__y = y

	def prepare_x(self, data):
		x = data.drop(columns=["TenYearCHD"])
		x = x.iloc[:, [0,1, 3, 8, 11, 13]]
		totalCols = 0
		for i in range(0,len(x.columns)):
			for j in range(0,len(x.columns)):
				if i < j:
					totalCols = totalCols + 1
		currIter = 0
		for i in range(0,len(x.columns)):
			for j in range(0,len(x.columns)):
				if i < j:
					currIter = currIter + 1
					print(f"Iter: {currIter}/{totalCols}")
					x = self.multiply_columns(x, i, j)
		return x

	def split_x(self, data):
		x_1 = data[data.iloc[:, 0] == 1]
		x_0 = data[data.iloc[:, 0] == 0]

		print(x_0)

		print(x_1["TenYearCHD"].mean())
		print(x_0["TenYearCHD"].mean())

		return x_1, x_0

	def multiply_columns(self, data, col1, col2):
		c1 = data.iloc[:, col1].values
		c2 = data.iloc[:, col2].values
		m = []

		for i in range(0, min(len(c1), len(c2))):
			m.append(c1[i] * c2[i])

		data[f"{col1}_x_{col2}"] = m
		return data

	def Logit(self):
		model = sm.Logit(self.__y,self.__x)
		result = model.fit(method = 'newton')
		print(result.summary())

	def Probit(self):
		model = sm.Probit(self.__y,self.__x)
		result = model.fit(method = 'newton')
		print(result.summary())