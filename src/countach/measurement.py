from dataclasses import dataclass

@dataclass
class Measurement:
    name: str
    longIdentifier: str
    vcuType: str
    address: int
    recordLayout: str
    maxDifference: int
    dataType: str
    lowerLimit: float
    upperLimit: float
