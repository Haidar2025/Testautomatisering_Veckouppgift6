# coding: utf-8
# ===================================
# Veckouppgift 6 - Section 4
# Webshop (E-commerce System)
# ===================================

print("="*60)
print("SECTION 4: Webshop (E-commerce System)")
print("="*60)

# ============================================================
# Class 1: Product
# ============================================================
print("\n--- Class 1: Product ---")

class Product:
    # Class variable to track next available ID
    __next_id = 1
    
    def __init__(self, name, price, description="", stock=0):
        """
        Initialize a product
        
        Args:
            name: Product name
            price: Product price
            description: Product description (optional)
            stock: Available stock quantity (optional)
        """
        self.__id = Product.__next_id
        Product.__next_id += 1
        
        self.__name = name
        self.__price = float(price)
        self.__description = description
        self.__stock = stock
    
    def get_id(self):
        """Get product ID"""
        return self.__id
    
    def get_name(self):
        """Get product name"""
        return self.__name
    
    def get_price(self):
        """Get product price"""
        return self.__price
    
    def get_description(self):
        """Get product description"""
        return self.__description
    
    def get_stock(self):
        """Get available stock"""
        return self.__stock
    
    def set_price(self, new_price):
        """Update product price"""
        if new_price >= 0:
            self.__price = float(new_price)
            return True
        return False
    
    def add_stock(self, quantity):
        """Add stock quantity"""
        if quantity > 0:
            self.__stock += quantity
            return True
        return False
    
    def reduce_stock(self, quantity):
        """Reduce stock quantity"""
        if 0 < quantity <= self.__stock:
            self.__stock -= quantity
            return True
        return False
    
    def is_available(self, quantity=1):
        """Check if product is available in requested quantity"""
        return self.__stock >= quantity
    
    def __str__(self):
        """String representation"""
        return f"Product #{self.__id}: {self.__name} - {self.__price} kr (Stock: {self.__stock})"
    
    def display_info(self):
        """Display detailed product information"""
        print(f"\nProduct ID: {self.__id}")
        print(f"Name: {self.__name}")
        print(f"Price: {self.__price:.2f} kr")
        print(f"Stock: {self.__stock} units")
        if self.__description:
            print(f"Description: {self.__description}")

print("Product class created with:")
print("  - Unique ID generation")
print("  - Name, price, description, stock tracking")
print("  - Stock management methods")
print("  - Availability checking")

# ============================================================
# Class 2: ShoppingCart
# ============================================================
print("\n--- Class 2: ShoppingCart ---")

class ShoppingCart:
    __next_id = 1
    
    def __init__(self):
        """Initialize an empty shopping cart"""
        self.__id = ShoppingCart.__next_id
        ShoppingCart.__next_id += 1
        
        # Dictionary: product_id -> quantity
        self.__items = {}
        # Reference to actual Product objects
        self.__products = {}
    
    def add_item(self, product, quantity=1):
        """
        Add product to cart
        
        Args:
            product: Product object
            quantity: Quantity to add
            
        Returns:
            True if successful, False otherwise
        """
        if not product.is_available(quantity):
            print(f"[ERROR] Not enough stock for {product.get_name()}")
            return False
        
        product_id = product.get_id()
        
        # Store product reference
        if product_id not in self.__products:
            self.__products[product_id] = product
        
        # Add or update quantity
        if product_id in self.__items:
            self.__items[product_id] += quantity
        else:
            self.__items[product_id] = quantity
        
        print(f"[OK] Added {quantity}x {product.get_name()} to cart")
        return True
    
    def remove_item(self, product_id):
        """Remove product from cart completely"""
        if product_id in self.__items:
            product_name = self.__products[product_id].get_name()
            del self.__items[product_id]
            del self.__products[product_id]
            print(f"[OK] Removed {product_name} from cart")
            return True
        return False
    
    def update_quantity(self, product_id, new_quantity):
        """Update quantity of a product in cart"""
        if product_id not in self.__items:
            print("[ERROR] Product not in cart")
            return False
        
        if new_quantity <= 0:
            return self.remove_item(product_id)
        
        product = self.__products[product_id]
        if not product.is_available(new_quantity):
            print(f"[ERROR] Not enough stock for {product.get_name()}")
            return False
        
        self.__items[product_id] = new_quantity
        print(f"[OK] Updated quantity to {new_quantity}")
        return True
    
    def get_total(self):
        """Calculate total cart value"""
        total = 0
        for product_id, quantity in self.__items.items():
            product = self.__products[product_id]
            total += product.get_price() * quantity
        return total
    
    def get_item_count(self):
        """Get total number of items in cart"""
        return sum(self.__items.values())
    
    def is_empty(self):
        """Check if cart is empty"""
        return len(self.__items) == 0
    
    def clear(self):
        """Empty the cart"""
        self.__items.clear()
        self.__products.clear()
        print("[OK] Cart cleared")
    
    def get_items(self):
        """Get list of (product, quantity) tuples"""
        return [(self.__products[pid], qty) for pid, qty in self.__items.items()]
    
    def display(self):
        """Display cart contents"""
        if self.is_empty():
            print("\n[CART IS EMPTY]")
            return
        
        print(f"\n{'='*60}")
        print(f"SHOPPING CART #{self.__id}")
        print(f"{'='*60}")
        print(f"{'Item':<30} {'Qty':>5} {'Price':>10} {'Total':>10}")
        print("-" * 60)
        
        for product, qty in self.get_items():
            name = product.get_name()
            price = product.get_price()
            total = price * qty
            print(f"{name:<30} {qty:>5} {price:>10.2f} {total:>10.2f}")
        
        print("-" * 60)
        print(f"{'Total:':<30} {self.get_item_count():>5} {'':<10} {self.get_total():>10.2f}")
        print("=" * 60)

