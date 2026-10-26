```python
import unittest
from trie import Trie


class TestTrie(unittest.TestCase):

    def setUp(self):
        self.trie = Trie()
        self.trie.insert("Arun")
        self.trie.insert("Aravind")
        self.trie.insert("Arjun")
        self.trie.insert("Rahul")

    def test_search_existing_contact(self):
        self.assertTrue(self.trie.search("Arun"))

    def test_search_case_insensitive(self):
        self.assertTrue(self.trie.search("ARUN"))

    def test_search_missing_contact(self):
        self.assertFalse(self.trie.search("Kumar"))

    def test_autocomplete(self):
        result = self.trie.autocomplete("Ar")
        self.assertEqual(
            [name.lower() for name in result],
            ["aravind", "arjun", "arun"]
        )

    def test_delete_existing_contact(self):
        self.assertTrue(self.trie.delete("Arun"))
        self.assertFalse(self.trie.search("Arun"))

    def test_delete_missing_contact(self):
        self.assertFalse(self.trie.delete("Kumar"))

    def test_shared_prefix_deletion(self):
        self.assertTrue(self.trie.delete("Arun"))
        self.assertTrue(self.trie.search("Aravind"))
        self.assertTrue(self.trie.search("Arjun"))

    def test_empty_contact(self):
        self.assertFalse(self.trie.delete(""))

    def test_insert_contact(self):
        self.trie.insert("Naziya")
        self.assertTrue(self.trie.search("Naziya"))


if __name__ == "__main__":
    unittest.main()
```
