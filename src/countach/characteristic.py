from dataclasses import dataclass

@dataclass
class Characteristic:
	name: str
	longIdentifier: str
	vcuType: str
	dataType: str
	resolution: int
	accuracy: int
	lowerLimit: float
	upperLimit: float
	address: int
