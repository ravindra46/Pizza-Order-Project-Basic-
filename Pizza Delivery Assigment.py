#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[49]:





# In[ ]:


print('''  Welcome!!!!!!!
_....._
    _.:`.--|--.`:._
  .: .'\o  | o /'. '.
 // '.  \ o|  /  o '.\
//'._o'. \ |o/ o_.-'o\\
|| o '-.'.\|/.-' o   || 
||--o--o-->| 

 ''')

available_pizzas = ['Small', 'Medium', 'Large']
available_toppings = ['Pepperoni', 'Extra Cheese', 'Thin Bread', 'Everything']
pizza_prices = {'Small':150, 'Medium': 200, 'Large':250}
topping_prices = {'Pepperoni':20 , 'Extra Cheese':10 , 'Thin Bread':50 , 'Everything': 80 }
sub_total = []
final_order = {}
customer_address = {}

#ordering a pizza
print("Hi, Welcome to Desire's Pizza Deliveries")
order_pizza = True
while order_pizza:    
    print("Please choose a pizza: ")
    
    for pizzas in available_pizzas:
        print(pizzas)
      
    while True:
        pizza = input("which pizza would you like to order?")
        if pizza in available_pizzas:
            print(f"You have ordered a {pizza}.")
            sub_total.append(pizza_prices[pizza])
            break
        if pizza not in available_pizzas:
            print(f"I am sorry, we currently do not have {pizza}.")
            
            
            
  #asking for extra toppings
    order_topping = True
    print("This is the list of available extra toppings: ")
    for toppings in available_toppings:
        print(toppings)
       
    while order_topping:
        extra_topping = input("Would you like an extra topping? yes or no?")
        if extra_topping == "yes":
            topping = input("Which one would you like to add?")
            if topping in available_toppings:
                final_order.setdefault(pizza, [])
                final_order[pizza].append(topping)
                print(f"I have added {topping}.")
                sub_total.append(topping_prices[topping])
            else:
                print(f"I am sorry, we don't have {topping} available.")

        elif extra_topping == "no":
            break
    extra_pizza = input("Would you like to order another pizza?")
    if extra_pizza == "no":
        for key, value in final_order.items():
            print(f"\nYou have order a {key} pizza with {value}")
        check_order = True
        while check_order:
        
            order_correct = input("Is this correct? yes/no ")
            if order_correct == "yes":
                check_order = False
                order_pizza = False
            if order_correct == "no":
                print(final_order)
                add_remove = input("would you like to add or remove? ")
                if add_remove == "remove":
                    remove = input("Which pizza would you like to remove? ")
                    del final_order[remove]
                    print(final_order)
                if add_remove == "add":
                    check_order = False
                    
                    
                    
                    
#finalizing the order
print(f"\nYour total order price is: Rs.{sum(sub_total)}")
print("Please provide us with your name, address and ContactNumber" )
customer_adress['name'] = input("what is your name ? ")
customer_adress['street_name'] = input("What is your streetname and housenumber ? ")
customer_adress['postalcode'] = input("What is the postalcode and cityname ? ")
customer_adress['ContactNumber'] = input("What is your ContactNumber ? ")
print(f"Thank you for your order {customer_adress['name']}.")
print("We will deliver your order to this address ASAP ")
print(customer_adress['street_name'])
print(customer_adress['postalcode'])
print(f"we will contact you on {customer_adress['ContactNumber']} if anything comes up.")



print('''  ═✿✿✿═════✿✿═════✿✿═════✿✿✿═
════════════ ('\../') ═════════════
════════════ (◕.◕) ═══════════
════════════ (,,)(,,) ═════════════
.▀█▀.█▄█.█▀█.█▄.█.█▄▀　█▄█.█▀█.█─█
─.█.─█▀█.█▀█.█.▀█.█▀▄　─█.─█▄█.█▄█
''')


# In[ ]:




