import unittest
from duration_math import format_duration, parse_duration

class Tests(unittest.TestCase):
    def test_round_trip(self):
        self.assertEqual(parse_duration("1h30m"), 5400)
        self.assertEqual(format_duration(90061), "1d1h1m1s")

if __name__ == "__main__":
    unittest.main()
