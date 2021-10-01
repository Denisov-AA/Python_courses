def original_multiplier(m=1, source=[1, 2, 3]):
    result = source
    for i, x in enumerate(source):
        result[i] *= m
    return result


# Implement function correct_multiplier here


multiplier = original_multiplier


# multiplier = correct_multiplier


def test_default_values():
    assert multiplier() == [1, 2, 3]


def test_default_list_with_custom_multiplier():
    assert multiplier(5) == [5, 10, 15]


def test_custom_list_with_custom_multiplier():
    assert multiplier(12, [1, 2]) == [12, 24]


def test_empty_list():
    empty_list = []
    assert multiplier(source=empty_list) == empty_list


def test_that_result_is_a_new_list():
    origin = [1, 2, 3, 4, 5]
    new = multiplier(2, origin)
    assert new == [2, 4, 6, 8, 10]
    assert new is not origin


def test_that_original_list_is_not_changed():
    origin = [1, 2, 3, 4, 5]
    new = multiplier(2, origin)
    assert new == [2, 4, 6, 8, 10]
    assert origin == [1, 2, 3, 4, 5]


def test_multiple_subsequent_calls_with_default_list():
    assert multiplier(2) == [2, 4, 6]
    assert multiplier(2) == [2, 4, 6]
    assert multiplier(2) == [2, 4, 6]
    assert multiplier(2) == [2, 4, 6]
    assert multiplier(2) == [2, 4, 6]
