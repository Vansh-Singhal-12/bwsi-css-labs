from labs.lab_1.lab_1d import two_sum

def test_two_sum_standard():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]

def test_two_sum_not_first_indices():
    assert two_sum([3, 2, 4], 6) == [1, 2]