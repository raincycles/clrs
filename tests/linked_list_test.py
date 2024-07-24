from clrs.linked_list import LinkedList


class TestLinkedList:
    def test_reverse(self):
        input_list = [1, 2, 3, 4, 5]
        linked_list = LinkedList()

        for x in input_list:
            linked_list.push_back(x)

        linked_list.reverse()
        assert list(linked_list) == list(reversed(input_list))

    def test_insert(self):
        input_list = [1, 2, 4]
        linked_list = LinkedList()

        for x in input_list:
            linked_list.push_back(x)

        linked_list.insert_before(2, 3)
        assert list(linked_list) == [1, 2, 3, 4]

        linked_list.insert_after(3, 5)
        assert list(linked_list) == [1, 2, 3, 4, 5]

    def test_pop(self):
        input_list = [1, 2, 3, 4, 5]
        linked_list = LinkedList()

        for x in input_list:
            linked_list.push_back(x)

        assert linked_list.pop_front() == 1
        assert linked_list.pop_back() == 5

    def test_push(self):
        input_list = [4, 5]
        linked_list = LinkedList()

        for x in input_list:
            linked_list.push_back(x)

        linked_list.push_back(6)
        assert list(linked_list) == [4, 5, 6]

        linked_list.push_front(3)
        assert list(linked_list) == [3, 4, 5, 6]
