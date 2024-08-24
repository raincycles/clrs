import re

import pytest

from clrs.hash_table import HashTable


@pytest.fixture(scope="module")
def tokens():
    sample = "Welcome, Nerevar. Together we shall speak for the Law and the Land, and shall drive the mongrel dogs of the Empire from Morrowind."
    return re.sub(r"[^\w\s]", "", sample).lower().split(" ")


class TestHashTable:
    def test_insert_and_get(self, tokens):
        ht = HashTable()

        for token in tokens:
            if ht.contains(token):
                ht.insert(token, ht.get(token) + 1)
            else:
                ht.insert(token, 1)

        assert len(ht) == 18

        assert ht.get("for") == 1
        assert ht.get("and") == 2
        assert ht.get("the") == 4

    def test_remove(self, tokens):
        ht = HashTable()

        for token in tokens:
            ht.insert(token, 0)

        ht.remove("empire")

        assert len(ht) == 17
        assert not ht.contains("empire")

        assert ht.contains("for")
        assert ht.contains("and")
        assert ht.contains("the")
