class Lunch:
    def __init__(self):
        self.customer = Customer()
        self.employee = Employee()

    def order(self, foodName):
        return self.customer.placeorder(foodName, self.employee)

    def result(self):
        return 'Блюдо {} готово'.format(self.customer.printFood())


class Customer:
    def __init__(self):
        self.food = Food(None)

    def placeorder(self, foodName, employee):
        self.food = employee.takeOrder(foodName)

    def printFood(self):
        return self.food.foodname


class Employee:
    def takeOrder(self, foodName):
        return Food(foodName)


class Food:
    def __init__(self, name):
        self.foodname = name

a = Lunch()
a.order('шашлык')
print(a.result())
