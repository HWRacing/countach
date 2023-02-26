def _importFile(fileName):
	with open(fileName, "r") as f:
		lines = f.readlines()
	return lines
