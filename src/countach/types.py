from countach import fixed # Broken import

# Given a type string from an A2L file, returns a dictionary describing the type
def getTypeDict(typeName):
	if "uint8" in typeName:
		result = {
			"Name": "uint8",
			"Bits": 8,
			"Signed": False,
			"Encoding": "int"
		}
	elif "uint16" in typeName:
		result = {
			"Name": "uint16",
			"Bits": 16,
			"Signed": False,
			"Encoding": "int"
		}
	elif "uint32" in typeName:
		result = {
			"Name": "uint32",
			"Bits": 32,
			"Signed": False,
			"Encoding": "int"
		}
	elif "int8" in typeName:
		result = {
			"Name": "int8",
			"Bits": 8,
			"Signed": True,
			"Encoding": "int"
		}
	elif "int16" in typeName:
		result = {
			"Name": "int16",
			"Bits": 16,
			"Signed": True,
			"Encoding": "int"
		}
	elif "int32" in typeName:
		result = {
			"Name": "int32",
			"Bits": 32,
			"Signed": True,
			"Encoding": "int"
		}
	elif "boolean" in typeName:
		result = {
			"Name": "boolean",
			"Bits": 8,
			"Signed": False,
			"Encoding": "boolean"
		}
	elif "single" in typeName:
		result = {
			"Name": "single",
			"Bits": 32,
			"Signed": True,
			"Encoding": "float"
		}
	elif "fix" in typeName:
		result = fixed.getFixedDict(typeName)
	else:
		raise ValueError(f"No valid type found in {typeName}")
	
	return result
