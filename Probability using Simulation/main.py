from prob_simul import Hat,experiment
seed_=15000
myhat=Hat(black=5,red=8,green=3,blue=9)
print(f"The hat contains: \n\n {myhat.contents}")
print("\n")
expected_balls={'black':2,'red':2,'green':2,'blue':3}
wording_dict={"0":"at least","1":"exactly"}
print(wording_dict)
wording=int(input('Choose the wording used for the problem using the corresponding keys of "at least" or "exactly": '))
print("\n\n")
num_experiments=int(input("Choose the number of simulations:"))
num_balls_drawn=int(input("Choose the number of balls drawn:"))
print("\n\n")
char_expected_balls=", ".join([f"{value} {key} balls" for key,value in expected_balls.items()])
random.seed(seed_)
print(f"The probability of drawing {wording_dict.get(str(wording))} {char_expected_balls} is: {experiment(myhat,expected_balls,num_balls_drawn,num_experiments,wording)}")
