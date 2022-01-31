import sys, pytest
sys.path.append('../')

from src.closed_interval import ClosedInterval

@pytest.fixture
def closed_interval():
    closed_interval = ClosedInterval(lower=1, upper=3)
    return closed_interval

def test_init_lower(closed_interval):
    lower = closed_interval.lower
    assert 1 == lower
    
def test_init_upper(closed_interval):
    upper = closed_interval.upper
    assert 3 == upper
    
def test_get_range_string(closed_interval):
    assert "[1,3]" == closed_interval.get_range_string()

def test_init_condition():
    # 文字列や実数などを引数に取ると、動いてしまう
    with pytest.raises(ValueError):
        ClosedInterval(lower=3, upper=1)

def test_is_include(closed_interval):
    assert closed_interval.is_include(num=1) == True

def test_is_equivalent(closed_interval):
    assert closed_interval.is_equivalent([1,2,3]) == True

def test_is_subset(closed_interval):
    assert closed_interval.is_inclusiveness([1,2]) == True
    
def test_is_lower_include(closed_interval):
    assert closed_interval.is_inclusiveness([0,2]) == False

def test_is_upper_include(closed_interval):
    assert closed_interval.is_inclusiveness([2,5]) == False