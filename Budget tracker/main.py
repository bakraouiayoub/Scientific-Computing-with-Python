from budget_tracker.py import Category
from budget_tracker.py import create_spend_chart
food = Category('Food') 
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert') 
clothing = Category('Clothing')
food.transfer(400, clothing)
clothing.withdraw(200,'suit')
auto = Category('Auto')
auto.deposit(1500,'initial deposit')
auto.withdraw(400,'Repairs')
print(food)
print('\n')
print(clothing)
print('\n')
print(auto)
print('\n')
print(create_spend_chart([food,clothing,auto]))
  

