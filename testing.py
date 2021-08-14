import unittest
import solve


class Test(unittest.TestCase):
    def test_india(self):
        ans = solve.solve('india.csv')
        india = ans[0]
        self.assertEqual(len(india.keys()), 21, "Extra entries, check the" +
                         " function filtering values for india's population")

    def test_south_east(self):
        ans = solve.solve('south_east.csv')
        south_east = ans[1]
        self.assertEqual(len(south_east.keys()), 9, "Extra Entries,check the" +
                         " function filtering values for south-east asian" +
                         " countries population in 2014")

    def test_saarc(self):
        ans = solve.solve('southern_asia.csv')
        southern_asia = ans[2]
        self.assertEqual(len(southern_asia.keys()), 11, "Extra Entries, check"
                         + " the function filtering values for southern asian"
                         + " countries population")

    def test_asia(self):
        ans = solve.solve('asia.csv')
        southern_asia = ans[3]
        self.assertEqual(len(southern_asia.keys()), 11, "Extra Entries,check" +
                         "the function filtering values for asian" +
                         " countries population 2004-2014")
