pizza_orders = ['Margherita','Pepperoni','Meat Lovers,','Supreme']
finished_pizzas=[]

while pizza_orders:
    current_pizza=pizza_orders.pop(0)
    print(f"Your pizza{current_pizza}is finished!")
    finished_pizzas.append(current_pizza)

for pizza in finished_pizzas:
    print(f"The pizza {pizza} was made.")
    