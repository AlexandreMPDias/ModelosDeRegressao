import src.services.files as files
import src.services.debug as debug
from src.models.heartDisease.columns import HeartColumn
from inspect import signature

class DataFrameShaper():
	def __init__(self):
		self.__readFile()
		self.__languageMapping()

	def __readFile(self):
		self.data = files.Filer.read(files.paths.DATA_SET)
		self.data.drop([HeartColumn.EDUCATION], axis=1, inplace = True)
		self.data.rename(columns = dict(male = HeartColumn.SEX), inplace = True)
		self.data.dropna(axis = 0, inplace = True)

	def __languageMapping(self):
		langMap = {}
		langMap[HeartColumn.SEX] = "Sexo"
		langMap[HeartColumn.AGE] = "Idade"
		langMap[HeartColumn.CURRENT_SMOKER] = "Fumante (Atualmente)"
		langMap[HeartColumn.CIGSPER_DAY] = "Cigarros por Dia [un/dia]"
		langMap[HeartColumn.BPMEDS] = "Usa remédios para Pressão Sanguínea"
		langMap[HeartColumn.PREVALENT_STROKE] = "Já teve derrame"
		langMap[HeartColumn.PREVALENT_HYP] = "Hipertenso"
		langMap[HeartColumn.DIABETES] = "Possui diabetes"
		langMap[HeartColumn.TOT_CHOL] = "Nível total de Colesterol no sangue [mg/dL]"
		langMap[HeartColumn.SYS_BP] = "Pressão Sanguínea Sistólica [mmHg]"
		langMap[HeartColumn.DIA_BP] = "Pressão Sanguínea Diastólica [mmHg]"
		langMap[HeartColumn.BMI] = "Índice de Massa Corpórea [kg/m²]"
		langMap[HeartColumn.HEART_RATE] = "Frequência Cardíaca Média [1/min]"
		langMap[HeartColumn.GLUCOSE] = "Nível de Glucose [mg/dl]"

		self.langMap = langMap