"""Tests for the society dues ledger."""

import unittest

import society_dues as sd


class SocietyDuesTests(unittest.TestCase):

    def setUp(self):
        sd.conn.execute("DELETE FROM dues")

    def test_independent_history_lists(self):
        first = sd.add_due("B-101", "Nov", 3000)
        second = sd.add_due("B-102", "Nov", 3500)
        self.assertIsNot(first, second)

    def test_sql_injection_protection(self):
        sd.add_due("X'); DROP TABLE dues; --", "Nov", 1000)
        count = sd.conn.execute(
            "SELECT COUNT(*) FROM dues"
        ).fetchone()[0]
        self.assertEqual(count, 1)

    def test_valid_arithmetic(self):
        self.assertEqual(sd.penalty("50 * 2"), 100)

    def test_malicious_expression_rejected(self):
        result = sd.penalty(
            "__import__('os').system('echo hacked')"
        )
        self.assertEqual(result, 0)

    def test_payment_collection(self):
        sd.add_due("B-101", "Nov", 3000)
        self.assertEqual(sd.collect("B-101", "Nov"), 3000)
        self.assertNotIn("B-101", sd.pending())

    def test_pending_dues(self):
        sd.add_due("B-102", "Nov", 3500)
        self.assertIn("B-102", sd.pending())


if __name__ == "__main__":
    unittest.main()
