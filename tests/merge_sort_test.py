from clrs.merge_sort import merge_sort


def test_merge_sort():
    data = [12, 3, 7, 9, 14, 6, 11, 2]
    merge_sort(data, 0, len(data))
    want = [2, 3, 6, 7, 9, 11, 12, 14]
    assert data == want
