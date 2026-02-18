# coding: utf-8
# ===================================
# Veckouppgift 6 - Section 3
# Bank Account (TDD Approach)
# ===================================

print("="*60)
print("SECTION 3: Bank Account (TDD Approach)")
print("="*60)

# ============================================================
# TDD Step 1: Write Tests First (RED)
# ============================================================
print("\n--- TDD Step 1: Write Tests First ---")
print("Following TDD methodology: RED -> GREEN -> REFACTOR\n")

# Test functions (will be implemented later)
def test_initial_balance():
    """Test that new account starts with 0 balance"""
    account = BankAccount()
    assert account.balance() == 0
    print("[OK] test_initial_balance: Passed!")

def test_deposit():
    """Test depositing money increases balance"""
    account = BankAccount()
    account.deposit(100)
    assert account.balance() == 100
    account.deposit(50)
    assert account.balance() == 150
    print("[OK] test_deposit: Passed!")

def test_deposit_negative():
    """Test that depositing negative amount is rejected"""
    account = BankAccount()
    result = account.deposit(-50)
    assert result == False
    assert account.balance() == 0
    print("[OK] test_deposit_negative: Passed!")

def test_withdraw():
    """Test withdrawing money decreases balance"""
    account = BankAccount()
    account.deposit(100)
    result = account.withdraw(30)
    assert result == True
    assert account.balance() == 70
    print("[OK] test_withdraw: Passed!")

def test_withdraw_insufficient_funds():
    """Test that withdrawing more than balance is rejected"""
    account = BankAccount()
    account.deposit(50)
    result = account.withdraw(100)
    assert result == False
    assert account.balance() == 50
    print("[OK] test_withdraw_insufficient_funds: Passed!")

def test_withdraw_negative():
    """Test that withdrawing negative amount is rejected"""
    account = BankAccount()
    account.deposit(100)
    result = account.withdraw(-30)
    assert result == False
    assert account.balance() == 100
    print("[OK] test_withdraw_negative: Passed!")

def test_apply_interest():
    """Test that interest is calculated and added correctly"""
    account = BankAccount(interest_rate=0.05)  # 5% interest
    account.deposit(1000)
    account.apply_interest()
    assert account.balance() == 1050.0
    print("[OK] test_apply_interest: Passed!")

def test_apply_interest_multiple_times():
    """Test compound interest"""
    account = BankAccount(interest_rate=0.10)  # 10% interest
    account.deposit(100)
    account.apply_interest()
    assert account.balance() == 110.0
    account.apply_interest()
    assert account.balance() == 121.0  # Compound interest
    print("[OK] test_apply_interest_multiple_times: Passed!")

def test_can_afford():
    """Test checking if account can afford a bill"""
    account = BankAccount()
    account.deposit(100)
    assert account.can_afford(50) == True
    assert account.can_afford(100) == True
    assert account.can_afford(101) == False
    print("[OK] test_can_afford: Passed!")

def test_can_afford_zero_balance():
    """Test can_afford with zero balance"""
    account = BankAccount()
    assert account.can_afford(0) == True
    assert account.can_afford(1) == False
    print("[OK] test_can_afford_zero_balance: Passed!")

# ============================================================
# TDD Step 2: Implement the Class (GREEN)
# ============================================================
print("\n--- TDD Step 2: Implement BankAccount Class ---\n")

class BankAccount:
    def __init__(self, initial_balance=0, interest_rate=0.0):
        """
        Initialize a bank account
        
        Args:
            initial_balance: Starting balance (default 0)
            interest_rate: Annual interest rate as decimal (default 0.0)
        """
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        
        self.__balance = float(initial_balance)
        self.__interest_rate = interest_rate
        self.__transaction_history = []
    
    def deposit(self, amount):
        """
        Deposit money into the account
        
        Args:
            amount: Amount to deposit
            
        Returns:
            True if successful, False if amount is invalid
        """
        if amount <= 0:
            print(f"[ERROR] Cannot deposit {amount}. Amount must be positive.")
            return False
        
        self.__balance += amount
        self.__transaction_history.append(f"Deposit: +{amount}")
        return True
    
    def withdraw(self, amount):
        """
        Withdraw money from the account
        
        Args:
            amount: Amount to withdraw
            
        Returns:
            True if successful, False if insufficient funds or invalid amount
        """
        if amount <= 0:
            print(f"[ERROR] Cannot withdraw {amount}. Amount must be positive.")
            return False
        
        if amount > self.__balance:
            print(f"[ERROR] Insufficient funds. Balance: {self.__balance}, Requested: {amount}")
            return False
        
        self.__balance -= amount
        self.__transaction_history.append(f"Withdraw: -{amount}")
        return True
    
    def balance(self):
        """
        Get current balance
        
        Returns:
            Current balance
        """
        return self.__balance
    
    def apply_interest(self):
        """
        Calculate and add interest to the account
        
        Returns:
            Amount of interest added
        """
        interest = self.__balance * self.__interest_rate
        self.__balance += interest
        self.__transaction_history.append(f"Interest: +{interest:.2f}")
        return interest
    
    def can_afford(self, amount):
        """
        Check if the account has enough funds for a bill
        
        Args:
            amount: Amount to check
            
        Returns:
            True if account can afford it, False otherwise
        """
        return self.__balance >= amount
    
    def get_transaction_history(self):
        """Get list of all transactions"""
        return self.__transaction_history.copy()
    
    def __str__(self):
        """String representation of the account"""
        return f"BankAccount(balance={self.__balance:.2f}, interest_rate={self.__interest_rate:.2%})"