print("ShoppingCart class created with:")
print("  - Add/remove/update items")
print("  - Calculate total price")
print("  - Track item quantities")
print("  - Display cart contents")

# ============================================================
# Class 3: Order
# ============================================================
print("\n--- Class 3: Order ---")

class Order:
    __next_id = 1
    
    def __init__(self, cart, customer_name="Guest"):
        """
        Create order from shopping cart
        
        Args:
            cart: ShoppingCart object
            customer_name: Name of customer
        """
        if cart.is_empty():
            raise ValueError("Cannot create order from empty cart")
        
        self.__id = Order.__next_id
        Order.__next_id += 1
        
        self.__customer_name = customer_name
        self.__items = []  # List of (product_id, product_name, quantity, price)
        self.__total = 0
        self.__status = "Pending"
        
        # Copy items from cart
        for product, qty in cart.get_items():
            self.__items.append({
                'product_id': product.get_id(),
                'name': product.get_name(),
                'quantity': qty,
                'price': product.get_price(),
                'subtotal': product.get_price() * qty
            })
            self.__total += product.get_price() * qty
            
            # Reduce stock
            product.reduce_stock(qty)
    
    def get_id(self):
        """Get order ID"""
        return self.__id
    
    def get_customer_name(self):
        """Get customer name"""
        return self.__customer_name
    
    def get_total(self):
        """Get order total"""
        return self.__total
    
    def get_status(self):
        """Get order status"""
        return self.__status
    
    def set_status(self, new_status):
        """Update order status"""
        valid_statuses = ["Pending", "Processing", "Shipped", "Delivered", "Cancelled"]
        if new_status in valid_statuses:
            self.__status = new_status
            print(f"[OK] Order #{self.__id} status updated to: {new_status}")
            return True
        return False
    
    def get_items(self):
        """Get order items"""
        return self.__items.copy()
    
    def display(self):
        """Display order details"""
        print(f"\n{'='*60}")
        print(f"ORDER #{self.__id}")
        print(f"{'='*60}")
        print(f"Customer: {self.__customer_name}")
        print(f"Status: {self.__status}")
        print(f"{'-'*60}")
        print(f"{'Item':<30} {'Qty':>5} {'Price':>10} {'Total':>10}")
        print(f"{'-'*60}")
        
        for item in self.__items:
            print(f"{item['name']:<30} {item['quantity']:>5} "
                  f"{item['price']:>10.2f} {item['subtotal']:>10.2f}")
        
        print(f"{'-'*60}")
        print(f"{'TOTAL:':<46} {self.__total:>10.2f} kr")
        print(f"{'='*60}")

print("Order class created with:")
print("  - Create order from cart")
print("  - Automatic stock reduction")
print("  - Order status tracking")
print("  - Display order details")

