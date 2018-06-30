from Exercise import reward

# in case anyone is still on Python 2
def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 4


# 0.3, 0.5, 0.9, 0.7
#-2.1, -0.1, 3.2, 3.0

def test_exercise_1():
	assert isclose(reward(-2.1,0.32), -3.0882352, rel_tol=1e-3)

def test_exercise_2():
	assert isclose(reward(-0.1,0.55), -0.222222, rel_tol=1e-3)

def test_exercise_3():
	assert isclose(reward(3.2,0.95), 64.000000, rel_tol=1e-3)

def test_exercise_4():
	assert isclose(reward(3.0,0.79), 14.285714, rel_tol=1e-3)
