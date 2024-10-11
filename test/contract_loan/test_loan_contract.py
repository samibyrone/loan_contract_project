import unittest

from contract_loan.loan_contract import LoanCalculator

class TestLoanCalculator(unittest.TestCase):

    def test_setup(self):
        calculator = LoanCalculator()
        self.assertIsNone(calculator.get_borrower())
        self.assertEqual(calculator.get_interest_rate(), 24)
        self.assertIsNone(calculator.get_loan_amount())
        self.assertEqual(calculator.get_loan_period(), 1)

    def test_set_borrower(self):
        calculator = LoanCalculator()
        calculator.set_borrower("samson olarewaju")
        self.assertEqual(calculator.get_borrower(), "samson olarewaju")

    def test_set_interest_rate(self):
        calculator = LoanCalculator()
        calculator.set_borrower("samson olarewaju")
        calculator.set_loan_amount(6500000)
        self.assertEqual(calculator.get_loan_amount(), 6500000)

    def test_set_loan_period(self):
        calculator = LoanCalculator()
        calculator.set_borrower("samson olarewaju")
        calculator.set_loan_amount(4500000)
        self.assertEqual(calculator.get_loan_amount(), 4500000)
        self.assertEqual(calculator.get_loan_period(), 1)

    def test_monthly_payment(self):
        calculator = LoanCalculator()
        calculator.set_borrower("samson olarewaju")
        calculator.set_loan_amount(6500000)
        self.assertEqual(calculator.get_interest_rate(), 24)
        self.assertEqual(calculator.get_loan_period(), 1)
        self.assertEqual(calculator.get_monthly_payment(), 378.24)

    def test_total_loan_payment(self):
        calculator = LoanCalculator()
        calculator.set_borrower("samson olarewaju")
        calculator.set_loan_amount(10000)
        self.assertEqual(calculator.get_interest_rate(), 24)
        self.assertEqual(calculator.get_loan_period(), 1)
        self.assertEqual(calculator.get_total_loan_payment(), 11347.20)

    def test_invalid_loan_amount(self):
        calculator = LoanCalculator()
        calculator.set_borrower("samson olarewaju")
        self.assertRaises(ValueError, calculator.set_loan_amount, -4000)

    def test_interest_rate_cannot_change(self):
        calculator = LoanCalculator()
        calculator.set_borrower("samson olarewaju")
        calculator.set_loan_amount(4000)
        self.assertRaises(ValueError, calculator.set_interest_rate, 1)

    def test_loan_period_cannot_change(self):
        calculator = LoanCalculator()
        calculator.set_borrower("samson olarewaju")
        calculator.set_loan_amount(4000)
        calculator.get_interest_rate()
        self.assertRaises(ValueError, calculator.set_loan_period, 24)

    def test_for_float_loan_amount(self):
        calculator = LoanCalculator()
        calculator.set_borrower("samson olarewaju")
        calculator.set_loan_amount(6500000)
        calculator.get_interest_rate()
        calculator.get_loan_period()
        self.assertEqual(calculator.get_loan_amount(), 6500000)
