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
from src.models.heartDisease.prova.logistic import LogisticReg

class Histogram:
	def __init__(self, data):
		x = data.drop(columns=["TenYearCHD"]).values
		y = data["TenYearCHD"]
		self.__x = sm.add_constant(x)
		self.__y = y

	def y_pred_Logit(self):
		model = sm.Logit(self.__y, self.__x)
		result = model.fit(method='newton')
		y_pred = result.predict(self.__x)
		return y_pred

	def y_pred_Probit(self):
		model = sm.Probit(self.__y,self.__x)
		result = model.fit(method='newton')
		y_pred = result.predict(self.__x)
		return y_pred

	def histogram(self, y_pred, title):
		values = []
		for i in range(0, len(y_pred)):
			delta = self.__y.values[i] - y_pred[i]
			values.append(delta)

		fig = plt.figure()
		plt.title(title)

		plt.style.use('ggplot')
		plt.hist(values, bins = 100, weights=np.ones(len(values)) / len(values))
		plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
		plt.show()