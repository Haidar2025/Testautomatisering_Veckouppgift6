# Veckouppgift 6 - Object-Oriented Programming (OOP)

**Course:** Test Automation with Python  
**Student:** Haidar  
**Week:** 8 (16 February 2026)  
**Topic:** Object-Oriented Programming, Classes, Encapsulation, Inheritance

---

## Table of Contents

- [Overview](#overview)
- [Learning Objectives](#learning-objectives)
- [Project Structure](#project-structure)
- [Installation and Running](#installation-and-running)
- [Sections](#sections)
- [OOP Concepts](#oop-concepts)
- [Code Quality](#code-quality)

---

## Overview

This week's assignment focuses on **Object-Oriented Programming (OOP)** in Python. The assignment covers fundamental OOP concepts through practical implementations:

- Classes and Objects
- Encapsulation (Private Attributes)
- Inheritance and Polymorphism
- Methods and Properties
- Test-Driven Development (TDD)
- Real-world Applications

---

## Learning Objectives

After completing this assignment, I can:

1. **Create and use classes** with proper encapsulation
2. **Implement inheritance** and understand polymorphism
3. **Use private attributes** and accessor methods
4. **Apply TDD** to OOP development
5. **Design class hierarchies** for real-world applications
6. **Manage object references** and IDs

---

## Project Structure

```
Veckouppgift6/
│
├── main_1.py              # Section 1: Read and Understand Code
├── main_2.py              # Section 2: Country Class
├── main_3.py              # Section 3: Bank Account (TDD)
├── main_4.py              # Section 4: Webshop System
│
├── README.md              # This file
├── .gitignore             # Git ignore file
│
└── Veckouppgift 6.pdf     # Assignment description (not in repo)
```

---

## Installation and Running

### Prerequisites

- Python 3.x installed
- No external libraries required (standard library only)

### Running the Programs

```bash
# Section 1: OOP Code Analysis
python main_1.py

# Section 2: Country Class
python main_2.py

# Section 3: Bank Account with TDD
python main_3.py

# Section 4: Webshop System
python main_4.py
```

---

## Sections

### Section 1: Read and Understand Code (main_1.py)

**Content:**
- **Exercise 1:** SafeStorage class with private attributes
- **Exercise 2a:** Animal inheritance - find and fix errors
- **Exercise 2b:** Add new animal class (Parrot)
- **Demonstration:** Polymorphism in action

**Key Concepts:**
- Name mangling with `__` prefix
- Inheritance hierarchy
- Method overriding
- Polymorphism

**Running:**
```bash
python main_1.py
```

**Output Highlights:**
- Fixed syntax errors in Animal classes
- Added missing Rooster class
- Implemented Parrot with custom behavior
- Demonstrated polymorphic method calls

---

### Section 2: Countries (main_2.py)

**Content:**
Progressive development of a Country class through 6 exercises:

1. **1a:** Create Country objects for Nordic countries
2. **1b:** Add `print_info()` method
3. **1c:** Add area property with default value
4. **1d:** Update print_info to show area conditionally
5. **1e:** Add `add_language()` method for multiple languages
6. **1f:** Display all languages in print_info

**Features:**
- Private attributes for name, population, area
- Dynamic language list
- Conditional display logic
- Support for multilingual countries (Finland, Switzerland)

**Running:**
```bash
python main_2.py
```

**Example Output:**
```
I Sverige bor det 10.5 miljoner invanare och landet har en area pa 450 tusen km2
  Officiellt sprak: Svenska

I Finland bor det 5.6 miljoner invanare och landet har en area pa 338 tusen km2
  Officiella sprak:
    - Finska
    - Svenska
```

---

### Section 3: Bank Account (main_3.py)

**Approach:** Test-Driven Development (TDD)

**TDD Process:**
1. **RED:** Write tests first (10 test functions)
2. **GREEN:** Implement BankAccount class to pass tests
3. **REFACTOR:** Improve code quality

**Features:**
- `deposit(amount)` - Add money with validation
- `withdraw(amount)` - Remove money with balance check
- `balance()` - Get current balance
- `apply_interest()` - Calculate and add compound interest
- `can_afford(amount)` - Check if balance is sufficient
- Transaction history tracking
- Private attributes for security

**Test Coverage:**
- [OK] Initial balance (0)
- [OK] Deposit positive amounts
- [OK] Reject negative deposits
- [OK] Withdraw with sufficient funds
- [OK] Reject withdrawal with insufficient funds
- [OK] Reject negative withdrawals
- [OK] Apply interest correctly
- [OK] Compound interest calculation
- [OK] Check affordability
- [OK] Zero balance edge case

**Running:**
```bash
python main_3.py
```

**Results:** All 10 tests passed

---

### Section 4: Webshop System (main_4.py)

**Architecture:** Three-class e-commerce system

#### Class 1: Product
- Unique ID generation (class variable)
- Name, price, description, stock
- Stock management (add/reduce)
- Availability checking

#### Class 2: ShoppingCart
- Add/remove/update items
- Quantity tracking
- Total price calculation
- Display cart contents

#### Class 3: Order
- Create order from cart
- Automatic stock reduction
- Status tracking (Pending -> Processing -> Shipped -> Delivered)
- Order history

**Test Data:** 10 tool shop products
```
1. Cordless Drill - 899 kr (Stock: 15)
2. Hammer - 149 kr (Stock: 25)
3. Screwdriver Set - 299 kr (Stock: 30)
... and 7 more
```

**Complete Shopping Flow:**
1. Create shopping cart
2. Add items (Drill, Hammers, Tool Box, Safety Glasses)
3. View cart (Total: 1794 kr)
4. Update quantities
5. Place order
6. Reduce stock automatically
7. Track order status

**Running:**
```bash
python main_4.py
```

**Advanced Features:**
- Multiple simultaneous orders
- Stock tracking across orders
- Customer name association
- Formatted displays

---

## OOP Concepts

### 1. Encapsulation

**Private Attributes:**
```python
class BankAccount:
    def __init__(self):
        self.__balance = 0  # Private attribute
```

**Why?** Prevents direct access, forces use of methods for validation.

### 2. Inheritance

**Base Class:**
```python
class Animal:
    def make_noise(self):
        print("Generic animal sound")
```

**Derived Classes:**
```python
class Dog(Animal):
    def make_noise(self):  # Override
        print("Voff!")
```

### 3. Polymorphism

**Same Interface, Different Behavior:**
```python
animals = [Dog(), Cat(), Parrot()]
for animal in animals:
    animal.make_noise()  # Each responds differently
```

### 4. Class Variables

**Shared Across All Instances:**
```python
class Product:
    __next_id = 1  # Shared counter
    
    def __init__(self):
        self.__id = Product.__next_id
        Product.__next_id += 1  # Increment for next instance
```

---

## Code Quality

### Code Standards
- [OK] Descriptive class and method names
- [OK] Docstrings for all classes and methods
- [OK] Private attributes with `__` prefix
- [OK] Input validation in all methods
- [OK] Consistent formatting (PEP 8)

### OOP Best Practices
- [OK] Single Responsibility Principle
- [OK] Encapsulation of data
- [OK] DRY (Don't Repeat Yourself)
- [OK] Meaningful abstractions

### Testing
- [OK] TDD approach for Bank Account
- [OK] 10 comprehensive unit tests
- [OK] Edge cases covered
- [OK] Real-world scenarios tested

---

## Key Takeaways

### What I Learned

1. **Encapsulation is powerful:** Private attributes prevent bugs and enforce validation

2. **Inheritance simplifies code:** Base classes reduce duplication

3. **Polymorphism enables flexibility:** Same interface, different implementations

4. **TDD improves design:** Writing tests first leads to better APIs

5. **Class design matters:** Proper structure makes code maintainable

### Challenges

- Understanding name mangling (`__attribute`)
- Managing object references (cart contains product IDs)
- Implementing compound interest correctly
- Designing the webshop class relationships

### Improvements

- Could add more validation (e.g., email format)
- Implement database persistence
- Add payment processing
- Create GUI interface

---

## Technologies

- **Language:** Python 3
- **Paradigm:** Object-Oriented Programming
- **Testing:** Test-Driven Development
- **Code Style:** PEP 8

---

## Contact

**Student:** Haidar  
**GitHub:** [Haidar2025](https://github.com/Haidar2025)  
**Repository:** [Testautomatisering_Veckouppgift6](https://github.com/Haidar2025/Testautomatisering_Veckouppgift6)

---

## License

This project is created for educational purposes as part of the Test Automation with Python course.

---

**Created:** 18 February 2026  
**Last Updated:** 18 February 2026  
**Version:** 1.0
