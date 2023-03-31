# Measurement

A measurement is a value inside the VCU that can be written to by the computer and read by the VCU (e.g. a calibration value). A measurement is represented by a Measurement object, which has the following properties:

- `name: str`: The name of the measurement
- `longIdentifier: str`: Unknown, has always been blank so far
- `vcuType: str`: A type value used by the VCU. Not overly useful.
- `dataType: str`: The [type](types.md) of the data in the measurement
- `resolution: int`: Always left at 0, unused by the VCU
- `accuracy: int`: Always left at 0, unused by the VCU
- `lowerLimit: float`: The lower limit for the data
- `upperLimit: float`: The lower limit for the data
- `address: int`: The address of the measurement
