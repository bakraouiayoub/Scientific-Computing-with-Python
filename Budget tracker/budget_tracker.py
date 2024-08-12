# Class that instantiate objects based on different budget categories like food, clothing, and entertainment

class Category:
    def __init__(self,budget_categ):
        self.categ_name=budget_categ
        self.ledger=[]
 
# deposit method

    def deposit(self,amount,description=""):
        self.ledger.append({"amount": amount, "description": description})

# withdraw method

    def withdraw(self,amount,description=""):
        if not self.check_funds(amount):
            return False
        self.ledger.append({"amount": -amount, "description": description})
        return True   

# get_balance method

    def get_balance(self):
        return sum(list(map(lambda my_dict: my_dict.get("amount"),self.ledger)))

# Transfer Method

    def transfer(self, amount, categ_transfer):
        if not self.check_funds(amount):
            return False
        self.withdraw(amount,f"Transfer to {categ_transfer.categ_name}")  
        categ_transfer.deposit(amount,f"Transfer from {self.categ_name}")  
        return True

# check_funds method

    def check_funds(self,amount):
        if amount > self.get_balance():
            return False
        return True    


    def __str__(self):
        title =  self.categ_name.center(30,"*") + "\n"
        items=""
        for item in self.ledger:
            item_description = f"{item.get('description')[:23]:<23}"
            items+= item_description +  f"{item.get('amount'):>7.2f}" + "\n" 
        total= "Total:" + " " + f"{self.get_balance():.2f}" 
        return title + items + total 


# Function that returns the line separator and a string containing the different categories displayed vertically

def category_name(categories):
    Names=[category.categ_name for category in categories]
    max_length=max(len(category.categ_name) 
    for category in categories)

    bottom_chart=" "*4 + "-"*(3*len(categories)+1) +"\n"
    Names=list(map(lambda name: name.ljust(max_length),Names))
    for description in zip(*Names):
        bottom_chart+=" "*4 + "".join(map(lambda x: x.center(3), description)) + " \n"
    return (bottom_chart)            
    
    
      


# Function that takes a list of categories as an argument and returns a string that is a bar chart 

def create_spend_chart(categories):

# Total spending for each category

    spendings_by_category={category.categ_name:sum(list(map(lambda my_dict: -my_dict.get("amount") 
         if my_dict.get("amount")<0 else 0 ,category.ledger))) for category in categories}

# Percentage spent in each category rounded down to the nearest 10 
    total_spent=sum(spendings_by_category.values())
    if total_spent==0:
        rounded_percentages={category.categ_name:0 for category in categories}
    else:
        rounded_percentages={category:int(((spending/total_spent*100)//10)*10) for category,spending in 
                             spendings_by_category.items()}


# Bar chart
    title="Percentage spent by category\n"
    filling_char=" o "
    bar_range=range(100,-10,-10)
    top_chart=""
    for percentage in bar_range:
        top_chart+=f"{str(percentage): >3}"+"|"
        for category_percentage in rounded_percentages.values():
            if category_percentage >= percentage :
                top_chart+=filling_char
            else:
                top_chart+="   "
        top_chart+=" \n" 
    return (title + top_chart+category_name(categories)).rstrip('\n')
    
       



# main 
def main():
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
  

main()

