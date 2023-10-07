class Dish:
    id = 0
    def __init__(self, name, price):
        Dish.id += 1
        self.name = name
        self.price = price
        self.id = Dish.id

class Order:
    def __init__(self, table):
        self.table = table
        self.dishes = {}

    def add_dish(self, dish: Dish):
        self.dishes.update({dish.id: dish})

    def remove_dish(self, dish: Dish):
        del self.dishes[dish.id]
        
    def calculate_total(self):
        cost: float = 0
        for dish in self.dishes.values():
            dish: Dish
            cost += dish.price
        return cost 

def print_order(order: Order):
    print(f"\n{order.table}")
    print("Ваш заказ:")
    for dish in order.dishes.values():
        dish: Dish
        print(f"  Блюдо: {dish.name}, цена: {dish.price}") 
    print(f"К оплате: {order.calculate_total()}")
    print("Спасибо за посещение нашего магазина ^-^\n")

# Создание блюд
dish1 = Dish("Стейк", 25.99)
dish2 = Dish("Салат", 12.99)
dish3 = Dish("Паста", 18.99)

# Создание заказов
order1 = Order("Столик 1")
order2 = Order("Столик 2")

# Добавление блюд в заказы
order1.add_dish(dish1)
order1.remove_dish(dish1) # Передумал XD
order1.add_dish(dish3)
order2.add_dish(dish2)

# Вывод информации о заказах
print_order(order1)
print_order(order2)