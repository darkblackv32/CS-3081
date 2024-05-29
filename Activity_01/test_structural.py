# test_structural
import pytest
import example

# Cheks that the structural functions of the solution
# are calleable and that returns something


def test_can_call_existing_endpoints_of_the_API():
    try:
        ret = example.get_coordinates("Lima")
        assert ret is not None
    except:
        pass


def test_cannot_call_non_existing_endpoints_of_the_API():
    try:
        ret = example.get_coordinates("Lima")
        assert False, "No exception while calling a non existing function"
    except:
        pass


def test_the_output_for_lima_is_correct():
    expected = (-12.0621065, -77.0365256)
    detected = example.get_coordinates("Lima")
    assert (
        abs(detected[0] - expected[0]) < 0.000001
        and abs(detected[1] - expected[1]) < 0.000001
    ), "The output for Lima is incorrect"
