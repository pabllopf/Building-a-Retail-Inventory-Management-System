class Product:
    inventory = []  # Class-level variable to store all products. This is shared among all instances of Product.

    def __init__(self, product_id, name, category, quantity, price, supplier):
        # The __init__ method is the constructor. It initializes a new instance of the Product class.
        self.product_id = product_id  # Instance variable to store the product's ID.
        self.name = name  # Instance variable to store the product's name.
        self.category = category  # Instance variable to store the product's category.
        self.quantity = quantity  # Instance variable to store the quantity of the product.
        self.price = price  # Instance variable to store the price of the product.
        self.supplier = supplier  # Instance variable to store the supplier of the product.
        Product.inventory.append(self)  # Add this new product instance to the class-level inventory list.

    @classmethod
    def add_product(cls, name, category, quantity, price, supplier):
        # This is a class method that adds a new product to the inventory.
        product_id = len(cls.inventory) + 1  # Generate a new product ID by counting existing products and adding 1.
        new_product = cls(product_id, name, category, quantity, price, supplier)  # Create a new product instance.
        return "Product added successfully"  # Return a confirmation message.

    @classmethod
    def update_product(cls, product_id, quantity=None, price=None, supplier=None):
        # This class method updates the details of an existing product.
        for product in cls.inventory:  # Loop through the inventory to find the product with the given ID.
            if product.product_id == product_id:  # Check if this is the product we want to update.
                if quantity is not None:  # If a new quantity is provided, update it.
                    product.quantity = quantity
                if price is not None:  # If a new price is provided, update it.
                    product.price = price
                if supplier is not None:  # If a new supplier is provided, update it.
                    product.supplier = supplier
                return "Product information updated successfully"  # Return a confirmation message.
        return "Product not found"  # If the product ID was not found, return this message.

    @classmethod
    def delete_product(cls, product_id):
        # This class method deletes a product from the inventory.
        for i, product in enumerate(cls.inventory):  # Loop through the inventory with index to find the product.
            if product.product_id == product_id:  # Check if this is the product we want to delete.
                del cls.inventory[i]  # Delete the product from the inventory list.
                return "Product deleted successfully"  # Return a confirmation message.
        return "Product not found"  # If the product ID was not found, return this message.


class Order:
    def __init__(self, order_id, products, customer_info=None):
        # The __init__ method is the constructor. It initializes a new instance of the Order class.
        self.order_id = order_id  # Instance variable to store the order's ID.
        self.products = products  # Instance variable to store the list of products in the order. Each product is represented as a tuple (product_id, quantity).
        self.customer_info = customer_info  # Instance variable to store optional customer information.

    def place_order(self, product_id, quantity, customer_info=None):
        # This method adds a product to the order.
        for product in Product.inventory:
            if product.product_id == product_id and product.quantity >= quantity: # Check that the product exist in the inventory and that there's stock
                product.quantity -= quantity  # Update the stock of the product by reducing it by the ordered quantity
                self.products.append((product_id, quantity))  # Add the product and quantity as a tuple to the order's products list.
                if customer_info:  # If customer information is provided, update it.
                    self.customer_info = customer_info
                return f"Order placed successfully. Order ID: {self.order_id}"  # Return a confirmation message with the order ID.
        return "Order could not be placed. Product not found or insufficient quantity."
