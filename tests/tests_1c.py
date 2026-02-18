from labs.lab_1.lab_1c import max_subarray_sum

# Test 1: Standard case
def test_max_subarray_standard():
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

# Test 2: All negatives
def test_max_subarray_negatives():
    assert max_subarray_sum([-10, -2, -3, -5]) == -2

# Test 3: Single element
def test_max_subarray_single():
    assert max_subarray_sum([100]) == 100