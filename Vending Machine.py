from prettytable import PrettyTable
import pyfiglet

text = "Aljo's Vending Machine"

# Specify the font you want to use
font = pyfiglet.Figlet(font='mini')

# Print the text in the specified font
ascii_art = font.renderText(text)
print(ascii_art)


p_key = "Price"

A1 = {"A1": "Mountain Dew", p_key: 2.50, "stock": 10}
A2 = {"A2": "Thumbs Up", p_key: 2.00, "stock": 5}
A3 = {"A3": "Lipton-Ice Tea", p_key: 2.00, "stock": 2}

B1 = {"B1": "Lays Max", p_key: 2.50, "stock": 10}
B2 = {"B2": "Cheetos Flaming hot", p_key: 3.50, "stock": 30}
B3 = {"B3": "Super rings", p_key: 4.00, "stock": 18}

C1 = {"C1": "Twix", p_key: 2.50, "stock": 4}
C2 = {"C2": "Snickers", p_key: 4.00, "stock": 7}
C3 = {"C3": "Kinder Bueno", p_key: 5.50, "stock": 20}

inventory = [A1, A2, A3, B1, B2, B3, C1, C2, C3]

#SUGGESTED PAIR WHEN BUYING A PRODUCT
item_pairs = {
    "A1": ["Lays Max"],  # Mountain Dew pairs with Lays Max.
    "A2": ["Cheetos flamin Hot"],  # Thumbs Up pairs with Cheetos Flaming Hot
    "A3": [],  # No suggestions for Lipton-Ice Tea
    "B1": ["Kinder bueno"],  # Lays Max pairs with   Kinder Bueno
    "B2": [],  # No suggestions for Cheetos Flaming Hot
    "B3": ["Snickers"],  # Super rings pair with Snickers
    "C1": ["Cheetos Flamin Hot"],  # Twix pairs with Cheetos Flamin Hot
    "C2": ["Super rings"],  # Snickers pairs with Super rings
    "C3": ["Lays Max"],  # Kinder Bueno pairs with Lays Max
}

# Displays the inventory
def display_invent():
    table = PrettyTable()
    table.field_names = ["Item Code", "Item", "Price", "stock"]

    for item in inventory:
        item_code = next(iter(item.keys()))
        item_name = item[item_code]
        item_price = item[p_key]
        item_stock = item["stock"]

        table.add_row([item_code, item_name, item_price, item_stock])

    print(table)

#vending Machine
def v_machine():
    while True:
        display_invent()

        item_code = input("Enter The Item Code You Want To Purchase: ")
        item = next((item for item in inventory if item_code in item), None)

        if not item:
            print("Invalid Item Code, Try again later!")
            continue

        quantity = int(input("Enter the quantity you want to buy: "))

        if quantity > item["stock"]:
            print(f"Sorry, only {item['stock']} of that item are available. ")
            continue
        total_cost = quantity * item[p_key]
        print(f'The total cost for {quantity} {item[item_code]}: ${total_cost:.2f}')

        payment = float(input("Enter the amount you are paying: $"))
        
        total_cost = item[p_key] * quantity

        while payment < total_cost:
            print(f"insufficient Amount. Please add ${total_cost - payment:.2f} more. ")
            payment += float(input("Enter Additional Payment: $"))

        change = payment - total_cost
        print(f"Here is your Change : ${change:.2f}")

        item["stock"] -= quantity
        print(f"Thank you for your Purchase! Enjoy Your {quantity} {item[item_code]}")

        sug_pair = item_pairs.get(item_code, [])
        if sug_pair:
            p_name = sug_pair[0]
            print(f"Would You Like To Pair Your {item[item_code]} with a {p_name}? (Y/N)")
            p_choice = input().upper()
            if p_choice == "Y":
                # Find the item code of the suggested pair
                p_item = next((item for item in inventory if p_name in item.values()), None)
                if p_item:
                    #calculate total price for the pair (quantity should be 1)
                    total_cost = p_item[p_key] * 1
                    print(f"Total Price for 1 {p_name}: ${total_cost:.2f}")

                    #Payment and handle paymet logic for the pair
                    payment = float(input("Enter the amount you are paying for the pair: $"))
                    while payment < total_cost:
                        print(f"Insufficient Amount. Please add ${total_cost - payment:.2f} more. ")
                        payment += float(input("Enter Additional Payment: $"))

                    change = payment - total_cost
                    print(f"Here Is Your Change: ${change:.2f}")

                    # Update stock for the pair Item
                    p_item["stock"] -= 1
                    print(f"Thank You For Your Purchase! Enjoy Your {p_name}")
                
                else:
                    print(f"Sorry {p_name} Is Currently Out Of stock.")
            else:
                print("Thank you for the purchase, hope you have a wonderful day. \n Please Come Back Again.")


if __name__ == "__main__":
    v_machine() # starts the vending machine simulation
            
    
            

