from src.converter import centimeter_to_meter, meter_to_centimeter, foot_to_inch, inch_to_foot
import pytest

def test_centimeter_to_meter():
    assert centimeter_to_meter(100) == 1

def test_meter_to_centimeter():
    assert meter_to_centimeter(1) == 100

def test_foot_to_inch():
    assert foot_to_inch(1) == 12

def test_inch_to_foot():
    assert inch_to_foot(12) == 1

@pytest.mark.skip(reason="We didn't completed millimeter_to_centimeter() function")
def test_millimeter_to_centimeter():
    assert millimeter_to_centimeter(10) == 1


@pytest.mark.xfail(reason="We didn't create any centimeter_to_millimeter() function. So, we're declaring this test as FAIL")
def test_centimeter_to_millimeter():
    assert centimeter_to_millimeter(10) == 1