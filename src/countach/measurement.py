from dataclasses import dataclass

@dataclass
class Measurement:
	name: str
	longIdentifier: str
	vcuType: str
	dataType: str
	resolution: int
	accuracy: int
	lowerLimit: float
	upperLimit: float
	address: int

def measurementFromDict(d):
	return Measurement(
		d["name"],
		d["longIdentifier"],
    	d["vcuType"],
		d["dataType"],
		d["resolution"],
		d["accuracy"],
		d["lowerLimit"],
		d["upperLimit"],
		d["address"]
	)
