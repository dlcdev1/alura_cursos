import unittest
from conta import ContaCorrent


class MainTest(unittest.TestCase):
    def test_created_new_conta(self):
        conta_do_david = ContaCorrent(1542)
        self.assertEqual(conta_do_david.__str__(), "Codigo 1542 Saldo 0")


if __name__ == "__main__":
    unittest.main()
