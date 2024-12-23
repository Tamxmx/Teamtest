import unittest
from teamB import calAge , calRank

class TestTeamA(unittest.TestCase):

    def test_calAge(self):
        self.assertEqual(calAge(20), 2547)

    def test_calRank(self):
        self.assertEqual(calRank("A"), "High Distinction")
        self.assertEqual(calRank("B+"), "Distinction")
        self.assertEqual(calRank("B"), "Distinction")
        self.assertEqual(calRank("C+"), "Good")
        self.assertEqual(calRank("C"), "Good")
        self.assertEqual(calRank("D+"), "Normal")
        self.assertEqual(calRank("D"), "Normal")
        self.assertEqual(calRank("F"), "Failed")
        self.assertEqual(calRank("Error Score"), "Error Rank")

if __name__ == "__main__":
    unittest.main(verbosity=2)