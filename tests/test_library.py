import unittest
import pas2_rle_codec as api


class Tests(unittest.TestCase):
    def test_roundtrip(self):
        for value in [b"", b"a" * 300, bytes(range(256)), b"aabbbcc"]:
            self.assertEqual(api.decode(api.encode(value)), value)

    def test_split_long_runs(self):
        self.assertEqual(api.encode(b"a" * 256), bytes([255, 97, 1, 97]))

    def test_invalid(self):
        for value in [b"x", bytes([0, 1])]:
            with self.assertRaises(ValueError):
                api.decode(value)
        with self.assertRaises(ValueError):
            api.decode(bytes([255, 1]), 10)


if __name__ == "__main__":
    unittest.main()
