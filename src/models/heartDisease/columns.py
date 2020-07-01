class _Column:
	SEX = "sex"
	AGE = "age"
	EDUCATION = "education"
	CURRENT_SMOKER = "currentSmoker"
	CIGSPER_DAY = "cigsPerDay"
	BPMEDS = "BPMeds"
	PREVALENT_STROKE = "prevalentStroke"
	PREVALENT_HYP = "prevalentHyp"
	DIABETES = "diabetes"
	TOT_CHOL = "totChol"
	SYS_BP = "sysBP"
	DIA_BP = "diaBP"
	BMI = "BMI"
	HEART_RATE = "heartRate"
	GLUCOSE = "glucose"

class HeartColumn(_Column):
	options = [
		_Column.SEX,
		_Column.AGE,
		_Column.CURRENT_SMOKER,
		_Column.CIGSPER_DAY,
		_Column.BPMEDS,
		_Column.PREVALENT_STROKE,
		_Column.PREVALENT_HYP,
		_Column.DIABETES,
		_Column.TOT_CHOL,
		_Column.SYS_BP,
		_Column.DIA_BP,
		_Column.BMI,
		_Column.HEART_RATE,
		_Column.GLUCOSE 
	]

	continuous = [
		_Column.AGE,
		_Column.CIGSPER_DAY,
		_Column.TOT_CHOL,
		_Column.SYS_BP,
		_Column.DIA_BP,
		_Column.BMI,
		_Column.HEART_RATE,
		_Column.GLUCOSE 
	]

	