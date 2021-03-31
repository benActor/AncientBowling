from unittest import TestCase, main
from ancientBowling import AncientBowling


class AncientBowlingTest(TestCase):
    def setUp(self):
        self.bowling = AncientBowling()

    def test_bowling_class(self):
        self.assertIsInstance(self.bowling, AncientBowling)


if __name__ == '__main__':
    main()