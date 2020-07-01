import src.services.files as files
from src.models.heartDisease import heartDisease as hD
import matplotlib.pyplot as plt

def histograms():
	hD.describe.histogram(
		hD.continuous,
		output = "percent",
		transform = "percent"
	)

histograms()

print(hD.describe.all())
