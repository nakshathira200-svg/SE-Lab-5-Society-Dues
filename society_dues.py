"""Apartment society maintenance dues ledger."""

import ast
import operator
import os
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute(
    """
    CREATE TABLE dues (
        flat TEXT,
        month TEXT,
        amount INTEGER,
        paid INTEGER
    )
    """
)

TREASURER_PASSWORD = os.getenv("TREASURER_PASSWORD")


def add_due(flat, month, amount, history=None):
    """Add a maintenance due and record it in the history."""
    if history is None:
        history = []

    conn.execute(
        "INSERT INTO dues VALUES (?, ?, ?, 0)",
        (flat, month, amount),
    )
    history.append((flat, month))
    return history


def collect(flat, month):
    """Collect payment for a flat and return its amount."""
    row = conn.execute(
        "SELECT amount FROM dues WHERE flat = ? AND month = ?",
        (flat, month),
    ).fetchone()

    if row:
        conn.execute(
            "UPDATE dues SET paid = 1 WHERE flat = ? AND month = ?",
            (flat, month),
        )
        return row[0]

    return None


def evaluate_expression(node):
    """Safely evaluate basic arithmetic expression nodes."""
    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)) and not isinstance(
            node.value, bool
        ):
            return node.value
        raise ValueError("Invalid numeric value")

    binary_operations = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.FloorDiv: operator.floordiv,
        ast.Mod: operator.mod,
        ast.Pow: operator.pow,
    }

    unary_operations = {
        ast.UAdd: operator.pos,
        ast.USub: operator.neg,
    }

    if isinstance(node, ast.BinOp):
        operation = binary_operations.get(type(node.op))
        if operation is None:
            raise ValueError("Unsupported arithmetic operation")

        left = evaluate_expression(node.left)
        right = evaluate_expression(node.right)

        if isinstance(node.op, ast.Pow) and abs(right) > 10:
            raise ValueError("Exponent is too large")

        return operation(left, right)

    if isinstance(node, ast.UnaryOp):
        operation = unary_operations.get(type(node.op))
        if operation is None:
            raise ValueError("Unsupported unary operation")
        return operation(evaluate_expression(node.operand))

    raise ValueError("Invalid arithmetic expression")


def penalty(rule):
    """Calculate a late fee using safe arithmetic evaluation."""
    try:
        expression = ast.parse(rule, mode="eval")
        return evaluate_expression(expression.body)
    except (
        SyntaxError,
        ValueError,
        TypeError,
        ZeroDivisionError,
        OverflowError,
    ):
        return 0


def pending():
    """Return the flat numbers with unpaid dues."""
    rows = conn.execute(
        "SELECT flat FROM dues WHERE paid = 0"
    ).fetchall()
    return [row[0] for row in rows]


def main():
    """Run the society dues ledger demonstration."""
    add_due("A-101", "Oct", 2500)
    add_due("A-102", "Oct", 2500)

    print(collect("A-101", "Oct"))
    print(penalty("50 * 2"))
    print(pending())


if __name__ == "__main__":
    main()