print("BankAccount class implemented with methods:")
print("  - deposit(amount)")
print("  - withdraw(amount)")
print("  - balance()")
print("  - apply_interest()")
print("  - can_afford(amount)")

# ============================================================
# TDD Step 3: Run Tests (RED -> GREEN)
# ============================================================
print("\n--- TDD Step 3: Run Tests ---\n")

test_initial_balance()
test_deposit()
test_deposit_negative()
test_withdraw()
test_withdraw_insufficient_funds()
test_withdraw_negative()
test_apply_interest()
test_apply_interest_multiple_times()
test_can_afford()
test_can_afford_zero_balance()

print("\n[OK] All 10 tests passed!")

# ============================================================
# TDD Step 4: Refactor (Improve Code Quality)
# ============================================================
print("\n--- TDD Step 4: Refactor Complete ---")
print("""
Refactoring improvements made:
- Private attributes (__balance, __interest_rate)
- Input validation for all methods
- Comprehensive error messages
- Transaction history tracking
- String representation (__str__ method)
- Docstrings for all methods
- Float conversion for precise calculations
""")

# ============================================================
# Demonstration: Real-World Usage
# ============================================================
print("\n--- Demonstration: Real-World Usage ---\n")

# Create savings account with 3% interest
savings = BankAccount(interest_rate=0.03)
print(f"Created savings account: {savings}")

print("\nMonthly transactions:")
print("Month 1: Deposit salary")
savings.deposit(5000)
print(f"  Balance: {savings.balance()} kr")

print("\nMonth 2: Pay bills and add interest")
savings.withdraw(1500)
print(f"  After bills: {savings.balance()} kr")
savings.apply_interest()
print(f"  After interest: {savings.balance():.2f} kr")

print("\nMonth 3: Emergency expense")
can_buy_laptop = savings.can_afford(8000)
print(f"  Can afford 8000 kr laptop? {can_buy_laptop}")
can_buy_phone = savings.can_afford(3000)
print(f"  Can afford 3000 kr phone? {can_buy_phone}")

if can_buy_phone:
    savings.withdraw(3000)
    print(f"  Bought phone! New balance: {savings.balance():.2f} kr")

print("\nTransaction history:")
for transaction in savings.get_transaction_history():
    print(f"  {transaction}")

# ============================================================
# Advanced Example: Multiple Accounts
# ============================================================
print("\n--- Advanced Example: Multiple Accounts ---\n")

checking = BankAccount(1000, interest_rate=0.0)  # No interest
savings = BankAccount(5000, interest_rate=0.05)  # 5% interest
investment = BankAccount(10000, interest_rate=0.08)  # 8% interest

accounts = {
    "Checking": checking,
    "Savings": savings,
    "Investment": investment
}

print("Account Summary:")
total = 0
for name, account in accounts.items():
    bal = account.balance()
    total += bal
    print(f"  {name:12s}: {bal:10,.2f} kr")

print(f"  {'Total':12s}: {total:10,.2f} kr")

print("\nApplying annual interest:")
for name, account in accounts.items():
    initial = account.balance()
    interest = account.apply_interest()
    final = account.balance()
    if interest > 0:
        print(f"  {name}: {initial:.2f} kr + {interest:.2f} kr = {final:.2f} kr")

print("\n" + "="*60)
print("Section 3 Complete!")
print("   [OK] TDD approach applied (RED -> GREEN -> REFACTOR)")
print("   [OK] BankAccount class implemented")
print("   [OK] deposit() method with validation")
print("   [OK] withdraw() method with validation")
print("   [OK] balance() method")
print("   [OK] apply_interest() method with compound interest")
print("   [OK] can_afford() method")
print("   [OK] All 10 unit tests passed")
print("   [OK] Transaction history tracking added")
print("="*60)
