# coding: utf-8
# ===================================
# Veckouppgift 6 - Section 1
# Read and Understand Code - OOP
# ===================================

print("="*60)
print("SECTION 1: Read and Understand Code - OOP")
print("="*60)

# ============================================================
# Exercise 1: SafeStorage Class
# ============================================================
print("\n--- Exercise 1: SafeStorage Class ---")
print("""
This code demonstrates private attributes in Python using name mangling.
The __data attribute is private (starts with __) which means it can only
be accessed within the class through the get() and put() methods.
""")

class SafeStorage:
    __data = None
    
    def get(self):
        return self.__data
    
    def put(self, data):
        self.__data = data

# Test the class
safe = SafeStorage()
safe.put("Anakonda")
x = safe.get()
safe.put("Boaorm")
y = safe.get()
print(f"Result: x = '{x}', y = '{y}'")

print("""
Prediction: x will be 'Anakonda' and y will be 'Boaorm'

Explanation:
1. safe.put("Anakonda") - stores "Anakonda" in __data
2. x = safe.get() - retrieves "Anakonda" and stores it in x
3. safe.put("Boaorm") - REPLACES __data with "Boaorm"
4. y = safe.get() - retrieves "Boaorm" and stores it in y

So x = 'Anakonda' and y = 'Boaorm'
""")

# ============================================================
# Exercise 2a: Animal Classes - Find and Fix Errors
# ============================================================
print("\n--- Exercise 2a: Animal Classes - Find and Fix Errors ---")
print("""
Original code has several errors:
1. Dog.make_noise() - missing 'self' parameter and indentation error
2. Cat.make_noise(shelf) - parameter should be 'self', not 'shelf'
3. Rooster class is not defined but used in main code
4. sound_off([c, d, h]) - tries to pass a list but function expects single animal

Let's fix these errors:
""")

class Animal:
    def make_noise(self):
        print("Detta djur har vi inget ljud for.")

class Dog(Animal):
    def make_noise(self):  # Fixed: added 'self' and proper indentation
        print("Voff!")

class Cat(Animal):
    def make_noise(self):  # Fixed: changed 'shelf' to 'self'
        super().make_noise()
        print("Mjau!")

# Fixed: Added missing Rooster class
class Rooster(Animal):
    def make_noise(self):
        print("Kuckeliku!")

def sound_off(animal):
    animal.make_noise()

# Test the fixed code
print("\nTesting the fixed code:")
c = Cat()
d = Dog()
h = Rooster()

print("Cat sound:")
sound_off(c)

print("\nDog sound:")
sound_off(d)

print("\nRooster sound:")
sound_off(h)

# ============================================================
# Exercise 2b: Add a New Animal Class
# ============================================================
print("\n--- Exercise 2b: Add a New Animal Class ---")
print("Adding a Parrot class that repeats what you say!\n")

class Parrot(Animal):
    def __init__(self, phrase="Hej!"):
        self.phrase = phrase
    
    def make_noise(self):
        print(f"{self.phrase} {self.phrase}!")
    
    def teach(self, new_phrase):
        """Teach the parrot a new phrase"""
        self.phrase = new_phrase
        print(f"Parrot learned to say: {new_phrase}")

# Test the Parrot class
print("Testing Parrot class:")
p = Parrot()
print("Default sound:")
sound_off(p)

print("\nTeaching the parrot:")
p.teach("Polly vill ha kex")
sound_off(p)

# ============================================================
# Demonstration: Polymorphism
# ============================================================
print("\n--- Demonstration: Polymorphism ---")
print("Polymorphism allows different objects to respond to the same method call:\n")

animals = [Dog(), Cat(), Rooster(), Parrot("Hejsan")]

for i, animal in enumerate(animals, 1):
    animal_type = type(animal).__name__
    print(f"{i}. {animal_type}:", end=" ")
    animal.make_noise()

# ============================================================
# Advanced: Inheritance Hierarchy
# ============================================================
print("\n--- Advanced: Inheritance Hierarchy ---")
print("""
Inheritance allows us to create a hierarchy of classes:

        Animal (base class)
          |
    +-----+-----+-----+
    |     |     |     |
   Dog   Cat  Rooster Parrot

All subclasses inherit from Animal and can:
- Override make_noise() to provide specific behavior
- Add their own unique methods (like Parrot.teach())
- Call parent methods using super()
""")

print("\n" + "="*60)
print("Section 1 Complete!")
print("   [OK] SafeStorage class analyzed")
print("   [OK] Animal class errors found and fixed")
print("   [OK] Rooster class added")
print("   [OK] Parrot class implemented")
print("   [OK] Polymorphism demonstrated")
print("="*60)
