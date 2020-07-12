import src.services.files as files
from src.models.heartDisease import heartDisease as hD
import matplotlib.pyplot as plt
from src.models.heartDisease.prova.multiCol import Klass

def histograms():
	hD.describe.histogram(
		hD.continuous,
		output = "percent",
		transform = "percent"
	)


def dispersion():
	for col in hD.options:
		x,y = hD.describe.slice_avg(col)

		if col in hD.continuous:
			hD.draw(x,y,f"Prob [ Y = 1 ] x [ {hD.shaper.langMap[col]} ]", col)
		else:
			out = []
			print(x,y)
			out.append(f"\t\t| Y = 0 | Y = 1")
			out.append(f"{hD.shaper.langMap[col]} = 0 | {1 - y[0]} | {y[0]}")
			out.append(f"{hD.shaper.langMap[col]} = 1 | {1 - y[1]} | {y[1]}")
			print("\n".join(out))
			files.Filer.write(f"histograms/dispersion/{col}.txt", (out))

def corr():
	print(hD.shaper.data.corr())

# corr()


# histograms()
# logistic = LogisticReg(hD.data)
# logistic.Probit()
# logistic.Logit()

# h = Histogram(hD.data)

# h.histogram(h.y_pred_Logit(), "Logit")
# h.histogram(h.y_pred_Logit(), "Logit")
# h.histogram(h.y_pred_Probit(), "Probit")
k = Klass(hD.data)

print("\n" * 10)
k.Probit()
print("\n" * 10)

# # k.Logit()
# print("\n" * 10)


# print(hD.describe.all(rows = ["TenYearCHD"]))