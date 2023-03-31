# Characteristic

A characteristic is a value inside the VCU that can be read by the computer (e.g. throttle position). A characteristic is represented by a Characteristic object, which has the following properties:

- `name: str`: The name of the characteristic
- `longIdentifier: str`: Unknown, has always been blank so far
- `vcuType: str`: A type value used by the VCU. Not overly useful.
- `address: int`: The address of the characteristic
- `recordLayout: str`: A value used by the VCU.
- `maxDifference: int`: Unknown
- `dataType: str`:  The [type](types.md) of the data given by the characteristic
- `lowerLimit: float`: The lower limit for the data
- `upperLimit: float`: The lower limit for the data
