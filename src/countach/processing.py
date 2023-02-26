from .fileops import _importFile
from .types import getTypeFromRawString

# Take the whole a2l file and extract the lines containing measurement or characteristic sections
def _linesToSections(lines):
	# Whether or not the current line is inside a section
	inSection = False
	output = []
	currentOutput = []
	for rawline in lines:
		# Remove leading and trailing whitespace
		line = rawline.lstrip()[:-1]

		if line == "/begin CHARACTERISTIC" or line == "/begin MEASUREMENT":
			inSection = True
		elif line == "/end CHARACTERISTIC" or line == "/end MEASUREMENT":
			inSection = False
			currentOutput.append(line)
			output.append(currentOutput)
			currentOutput = []
		
		if inSection:
			currentOutput.append(line)

	return output

def _convertMSection(sectionLines):
	output = {"Category": "Measurement"}
	for rawline in sectionLines:
		line = rawline.split()

		if line[1] == "Name":
			output['Name'] = line[3]
		elif line[1] == "Long":
			if line[4] == '""':
				output["Long Identifier"] = ""
			else:	
				output["Long Identifier"] = line[4]
		elif line[1] == "Data":
			output["VCU Type"] = line[4]
		elif line[1] == "Conversion":
			output["Type"] = getTypeFromRawString(line[4])
		elif line[1] == "Resolution":
			output["Resolution"] = int(line[5])
		elif line[1] == "Accuracy":
			output["Accuracy"] = int(line[5])
		elif line[1] == "Lower":
			output["Lower Limit"] = float(line[4])
		elif line[1] == "Upper":
			output["Upper Limit"] = float(line[4])
		elif line[0] == "ECU_ADDRESS":
			output["Address"] = int(line[1], 16)
	
	return output

def _convertCSection(sectionLines):
	output = {"Category": "Characteristic"}
	for rawline in sectionLines:
		line = rawline.split()

		if line[1] == "Name":
			output['Name'] = line[3]
		elif line[1] == "Long":
			if line[4] == '""':
				output["Long Identifier"] = ""
			else:	
				output["Long Identifier"] = line[4]
		elif line[1] == "Type":
			output["VCU Type"] = line[3]
		elif line[1] == "ECU":
			output["Address"] = int(line[4], 16)
		elif line[1] == "Record":
			output["Record Layout"] = line[4]
		elif line[1] == "Maximum":
			output["Maximum Difference"] = int(line[4])
		elif line[1] == "Conversion":
			output["Type"] = getTypeFromRawString(line[4])
		elif line[1] == "Lower":
			output["Lower Limit"] = float(line[4])
		elif line[1] == "Upper":
			output["Upper Limit"] = float(line[4])
	
	return output

def _convertSection(sectionLines):
	sectionType = sectionLines[0].split()[1]
	output = {}
	if sectionType == "CHARACTERISTIC":
		output = _convertCSection(sectionLines)
	elif sectionType == "MEASUREMENT":
		output = _convertMSection(sectionLines)
	else:
		raise RuntimeError("convertSecion only accepts CHARACTERISTIC or MEASUREMENT sections")
	
	return output

def extractData(file):
	lines = _importFile(file)
	sections = _linesToSections(lines)
	output = []
	for section in sections:
		output.append(_convertSection(section))
	return output
