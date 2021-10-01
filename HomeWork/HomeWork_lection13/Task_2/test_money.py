import unittest
import Money


class MoneyTest(unittest.TestCase):

    def test_sum(self):
        res = Money.Money(50, 0) + Money.Money(50, 0)
        print(res)
        self.assertEqual("100, 0", Money.Money(50, 0) + Money.Money(50, 0))

    def test_sub(self):
        res = Money.Money(50, 0) - Money.Money(50, 0)
        print(res)
        self.assertEqual("0, 0", Money.Money(50, 0) - Money.Money(50, 0))

    def test_div(self):
        res = Money.Money(50, 0) / 2
        print(res)
        self.assertEqual("50, 0", Money.Money(100, 0) / 2)

    def test_gt(self):
        self.assertTrue(Money.Money(20, 0) > Money.Money(10, 0))

    def test_lt(self):
        self.assertTrue(Money.Money(10, 0) < Money.Money(20, 0))

    def test_ge(self):
        self.assertTrue(Money.Money(20, 0) >= Money.Money(10, 0))

    def test_le(self):
        self.assertTrue(Money.Money(10, 0) <= Money.Money(20, 0))

    def test_ne(self):
        self.assertTrue(Money.Money(20, 0) != Money.Money(10, 0))

    def test_eq(self):
        self.assertTrue(Money.Money(20, 0) == Money.Money(20, 0))

    def test_get_money(self):
        self.assertEqual("10, 10", Money.Money(10, 10).get_money())

    def test_set_course(self):
        money = Money.Money(10, 10)
        self.assertEqual(money.course, 1)
        money.set_course(80)
        self.assertEqual(money.course, 80)
        money.set_course(0)
        self.assertEqual(money.course, 80)

    def test_get_currency(self):
        money = Money.Money(10, 10)
        money.set_course(2)
        self.assertEqual("5.05", money.get_currency())
        money.set_course(10)
        self.assertEqual("1.01", money.get_currency())
        money.set_course(8)
        self.assertEqual("1.2625", money.get_currency())


if __name__ == '__main__':
    unittest.main()
