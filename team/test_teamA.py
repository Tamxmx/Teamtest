import unittest
from teamA import calAge , calGrade

class TestTeamA(unittest.TestCase):

    def test_calAge(self):
        self.assertEqual(calAge(2004), 20)

    def test_calGrade(self):
        self.assertEqual(calGrade(81), "A")
        self.assertEqual(calGrade(76), "B+")
        self.assertEqual(calGrade(73), "B")
        self.assertEqual(calGrade(68), "C+")
        self.assertEqual(calGrade(62), "C")
        self.assertEqual(calGrade(57), "D+")
        self.assertEqual(calGrade(54), "D")
        self.assertEqual(calGrade(49), "F")
        self.assertEqual(calGrade(120), "Error Score")

if __name__ == "__main__":
    unittest.main(verbosity=2)