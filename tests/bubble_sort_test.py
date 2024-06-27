from clrs.bubble_sort import bubble_sort


def test_bubble_sort():
    data = [5, 2, 4, 6, 1, 3]
    bubble_sort(data)
    expected = [1, 2, 3, 4, 5, 6]
    assert data == expected
