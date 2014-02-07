import unittest

import marvel


PUBLIC_KEY = 'eed60d956db501cc4de289d94f580d79'
PRIVATE_KEY = 'a03352496ea7a77ec7124da8a76f9202dc560f89'


class TestCerebro(unittest.TestCase):
    def setUp(self):
        self.cerebro = marvel.Cerebro(PUBLIC_KEY, PRIVATE_KEY)

    def test_get_characters(self):
        characters = marvel.CharacterResource(self.cerebro)
        self.assertGreater(len(characters), 0)
        self.assertTrue(characters[0].name)
        self.assertGreater(len(characters[0].comics), 0)

        with self.assertRaises(IndexError):
            characters[len(characters)]
