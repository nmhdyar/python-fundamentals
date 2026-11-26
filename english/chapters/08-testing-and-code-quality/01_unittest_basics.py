import unittest


def calculate_discount(price: float, rate: float) -> float:
    if price < 0 or not 0 <= rate <= 1:
        raise ValueError("invalid price or rate")
    return price * (1 - rate)


class DiscountTests(unittest.TestCase):
    def test_discount(self) -> None:
        self.assertEqual(calculate_discount(100, 0.2), 80)

    def test_invalid_rate(self) -> None:
        with self.assertRaises(ValueError):
            calculate_discount(100, 1.5)


if __name__ == "__main__":
    unittest.main()
