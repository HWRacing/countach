types = {
	"uint8": {
		"Name": "uint8",
		"Bits": 8,
		"Signed": False,
		"Encoding": "int"
		},
	"uint16": {
		"Name": "uint16",
		"Bits": 16,
		"Signed": False,
		"Encoding": "int"
		},
	"uint32": {
		"Name": "uint32",
		"Bits": 32,
		"Signed": False,
		"Encoding": "int"
		},
	"int8": {
		"Name": "int8",
		"Bits": 8,
		"Signed": True,
		"Encoding": "int"
		},
	"int16": {
		"Name": "int16",
		"Bits": 16,
		"Signed": True,
		"Encoding": "int"
		},
	"int32": {
		"Name": "int32",
		"Bits": 32,
		"Signed": True,
		"Encoding": "int"
		},
    "boolean": {
		"Name": "boolean",
		"Bits": 8,
		"Signed": False,
		"Encoding": "boolean"
		},
    "single": {
		"Name": "single",
		"Bits": 32,
		"Signed": True,
		"Encoding": "float"
		}
}

output = [
	{
		'Category': 'Characteristic',
		'Name': 'read_1',
		'Long Identifier': '',
		'VCU Type': 'VALUE',
		'Address': 16580608,
		'Record Layout': 'Scalar_FLOAT32_IEEE',
		'Maximum Difference': 0,
		'Type': types['single'],
		'Lower Limit': -3.4e+38,
		'Upper Limit': 3.4e+38
	},
	{
		'Category': 'Measurement',
		'Name': 'write_1',
		'Long Identifier': '',
		'VCU Type': 'FLOAT32_IEEE',
		'Type': types['single'],
		'Resolution': 0, 'Accuracy': 0,
		'Lower Limit': -3.4e+38,
		'Upper Limit': 3.4e+38,
		'Address': 1073774596
	},
	{
		'Category': 'Measurement',
		'Name': 'write_2',
		'Long Identifier': '',
		'VCU Type': 'UBYTE',
		'Type': types['boolean'],
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
		'Type': types['boolean'],
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
		'Type': types['boolean'],
		'Resolution': 0,
		'Accuracy': 0,
		'Lower Limit': 0.0,
		'Upper Limit': 1.0,
		'Address': 1073774593
	}
]