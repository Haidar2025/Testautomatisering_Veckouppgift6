# coding: utf-8
# ===================================
# Veckouppgift 6 - Section 2
# Countries (Lander)
# ===================================

print("="*60)
print("SECTION 2: Countries (Lander)")
print("="*60)

# ============================================================
# Exercise 1a: Create Country objects for Iceland and Denmark
# ============================================================
print("\n--- Exercise 1a: Create Country Objects ---")
print("""
Creating objects for Nordic countries:
- Iceland: 383,726 inhabitants (Jan 2024)
- Denmark: 5,961,249 inhabitants (Jan 2024)
""")

class Country:
    def __init__(self, name, pop):
        self.__name = name
        self.__population = pop

# Create country objects
se = Country("Sverige", 10.5)
no = Country("Norge", 5.5)
is_country = Country("Island", 0.4)  # 383,726 ≈ 0.4 million
dk = Country("Danmark", 6.0)  # 5,961,249 ≈ 6.0 million

print("[OK] Country objects created for Sweden, Norway, Iceland, and Denmark")

# ============================================================
# Exercise 1b: Add print_info method
# ============================================================
print("\n--- Exercise 1b: Add print_info Method ---")

class Country:
    def __init__(self, name, pop):
        self.__name = name
        self.__population = pop
    
    def print_info(self):
        """Print information about the country"""
        print(f"I {self.__name} bor det {self.__population} miljoner invanare")

# Recreate objects with new class definition
se = Country("Sverige", 10.5)
no = Country("Norge", 5.5)
is_country = Country("Island", 0.4)
dk = Country("Danmark", 6.0)

print("\nTesting print_info method:")
se.print_info()
no.print_info()
is_country.print_info()
dk.print_info()

# ============================================================
# Exercise 1c: Add area property with default value
# ============================================================
print("\n--- Exercise 1c: Add Area Property ---")
print("Adding area as an optional property with default value None\n")

class Country:
    def __init__(self, name, pop, area=None):
        self.__name = name
        self.__population = pop
        self.__area = area  # Area in km², default is None
    
    def print_info(self):
        """Print information about the country"""
        print(f"I {self.__name} bor det {self.__population} miljoner invanare")

# Recreate objects with area data (in thousand km²)
se = Country("Sverige", 10.5, 450)      # 450,295 km²
no = Country("Norge", 5.5, 385)         # 385,207 km²
is_country = Country("Island", 0.4, 103) # 103,000 km²
dk = Country("Danmark", 6.0, 43)        # 42,933 km²
fi = Country("Finland", 5.6)            # Without area (to test default)

print("Testing with area property:")
se.print_info()
fi.print_info()

# ============================================================
# Exercise 1d: Update print_info to show area if available
# ============================================================
print("\n--- Exercise 1d: Update print_info to Show Area ---")

class Country:
    def __init__(self, name, pop, area=None):
        self.__name = name
        self.__population = pop
        self.__area = area
    
    def print_info(self):
        """Print information about the country, including area if available"""
        info = f"I {self.__name} bor det {self.__population} miljoner invanare"
        
        if self.__area is not None:
            info += f" och landet har en area pa {self.__area} tusen km2"
        
        print(info)

# Recreate objects
se = Country("Sverige", 10.5, 450)
no = Country("Norge", 5.5, 385)
is_country = Country("Island", 0.4, 103)
dk = Country("Danmark", 6.0, 43)
fi = Country("Finland", 5.6)  # No area specified

print("\nTesting updated print_info:")
se.print_info()
no.print_info()
fi.print_info()  # Should not show area

# ============================================================
# Exercise 1e: Add method to add languages
# ============================================================
print("\n--- Exercise 1e: Add Language Support ---")
print("Adding support for multiple official languages\n")

