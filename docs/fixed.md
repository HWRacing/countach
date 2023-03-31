# Fixed-Point Data

The VCU can handle a number of fixed-point data types. In the A2L file, they are defined using a string looking like this: `sfix16_E5_B1`. Such a string is made up of the following components:

- Signed (`s` or `u`): Whether or not the value is signed
- Type identifier (`fix`: Signifies that this is a fixed-point data type
- Word length (e.g. `16`): The number of bits taken up by this type
- Total Slope (e.g. `S3` or `E5`): Slope of the scaling, specified as a scalar. This can either be in two forms:
  - Standard, signified by an `S`, where the total slope is the number that comes after the `S`
  - Exponential, signified by an `E`, where the total slope is two to the power of the number after the `E`
- Bias (e.g. `B3`): Bias of the scaling

For more information on fixed-point data types used by Matlab, see [this link](https://www.mathworks.com/help/simulink/slref/simulink.numerictype.fixdt.html).
