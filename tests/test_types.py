import src.countach.types as t
import testdata.output as data


def test_getTypeDict_uint8():
	assert t.getTypeDict("VCU_CM_uint8") == data.types["uint8"]

def test_getTypeDict_uint16():
	assert t.getTypeDict("VCU_CM_uint16") == data.types["uint16"]

def test_getTypeDict_uint32():
	assert t.getTypeDict("VCU_CM_uint32") == data.types["uint32"]

def test_getTypeDict_int8():
	assert t.getTypeDict("VCU_CM_int8") == data.types["int8"]

def test_getTypeDict_int16():
	assert t.getTypeDict("VCU_CM_int16") == data.types["int16"]

def test_getTypeDict_int32():
	assert t.getTypeDict("VCU_CM_int32") == data.types["int32"]

def test_getTypeDict_single():
	assert t.getTypeDict("VCU_CM_single") == data.types["single"]

def test_getTypeDict_boolean():
	assert t.getTypeDict("VCU_CM_boolean") == data.types["boolean"]

def test_getTypeDict_fixed():
	assert t.getTypeDict("VCU_CM_sfix16_E5_B1") == {
		"Name": "fixdt",
		"Signed": True,
		"Bits": 16,
		"Total Slope": 32,
		"Bias": 1
	}
