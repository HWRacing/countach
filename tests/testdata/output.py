from countach import measurement, characteristic

def dictToCharac(n):
	output = characteristic.Characteristic()
	output.name = n["Name"]
	output.longIdentifier = n["Long Identifier"]
	output.vcuType = n["VCU Type"]
	output.address = n["Address"]
	output.recordLayout = n["Record Layout"]
	output.maxDifference = n["Maximum Difference"]
	output.dataType = n["Type"]
	output.lowerLimit = n["Lower Limit"]
	output.upperLimit = n["Upper Limit"]
	return output

def dictToMeas(n):
	output = measurement.Measurement
	output.name = n["Name"]
	output.longIdentifier = n["Long Identifier"]
	output.vcuType = n["VCU Type"]
	output.dataType = n["Type"]
	output.resolution = n["Resolution"]
	output.accuracy = n["Accuracy"]
	output.lowerLimit = n["Lower Limit"]
	output.upperLimit = n["Upper Limit"]
	output.address = n["Address"]
	return output

def dictToClass(dictVersion):
	if dictVersion["Category"] == "Characteristic":
		return dictToCharac(dictVersion)
	elif dictVersion["Category"] == "Measurement":
		return dictToMeas(dictVersion)
	else:
		raise ValueError("Invalid dictionary")

outputDicts = [
	{
		'Category': 'Characteristic',
		'Name': 'read_1',
		'Long Identifier': '',
		'VCU Type': 'VALUE',
		'Address': 16580608,
		'Record Layout': 'Scalar_FLOAT32_IEEE',
		'Maximum Difference': 0,
		'Type': 'single',
		'Lower Limit': -3.4e+38,
		'Upper Limit': 3.4e+38
	},
	{
		'Category': 'Measurement',
		'Name': 'write_1',
		'Long Identifier': '',
		'VCU Type': 'FLOAT32_IEEE',
		'Type': 'single',
		'Resolution': 0, 
		'Accuracy': 0,
		'Lower Limit': -3.4e+38,
		'Upper Limit': 3.4e+38,
		'Address': 1073774596
	},
	{
		'Category': 'Measurement',
		'Name': 'write_2',
		'Long Identifier': '',
		'VCU Type': 'UBYTE',
		'Type': 'boolean',
		'Resolution': 0,
		'Accuracy': 0,
		'Lower Limit': 0.0,
		'Upper Limit': 1.0,
		'Address': 1073774600
	}, 
	{
		'Category': 'Measurement',
		'Name': 'PwrM_flgKeyOnDelay',
		'Long Identifier': '',
		'VCU Type': 'UBYTE',
		'Type': 'boolean',
		'Resolution': 0,
		'Accuracy': 0,
		'Lower Limit': 0.0,
		'Upper Limit': 1.0,
		'Address': 1073774592
	},
	{
		'Category': 'Measurement',
		'Name': 'PwrM_flgKeyOnRaw',
		'Long Identifier': '',
		'VCU Type': 'UBYTE',
		'Type':'boolean',
		'Resolution': 0,
		'Accuracy': 0,
		'Lower Limit': 0.0,
		'Upper Limit': 1.0,
		'Address': 1073774593
	}
]

output = []
for i in outputDicts:
	output.append(dictToClass(i))
