import src.countach.fixed as fx

def test_extractInitialInt():
    assert fx._extractInitialInt("16_S3_B1") == 16

def test_checkIfFixedIsSigned_signedCase():
	assert fx._checkIfFixedIsSigned("sfix15") == True
        
def test_checkIfFixedIsSigned_unSignedCase():
	assert fx._checkIfFixedIsSigned("ufix15") == False

def test_getWordLength():
	assert fx._getWordLength("sfix16_E20_B1") == 16#

# The case when the slope isn't explicitly specified
def test_getTotalSLope_unspec():
	assert fx._getTotalSlope("sfix15") == 1

# The case when the slope is explicitly specified
def test_getTotalSlope_explicit():
	assert fx._getTotalSlope("sfix16_S3_B1") == 3

# The case when the slope is specified as a power of 2
def test_getTotalSlope_exponent():
	assert fx._getTotalSlope("sfix16_E8_B1") == 256

# The case when the bias isn't explicitly specified
def test_getBias_unspec():
	assert fx._getBias("sfix16_S3") == 0

# The case when the bias is explicitly specified
def test_getBias_unspec():
	assert fx._getBias("sfix16_E4_B1") == 1

def test_getFixedTypeParameters():
	assert fx._getFixedTypeParameters("sfix16_E4_B1") == (True, 16, 16, 1)

def test_decodeA2LFixed():
	assert fx.decodeA2LFixed("sfix16_E5_B1") == "sf16S32B1"
