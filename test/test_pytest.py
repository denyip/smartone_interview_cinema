from src.just_for_test_pytest import add_xy

def test_add_1():
    assert add_xy(1, 2) == 3
def test_add_2():
    assert add_xy(-3, -10) == -13
def test_add_3():
    assert add_xy(0, 0) == 0
def test_add_4():
    assert add_xy(-3, 10) == 7
def test_add_5_false():
    assert add_xy(10, 10) == 30
    