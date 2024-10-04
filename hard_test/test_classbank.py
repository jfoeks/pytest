from all_class.BankAccount_class import BankAccount
import pytest
def test_initial_balance():
    account = BankAccount()
    assert account.get_balance() == 0

def test_initial_balance_with_value():
    account = BankAccount(100)
    assert account.get_balance() == 100

def test_deposit():
    account = BankAccount(100)
    account.deposit(50)
    assert account.get_balance() == 150

def test_deposit_negative_amount():
    account = BankAccount()
    with pytest.raises(ValueError):
        account.deposit(-50)

def test_withdraw():
    account = BankAccount(100)
    account.withdraw(50)
    assert account.get_balance() == 50

def test_withdraw_exceeding_amount():
    account = BankAccount(100)
    with pytest.raises(ValueError, match="Недостаточно средств"):
        account.withdraw(150)
