import pytest

def test_underwriting_dscr_calculation():
    rev = 500000.0
    exp = 300000.0
    net = rev - exp
    loan_pmt = 50000.0
    dscr = net / loan_pmt
    assert dscr >= 1.25
