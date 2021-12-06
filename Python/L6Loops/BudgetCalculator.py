'''
Using the names dictionary and order_list shown below, write a program that fits the following conditions:

- It should produce an order by adding items to receipt from order_list sequentially.

- It should Print "Current Total: £x" with each iteration

- If the order value exceeds the budget value, it should stop adding items and print "Budget Exceeded!".

- If not, each time it adds items, it should:

- Print "Adding *full name of item* (quantity)".

- Subtract the price from budget.

- Add the price to running_total.

- It should print out running_total, order and budget formatted into print statements (done for you).

order_list = [("tom", 0.87, 4),

("sug", 1.09, 3),

("ws", 0.29, 4),

("juc", 1.89, 1),

("fo", 1.29, 2)]

names = {"tom":"Tomatoes",

"sug":"Sugar",

"ws":"Washing Sponges",

"juc":"Juice",

"fo":"Foil"}

budget = 10.00

running_total = 0

receipt = []
'''

def ProductTot(item, *args):
    s = (args[item][1]*args[item][2])
    return s




def ProductPrice(item, *args):
    return args[item][1]




def FullProductName(item, *args, **kwargs):
    return (kwargs[args[item][0]])




def QtyRet(item, *args):
    return args[item][2]



order_list = [
    ("tom", 0.87, 4),
    ("sug", 1.09, 3),
    ("ws", 0.29, 4),
    ("juc", 1.89, 1),
    ("fo", 1.29, 2)
]

names = {
    'tom' : 'Tomatoes',
    'sug' : 'Sugar',
    'ws'  : 'Washing Sponges',
    'juc' : 'Juice',
    'fo'  : 'Foil'
}

budget = 10.00
running_total = 0
receipt = []

for item in range(0, len(order_list)) :
    if (running_total + ProductTot(item, *order_list)) < budget:
        running_total += ProductTot(item, *order_list)
        receipt.append(order_list[item])
        print(f"Adding: {FullProductName(item, *order_list, **names)} , {QtyRet(item, *order_list)}(qty)")
        print("Current Total: £ ", running_total)
    else:
        print("Budget Exceeded!")
        break
    

print('Thanks for been our customer :)')
print(50*'*')
print(f'For the budget amount: £{budget} You can affort:')
print(receipt)
print('Total amount: £', running_total)