class Country:
    def __init__(self, name, pop, area=None):
        self.__name = name
        self.__population = pop
        self.__area = area
        self.__languages = []  # List to store multiple languages
    
    def print_info(self):
        """Print information about the country, including area if available"""
        info = f"I {self.__name} bor det {self.__population} miljoner invanare"
        
        if self.__area is not None:
            info += f" och landet har en area pa {self.__area} tusen km2"
        
        print(info)
    
    def add_language(self, language):
        """Add an official language to the country"""
        if language not in self.__languages:
            self.__languages.append(language)
            print(f"[OK] Added {language} to {self.__name}'s official languages")
        else:
            print(f"[INFO] {language} is already an official language of {self.__name}")

# Recreate objects
se = Country("Sverige", 10.5, 450)
no = Country("Norge", 5.5, 385)
fi = Country("Finland", 5.6, 338)
ch = Country("Schweiz", 8.7, 41)  # Switzerland

print("Testing add_language method:")
se.add_language("Svenska")
fi.add_language("Finska")
fi.add_language("Svenska")  # Finland has two official languages
ch.add_language("Tyska")
ch.add_language("Franska")
ch.add_language("Italienska")
ch.add_language("Ratoromanska")  # Switzerland has four!

# Test adding duplicate
se.add_language("Svenska")  # Should show info message

# ============================================================
# Exercise 1f: Update print_info to show languages
# ============================================================
print("\n--- Exercise 1f: Show Languages in print_info ---")

class Country:
    def __init__(self, name, pop, area=None):
        self.__name = name
        self.__population = pop
        self.__area = area
        self.__languages = []
    
    def print_info(self):
        """Print full information about the country"""
        info = f"I {self.__name} bor det {self.__population} miljoner invanare"
        
        if self.__area is not None:
            info += f" och landet har en area pa {self.__area} tusen km2"
        
        print(info)
        
        # Print languages on a new line
        if self.__languages:
            if len(self.__languages) == 1:
                print(f"  Officiellt sprak: {self.__languages[0]}")
            else:
                print(f"  Officiella sprak:")
                for lang in self.__languages:
                    print(f"    - {lang}")
        else:
            print("  Inga officiella sprak registrerade")
    
    def add_language(self, language):
        """Add an official language to the country"""
        if language not in self.__languages:
            self.__languages.append(language)
    
    def get_name(self):
        """Get the country name"""
        return self.__name
    
    def get_languages(self):
        """Get list of official languages"""
        return self.__languages.copy()  # Return a copy to protect internal list

# Create comprehensive country objects
print("\nCreating Nordic and European countries with complete data:\n")

se = Country("Sverige", 10.5, 450)
se.add_language("Svenska")

no = Country("Norge", 5.5, 385)
no.add_language("Norska")

fi = Country("Finland", 5.6, 338)
fi.add_language("Finska")
fi.add_language("Svenska")

dk = Country("Danmark", 6.0, 43)
dk.add_language("Danska")

is_country = Country("Island", 0.4, 103)
is_country.add_language("Islandska")

ch = Country("Schweiz", 8.7, 41)
ch.add_language("Tyska")
ch.add_language("Franska")
ch.add_language("Italienska")
ch.add_language("Ratoromanska")

# Display all countries
countries = [se, no, fi, dk, is_country, ch]

print("="*60)
print("COMPLETE COUNTRY INFORMATION:")
print("="*60)
for country in countries:
    country.print_info()
    print()

# ============================================================
# Demonstration: Advanced Features
# ============================================================
print("\n--- Demonstration: Advanced Features ---")
print("\nFinding countries with multiple official languages:")
multilingual = [c for c in countries if len(c.get_languages()) > 1]
for country in multilingual:
    langs = ", ".join(country.get_languages())
    print(f"  {country.get_name()}: {langs}")

print("\n" + "="*60)
print("Section 2 Complete!")
print("   [OK] Country class with population created")
print("   [OK] print_info method implemented")
print("   [OK] Area property with default value added")
print("   [OK] print_info updated to show area conditionally")
print("   [OK] add_language method implemented")
print("   [OK] print_info shows all official languages")
print("   [OK] 6 countries created with complete data")
print("="*60)