# ============================================================
# Test Data: Creating Tool Shop Products
# ============================================================
print("\n--- Creating Test Data: Tool Shop Products ---\n")

# Create products (using AI-suggested tool shop data)
products = [
    Product("Cordless Drill", 899, "18V lithium-ion battery", 15),
    Product("Hammer", 149, "Claw hammer with fiberglass handle", 25),
    Product("Screwdriver Set", 299, "10-piece precision screwdriver set", 30),
    Product("Tape Measure", 79, "5m steel tape measure", 40),
    Product("Adjustable Wrench", 189, "250mm adjustable wrench", 20),
    Product("Pliers Set", 349, "3-piece pliers set", 18),
    Product("Tool Box", 599, "Large plastic tool box with organizer", 12),
    Product("Safety Glasses", 49, "Anti-fog safety glasses", 50),
    Product("Work Gloves", 99, "Heavy-duty work gloves, size L", 35),
    Product("LED Flashlight", 199, "Rechargeable LED flashlight", 22)
]

print(f"Created {len(products)} products:")
for p in products[:5]:  # Show first 5
    print(f"  {p}")
print("  ...")

# ============================================================
# Demonstration: Complete Shopping Flow
# ============================================================
print("\n--- Demonstration: Complete Shopping Flow ---")

print("\n1. Customer creates shopping cart:")
cart = ShoppingCart()

print("\n2. Customer browses and adds items:")
cart.add_item(products[0], 1)  # Cordless Drill
cart.add_item(products[1], 2)  # 2x Hammer
cart.add_item(products[6], 1)  # Tool Box
cart.add_item(products[7], 3)  # 3x Safety Glasses

print("\n3. Customer views cart:")
cart.display()

print("\n4. Customer updates quantity:")
cart.update_quantity(products[1].get_id(), 1)  # Reduce hammers to 1

print("\n5. Updated cart:")
cart.display()

print("\n6. Customer places order:")
order = Order(cart, customer_name="Erik Andersson")

print("\n7. Order confirmation:")
order.display()

print("\n8. Cart after order (should be same, but stock reduced):")
cart.display()

print("\n9. Check stock after order:")
print(f"  {products[0].get_name()} stock: {products[0].get_stock()} (was 15)")
print(f"  {products[1].get_name()} stock: {products[1].get_stock()} (was 25)")

print("\n10. Update order status:")
order.set_status("Processing")
order.set_status("Shipped")
order.set_status("Delivered")

# ============================================================
# Advanced Example: Multiple Orders
# ============================================================
print("\n--- Advanced Example: Multiple Orders ---")

# Customer 2
cart2 = ShoppingCart()
cart2.add_item(products[2], 2)  # 2x Screwdriver Set
cart2.add_item(products[3], 1)  # 1x Tape Measure
cart2.add_item(products[8], 2)  # 2x Work Gloves

order2 = Order(cart2, "Anna Svensson")

# Customer 3
cart3 = ShoppingCart()
cart3.add_item(products[4], 1)  # Adjustable Wrench
cart3.add_item(products[5], 1)  # Pliers Set
cart3.add_item(products[9], 1)  # LED Flashlight

order3 = Order(cart3, "Johan Karlsson")

print("\nAll orders:")
for order in [order, order2, order3]:
    print(f"\nOrder #{order.get_id()} - {order.get_customer_name()}: "
          f"{order.get_total():.2f} kr ({order.get_status()})")

# ============================================================
# Summary: Stock Status
# ============================================================
print("\n--- Summary: Stock Status After All Orders ---\n")
print(f"{'Product':<30} {'Original':>10} {'Current':>10} {'Sold':>10}")
print("-" * 65)

original_stock = [15, 25, 30, 40, 20, 18, 12, 50, 35, 22]
for i, product in enumerate(products):
    current = product.get_stock()
    original = original_stock[i]
    sold = original - current
    print(f"{product.get_name():<30} {original:>10} {current:>10} {sold:>10}")

print("\n" + "="*60)
print("Section 4 Complete!")
print("   [OK] Product class with unique ID system")
print("   [OK] ShoppingCart class with item management")
print("   [OK] Order class with status tracking")
print("   [OK] Stock reduction on order placement")
print("   [OK] 10 tool shop products created")
print("   [OK] Complete shopping flow demonstrated")
print("   [OK] Multiple orders processed")
print("="*60)
