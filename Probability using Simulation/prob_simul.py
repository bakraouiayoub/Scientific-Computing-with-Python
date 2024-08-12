import copy
import random

class Hat:
    def __init__(self,**args):
        self.contents=[]
        for color,value in args.items():
            self.contents+=[color]*value

# Draw nbr_draws balls without replacement from the hat            
    def draw(self,nbr_draws):
        if nbr_draws > len(self.contents):
            hat_copy=self.contents.copy()
            self.contents.clear()
            return hat_copy
        random_draws=[]
        for _ in range(nbr_draws):
            random_index=random.randint(0,len(self.contents)-1)
            random_draws.append(self.contents[random_index])
            self.contents.pop(random_index)
        return random_draws    



# Function that estimates the probability of drawing num_balls_drawn containing wording("at least"-default  or "exactly") balls, using num_experiments simulations.

def experiment(hat, expected_balls, num_balls_drawn, num_experiments, wording=0):
    if wording==0 and num_balls_drawn<sum(expected_balls.values()):
        raise ValueError("For the 'at least' wording, the number of balls drawn must exceed the number of balls in the event expected_balls")
    if wording==1 and num_balls_drawn!=sum(expected_balls.values()): 
        raise ValueError("For the 'exactly' wording, the number of balls drawn must be equal to the number of balls in the event expected_balls")   
    num_success=0
    for _ in range(num_experiments):
        hat_copy=copy.deepcopy(hat)
        balls_drawn=hat_copy.draw(num_balls_drawn)
        matching_colors= [balls_drawn.count(color) for color in expected_balls]
        
        if wording==0:
            drawn_expected_balls= [drawn_nbr>=expected_nbr for drawn_nbr,expected_nbr in zip(matching_colors,expected_balls.values())]
        elif wording == 1:
            drawn_expected_balls=[drawn_nbr==expected_nbr for drawn_nbr,expected_nbr in zip(matching_colors,expected_balls.values())] 
        else:
            raise ValueError("The wording must be 'at least' or 'exactly'. ")       
        if all(drawn_expected_balls):
            num_success+=1

    return num_success/num_experiments        
