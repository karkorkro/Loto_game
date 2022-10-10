import unittest
from Class_description_for_cards import Card
from Class_description_for_cards import ComputerCard


class TestCard(unittest.TestCase):

    def setUp(self) -> None:
        self.card = Card()

    def test_init(self):
        self.assertEqual(self.card.crossed_nums, 0)
        self.assertFalse(self.card.lost)
        self.assertEqual(len(self.card.nums), 15)
        for i in self.card.nums:
            self.assertIn(i, range(1, 91))
        self.assertEqual(len(self.card.card), 27)
        for i in self.card.nums:
            self.assertIn(str(i), self.card.appearance)

    def test_cross(self):
        self.assertNotIn(-1, self.card.card)
        self.card.cross(self.card.nums[0])
        self.assertNotIn(self.card.nums[0], self.card.card)
        self.assertIn(-1, self.card.card)
        self.assertTrue(self.card.crossed_nums)

    def test_update_appearance(self):
        n = self.card.appearance
        self.card.cross(self.card.nums[0])
        self.assertNotEqual(n, self.card.appearance)


class TestComputerCard(unittest.TestCase):
    def setUp(self) -> None:
        self.card = ComputerCard()

    def test_strike_correct_num(self):
        n = self.card.appearance
        self.card.strike(self.card.nums[0])
        self.assertNotIn(self.card.nums[0], self.card.card)
        self.assertNotEqual(n, self.card.appearance)

    def test_strike_incorrect_num(self):
        n = self.card.appearance
        self.card.strike(120)
        self.card.strike(-5)
        self.assertEqual(n, self.card.appearance)


