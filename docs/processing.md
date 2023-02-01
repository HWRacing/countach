# Processing

This file contains all actual processing that happens with the data. Please note that almost all of these functions are for internal use only.

## `linesToSections(lines)`

Takes an array of lines from a `.a2l` file and returns an array containing arrays. Each inner array represents a `MEASUREMENT` or `CHARACTERISTIC` block, and contains the lines that make up that block (including the `/begin` and `/end` lines).

## `convertMSection(sectionLines)`

Takes an array of lines making up a `MEASUREMENT` section and returns the data in dictionary format.

## `convertCSection(sectionLines)`

Takes an array of lines making up a `CHARACTERISTIC` section and returns the data in dictionary format.

## `convertSection(sectionLines)`

Takes an array of lines making up a section (either `MEASUREMENT` or `CHARACTERISTIC`) and returns the data in a dictionary format.

## `extractData(file)`

Takes a file name and returns the data from all the sections as dictionaries in an array.

