from countach import measurement, characteristic, memorySegment, addressMapping

def dictToClass(dictVersion):
	if dictVersion["Category"] == "Characteristic":
		return characteristic.characteristicFromDict(dictVersion)
	elif dictVersion["Category"] == "Measurement":
		return measurement.measurementFromDict(dictVersion)
	elif dictVersion["Category"] == "Memory Segment":
		return memorySegment.memorySegmentFromDict(dictVersion)
	else:
		raise ValueError("Invalid dictionary")

mapping = addressMapping.AddressMapping(0x00FD0000, 0x40000000, 0x00008000)

outputDicts = [
	{
		'Category': "Memory Segment",
		'name': '_RAMCAL',
		'longIdentifier': 'calibration_ram',
		'programType': 'DATA',
		'memoryType': 'RAM',
		'attribute': 'INTERN',
		'address': 0x40000000,
		'size': 0x00008000,
		'offset': (-1, -1, -1, -1, -1)
	},
	{
		'Category': "Memory Segment",
		'name': '_ROMCAL',
		'longIdentifier': 'calibration_rom',
		'programType': 'DATA',
		'memoryType': 'FLASH',
		'attribute': 'INTERN',
		'address': 0x00FD0000,
		'size': 0x00008000,
		'offset': (-1, -1, -1, -1, -1),
		'mapping': mapping
	},
	{
		'Category': "Memory Segment",
		'name': '_RAMMSR',
		'longIdentifier': 'measurement_ram',
		'programType': 'DATA',
		'memoryType': 'RAM',
		'attribute': 'INTERN',
		'address': 0x40000000,
		'size': 0x00060000,
		'offset': (-1, -1, -1, -1, -1)
	},
	{
		'Category': "Memory Segment",
		'name': '_CODE',
		'longIdentifier': 'ecu_code',
		'programType': 'CODE',
		'memoryType': 'FLASH',
		'attribute': 'INTERN',
		'address': 0x01000008,
		'size': 0x1FE000,
		'offset': (-1, -1, -1, -1, -1)
	},
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
