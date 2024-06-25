from clrs.selection_sort import selection_sort


def test_selection_sort():
    data = [1, 5, 3, 4, 6, 2]
    selection_sort(data)
    expected = [1, 2, 3, 4, 5, 6]
    assert data == expected
