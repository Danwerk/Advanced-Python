"""
Tests that checks conversing from WGS84 to L-Est97 coordinate system and vice versa.

Author: Danyil Kurbatov
"""
from coordinates.main import convert_est_to_wgs, convert_wgs_to_est
# from package_danyil.converter import convert_est_to_wgs, convert_wgs_to_est


# Test converting from wgs to est coordinate system
def test_wgs_to_est_conversion_1():
    """Test 1 to check the result is correct from wgs to est conversion system."""
    x, y = convert_wgs_to_est(59.395312, 24.664182)
    expected_x = 6584338.65
    expected_y = 537735.47

    assert round(x, 1) == round(expected_x, 1)
    assert round(y, 1) == round(expected_y, 1)


def test_wgs_to_est_conversion_2():
    """Test 2 to check the result is correct from wgs to est conversion system."""
    x, y = convert_wgs_to_est(59.421676, 24.7939)
    expected_x = 6587355.63
    expected_y = 545070.33

    assert round(x, 1) == round(expected_x, 1)
    assert round(y, 1) == round(expected_y, 1)


def test_wgs_to_est_conversion_3():
    """Test 3 to check the result is correct from wgs to est conversion system."""
    x, y = convert_wgs_to_est(57.829198, 27.033468)
    expected_x = 6413786.09
    expected_y = 680176.52

    assert round(x, 1) == round(expected_x, 1)
    assert round(y, 1) == round(expected_y, 1)


# Test converting from est to wgs coordinate system
def test_est_to_wgs_conversion_1():
    """Test 1 to check the result is correct from est to wgs conversion system."""
    x, y = convert_est_to_wgs(6584338.65, 537735.47)
    expected_x = 59.395312
    expected_y = 24.664182

    assert round(x, 4) == round(expected_x, 4)
    assert round(y, 4) == round(expected_y, 4)


def test_est_to_wgs_conversion_2():
    """Test 2 to check the result is correct from est to wgs conversion system."""
    x, y = convert_est_to_wgs(6587355.63, 545070.33)
    expected_x = 59.421676
    expected_y = 24.7939

    assert round(x, 4) == round(expected_x, 4)
    assert round(y, 4) == round(expected_y, 4)


def test_est_to_wgs_conversion_3():
    """Test 3 to check the result is correct from est to wgs conversion system."""
    x, y = convert_est_to_wgs(6413786.09, 680176.52)
    expected_x = 57.829198
    expected_y = 27.033468

    assert round(x, 4) == round(expected_x, 4)
    assert round(y, 4) == round(expected_y, 4)
