from countach import characteristic, measurement, types

def _parseLongID(rawText):
	if rawText == '""':
		return ""
	else:
		return rawText

# Parse a CHARACTERISTIC section
def parseCSection(section):
	current = characteristic.Characteristic()

	for rawLine in section:
		line = rawLine.split()
		if line[1] == "Name":
			current.name = line[3]
		elif line[1] == "Long":
			current.longIdentifier = _parseLongID(line[4])
		elif line[1] == "Type":
			current.vcuType = line[3]
		elif line[1] == "ECU":
			current.address = int(line[4], 16)
		elif line[1] == "Record":
			current.recordLayout = line[4]
		elif line[1] == "Maximum":
			current.maxDifference = int(line[4])
		elif line[1] == "Conversion":
			current.dataType = types.getTypeFromRawString(line[4])
		elif line[1] == "Lower":
			current.lowerLimit = float(line[4])
		elif line[1] == "Upper":
			current.upperLimit = float(line[4])
	
	return current

# Parse a MEASUREMENT section
def parseMSection(section):
	current = measurement.Measurement()

	for rawLine in section:
		line = rawLine.split()
		if line[1] == "Name":
			current.name = line[3]
		elif line[1] == "Long":
			current.longIdentifier = _parseLongID(line[4])
		elif line[1] == "Data":
			current.vcuType = line[4]
		elif line[1] == "Conversion":
			current.dataType = types.getTypeFromRawString(line[4])
		elif line[1] == "Resolution":
			current.resolution = int(line[5])
		elif line[1] == "Accuracy":
			current.accuracy = int(line[5])
		elif line[1] == "Lower":
			current.lowerLimit = float(line[4])
		elif line[1] == "Upper":
			current.upperLimit = float(line[4])
		elif line[0] == "ECU_ADDRESS":
			current.address = int(line[1], 16)
