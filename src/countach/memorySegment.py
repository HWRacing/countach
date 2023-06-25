from dataclasses import dataclass
from typing import Tuple
from countach import addressMapping

@dataclass
class MemorySegment:
	name: str
	longIdentifier: str
	programType: str
	memoryType: str
	attribute: str
	address: int
	size: int
	offset: Tuple[int, int, int, int, int]
	mapping: addressMapping.AddressMapping

def memorySegmentFromDict(d) -> MemorySegment:
	return MemorySegment(
		d["name"],
		d["longIdentifier"],
		d["programType"],
		d["memoryType"],
		d["attrinute"],
		d["address"],
		d["size"],
		d["offset"],
		d["mapping"]
	)