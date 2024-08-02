from clrs.binary_search_tree import BinarySearchTree


class TestBinarySearchTree:
    def test_insert(self):
        input_list = [5, 2, 8, 7, 1, 4]
        tree = BinarySearchTree()

        for value in input_list:
            tree.insert(value)

        assert len(tree) == len(input_list)
        assert list(tree) == [1, 2, 4, 5, 7, 8]

        prev_len = len(tree)
        tree.insert(7)

        assert len(tree) == prev_len

    def test_remove(self):
        input_list = [5, 2, 8, 7, 1, 4]
        tree = BinarySearchTree()

        for value in input_list:
            tree.insert(value)

        prev_len = len(tree)
        tree.remove(7)
        tree.remove(5)

        assert len(tree) == prev_len - 2
        assert list(tree) == [1, 2, 4, 8]

    def test_min(self):
        input_list = [5, 2, 8, 7, 1, 4]
        tree = BinarySearchTree()

        for value in input_list:
            tree.insert(value)

        assert tree.min() == 1

    def test_max(self):
        input_list = [5, 2, 8, 7, 1, 4]
        tree = BinarySearchTree()

        for value in input_list:
            tree.insert(value)

        assert tree.max() == 8

    def test_next_nearest(self):
        input_list = [5, 2, 8, 7, 1, 4]
        tree = BinarySearchTree()

        for value in input_list:
            tree.insert(value)

        assert tree.next_nearest(5) == 7
        assert tree.next_nearest(3) == 4

    def test_prev_nearest(self):
        input_list = [5, 2, 8, 7, 1, 4]
        tree = BinarySearchTree()

        for value in input_list:
            tree.insert(value)

        assert tree.prev_nearest(5) == 4
        assert tree.prev_nearest(3) == 2
