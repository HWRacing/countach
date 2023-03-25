from countach import measurement, characteristic

def dictToClass(dictVersion):
	if dictVersion["Category"] == "Characteristic":
		return characteristic.characteristicFromDict(dictVersion)
	elif dictVersion["Category"] == "Measurement":
		return measurement.measurementFromDict(dictVersion)
	else:
		raise ValueError("Invalid dictionary")

outputDicts = [
	{
		'Category': "Characteristic",
		'name': 'read_1',
		'longIdentifier': '',
		'vcuType': 'VALUE',
		'address': 16580608,
		'recordLayout': 'Scalar_FLOAT32_IEEE',
		'maxDifference': 0,
		'dataType': 'single',
		'lowerLimit': -3.4e+38,
		'upperLimit': 3.4e+38
	},
	{
		'Category': "Measurement",
		'name': 'write_1',
		'longIdentifier': '',
		'vcuType': 'FLOAT32_IEEE',
		'dataType': 'single',
		'resolution': 0, 
		'accuracy': 0,
		'lowerLimit': -3.4e+38,
		'upperLimit': 3.4e+38,
		'address': 1073774596
	},
	{
		'Category': "Measurement",
		'name': 'write_2',
		'longIdentifier': '',
		'vcuType': 'UBYTE',
		'dataType': 'boolean',
		'resolution': 0,
		'accuracy': 0,
		'lowerLimit': 0.0,
		'upperLimit': 1.0,
		'address': 1073774600
	}, 
	{
		'Category': "Measurement",
		'name': 'PwrM_flgKeyOnDelay',
		'longIdentifier': '',
		'vcuType': 'UBYTE',
		'dataType': 'boolean',
		'resolution': 0,
		'accuracy': 0,
		'lowerLimit': 0.0,
		'upperLimit': 1.0,
		'address': 1073774592
	},
	{
		'Category': "Measurement",
		'name': 'PwrM_flgKeyOnRaw',
		'longIdentifier': '',
		'vcuType': 'UBYTE',
		'dataType':'boolean',
		'resolution': 0,
		'accuracy': 0,
		'lowerLimit': 0.0,
		'upperLimit': 1.0,
		'address': 1073774593
	}
]

output = []
for i in outputDicts:
	output.append(dictToClass(i))
