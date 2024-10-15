class ItemToPurchase:
    def __init__(self):
        # Initialize item attributes with default values
        self.item_name = 'none'
        self.item_description = 'none'
        self.item_price = 0.0
        self.item_quantity = 0

    def print_item_cost(self):
        # Calculate total cost of the item
        totalCost = self.item_quantity * self.item_price
        # Print item cost in the specified format
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price:.0f} = ${totalCost:.0f}')

    def print_item_description(self):
        # Print item description in the specified format
        print(f'{self.item_name}: {self.item_description}')

class ShoppingCart:
    def __init__(self, customer_name='none', current_date='January 1, 2016'):
        # Initialize shopping cart attributes with default values
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        # Add an item to the shopping cart
        self.cart_items.append(item)

    def remove_item(self, item_name):
        # Remove an item from the shopping cart by item name
        found = False
        for i in self.cart_items:
            if i.item_name == item_name:
                found = True
                self.cart_items.remove(i)
        if found == False:
            # Print message if item was not found in the cart
            print('Item not found in cart. Nothing removed.')

    def modify_item(self, item):
        # Modify the quantity of an item in the shopping cart
        found = False
        for i in range(len(self.cart_items)):
            if self.cart_items[i].item_name == item.item_name:
                found = True
                self.cart_items[i].item_quantity = item.item_quantity
        if not found:
            # Print message if item was not found in the cart
            print('Item not found in cart. Nothing modified.')

    def get_num_items_in_cart(self):
        # Calculate the total number of items in the shopping cart
        total_num_items = 0
        for i in self.cart_items:
            total_num_items += i.item_quantity
        return total_num_items

    def get_cost_of_cart(self):
        # Calculate the total cost of the shopping cart
        total_cost = 0
        for i in self.cart_items:
            total_cost += (i.item_price * i.item_quantity)
        return total_cost

    def print_total(self):
        # Print the total cost and number of items in the shopping cart
        print(f'{self.customer_name}\'s Shopping Cart - {self.current_date}')
        print(f'Number of Items: {self.get_num_items_in_cart()}\n')

        if len(self.cart_items) > 0:
            for i in self.cart_items:
                i.print_item_cost()
        else:
            # Print message if the shopping cart is empty
            print('SHOPPING CART IS EMPTY')
        total_cost = self.get_cost_of_cart()
        print(f'\nTotal: ${total_cost:.0f}')
        
    def print_descriptions(self):
        # Print the descriptions of all items in the shopping cart
        print(f'{self.customer_name}\'s Shopping Cart - {self.current_date}\n')
        print('Item Descriptions')
        if len(self.cart_items) > 0:
            for i in self.cart_items:
                i.print_item_description()
        else:
            # Print message if the shopping cart is empty
            print('SHOPPING CART IS EMPTY')

def print_menu():
    # Print the menu options
    print('MENU')
    print('a - Add item to cart')
    print('r - Remove item from cart')
    print('c - Change item quantity')
    print('i - Output items\' descriptions')
    print('o - Output shopping cart')
    print('q - Quit\n')
    
def execute_menu(menuOp, theCart):
    # Execute the selected menu option
    if menuOp == 'a':
        print('ADD ITEM TO CART')
        name = input('Enter the item name:\n')
        description = input('Enter the item description:\n')
        price = float(input('Enter the item price:\n'))
        quantity = int(input('Enter the item quantity:\n'))

        new_item = ItemToPurchase()
        new_item.item_name = name
        new_item.item_description = description
        new_item.item_price = price
        new_item.item_quantity = quantity
        theCart.add_item(new_item)
        print()

    elif menuOp == 'r':
        print('REMOVE ITEM FROM CART')
        name = input('Enter name of item to remove:\n')
        theCart.remove_item(name)
        print()

    elif menuOp == 'c':
        print('CHANGE ITEM QUANTITY')
        name = input('Enter the item name:\n')
        quantity = int(input('Enter the new quantity:\n'))

        item = ItemToPurchase()
        item.item_name = name
        item.item_quantity = quantity
        theCart.modify_item(item)
        print()

    elif menuOp == 'i':
        print('OUTPUT ITEMS\' DESCRIPTIONS')
        theCart.print_descriptions()
        print()

    elif menuOp == 'o':
        print('OUTPUT SHOPPING CART')
        theCart.print_total()
        print()
                
if __name__ == "__main__":
    # Main execution starts here
    menu_choice = ' '
    cust_name = input('Enter customer\'s name:\n')
    day_date = input('Enter today\'s date:\n')

    print(f'\nCustomer name: {cust_name}')
    print(f'Today\'s date: {day_date}')
    print()

    my_cart = ShoppingCart(cust_name, day_date)

    print_menu()

    while menu_choice != 'q':
        menu_choice = input('Choose an option:\n')
        if menu_choice in ['a', 'r', 'c', 'i', 'o']:
            execute_menu(menu_choice, my_cart)
            print_menu()