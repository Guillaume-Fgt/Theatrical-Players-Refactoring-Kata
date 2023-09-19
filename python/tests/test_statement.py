import json

import pytest
from approvaltests import verify
from approval_utilities.utils import get_adjacent_file

from statement import statement


def test_example_statement() -> None:
    with open(get_adjacent_file("invoice.json")) as f:
        invoice = json.loads(f.read())
    with open(get_adjacent_file("plays.json")) as f:
        plays = json.loads(f.read())
    verify(statement(invoice, plays))


def test_example_statement_html() -> None:
    with open(get_adjacent_file("invoice.json")) as f:
        invoice = json.loads(f.read())
    with open(get_adjacent_file("plays.json")) as f:
        plays = json.loads(f.read())
    verify(statement(invoice, plays, html=True))


def test_statement_with_new_play_types() -> None:
    with open(get_adjacent_file("invoice_new_plays.json")) as f:
        invoice = json.loads(f.read())
    with open(get_adjacent_file("new_plays.json")) as f:
        plays = json.loads(f.read())
    with pytest.raises(ValueError) as exception_info:
        statement(invoice, plays)
    assert "unknown type" in str(exception_info.value)


def test_statement_with_handled_new_play_type() -> None:
    with open(get_adjacent_file("invoice_new_plays_working.json")) as f:
        invoice = json.loads(f.read())
    with open(get_adjacent_file("new_plays_working.json")) as f:
        plays = json.loads(f.read())
    verify(statement(invoice, plays))
