from .processing import *

def getTypeFromRawString(rawString):
	typeList = [
	"uint8", 
	"uint16", 
	"uint32", 
	"int8", 
	"int16", 
	"int32", 
	"single",
	"boolean"]

	# Check if the type is a common one
	for typeString in typeList:
		if typeString in rawString:
			return typeString
	
	# Handle fixed types
	if "fix" in rawString:
		raise NotImplementedError("Cannot handle fixed-point data types yet")
