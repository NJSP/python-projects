# Online Shopping Cart (Part 2)

class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0
        self.item_quantity = 0
        self.item_description = "none"
    def print_item_cost(self):
        print(self.item_name + " " + str(self.item_quantity) + " @ $" + str(self.item_price) + " = $" + str(self.item_price * self.item_quantity))
    def print_item_description(self):
        print(self.item_name + ": " + self.item_description)

class ShoppingCart:
    def __init__(self):
        self.customer_name = "none"
        self.current_date = "January 1, 2016"
        self.cart_items = []
    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)
    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")
    def modify_item(self, ItemToPurchase):
        for item in self.cart_items:
            if item.item_name == ItemToPurchase.item_name:
                item.item_quantity = ItemToPurchase.item_quantity
                return
        print("Item not found in cart. Nothing modified.")
    def get_num_items_in_cart(self):
        num_items = 0
        for item in self.cart_items:
            num_items += item.item_quantity
        return num_items
    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += (item.item_price * item.item_quantity)
        return total_cost
    def print_total(self):
        print(self.customer_name + "'s Shopping Cart - " + self.current_date)
        print("Number of Items: " + str(self.get_num_items_in_cart()) + "\n")
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                item.print_item_cost()
        print("\nTotal: $" + str(self.get_cost_of_cart()))
    def print_descriptions(self):
        print(self.customer_name + "'s Shopping Cart - " + self.current_date + "\n")
        print("Item Descriptions")
        for item in self.cart_items:
            item.print_item_description()
    def print_menu(self):
        print("\nMENU\n"
                "a - Add item to cart\n"
                "r - Remove item from cart\n"
                "c - Change item quantity\n"
                "i - Output items' descriptions\n"
                "o - Output shopping cart\n"
                "q - Quit\n")
    # execute_menu()
    # Takes 2 parameters: a character representing the user's choice and a shopping cart. Performs the menu options described below in step 5, according to the users choice.'
    def execute_menu(self, choice):
        while choice != 'q':
            if choice == 'a':
                print("ADD ITEM TO CART")
                item = ItemToPurchase()
                item.item_name = input("Enter the item name:\n")
                item.item_description = input("Enter the item description:\n")
                item.item_price = int(input("Enter the item price:\n"))
                item.item_quantity = int(input("Enter the item quantity:\n"))
                self.add_item(item)
            elif choice == 'r':
                print("REMOVE ITEM FROM CART")
                item_name = input("Enter name of item to remove:\n")
                self.remove_item(item_name)
            elif choice == 'c':
                print("CHANGE ITEM QUANTITY")
                item = ItemToPurchase()
                item.item_name = input("Enter the item name:\n")
                item.item_quantity = int(input("Enter the new quantity:\n"))
                self.modify_item(item)
            elif choice == 'i':
                print("OUTPUT ITEMS' DESCRIPTIONS")
                self.print_descriptions()
            elif choice == 'o':
                print("OUTPUT SHOPPING CART")
                self.print_total()
            elif choice == 'q':
                break
            else:
                print("")
            choice = input("Choose an option:\n")
        return


if __name__ == "__main__":
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    print("\nCustomer name: " + customer_name)
    print("Today's date: " + current_date)
    ShoppingCart = ShoppingCart()
    ShoppingCart.customer_name = customer_name
    ShoppingCart.current_date = current_date
    ShoppingCart.print_menu()
    ShoppingCart.execute_menu(input("Choose an option:\n"))
    

