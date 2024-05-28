#test_structural
import pytest
import example

# Cheks that the structural functions of the solution
# are calleable and that returns something

def test_can_call_existing_endpoints_of_the_API():
    try:
        ret = example.get_coordinates("Lima, Peru")
        assert (ret is not None)
    except:
        assert False, "Expection while calling an existing function"

def test_cannot_call_non_existing_endpoints_of_the_API():
    try:
        ret = example.get_coordinates("blah blah")
        assert False, "Expection not raised"
    except:
        pass