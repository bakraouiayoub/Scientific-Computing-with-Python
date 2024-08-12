# Function that checks the rules and returns the numbers, the operators, the solutions of the given problems 
#and the maximum number of digits for each problem.
def numbers_operators(problems):
    if len(problems)>5:
        return 'Error: Too many problems.'
    numbers=[]
    operators=[]
    solutions=[]
    max_digits=[]
    problems_dict={}
    for problem in problems:
        first_number=problem.split()[0]
        second_number=problem.split()[2]
        operator=problem.split()[1]
        if operator not in set(("+","-")):
            return "Error: Operator must be '+' or '-'."
        elif not first_number.isdigit() or not second_number.isdigit():
            return 'Error: Numbers must only contain digits.' 
        elif max(len(first_number),len(second_number))>4:
            return 'Error: Numbers cannot be more than four digits.'  
        else:
            numbers.append([first_number,second_number])
            operators.append(operator) 
            solutions.append(str(eval(problem)))
            max_digits.append(str(max(len(first_number),len(second_number))))
    problems_dict["Numbers"]=numbers
    problems_dict["Operators"]=operators
    problems_dict["Solutions"]=solutions
    problems_dict["Max_digits"]=max_digits   
    return problems_dict  

        
#function that receives a list of strings which are arithmetic problems, and returns the problems arranged vertically 
#and side-by-side

def arithmetic_arranger(problems, show_answers=False):
    number_of_problems=len(problems)
    separator=" "*4
    top_row=""
    bottom_row=""
    dashes=""
    solution=""
    
    if isinstance(numbers_operators(problems),str):
        return numbers_operators(problems)
    
    problems_dict=numbers_operators(problems)
    for problem_i in range(number_of_problems):
        if problem_i==number_of_problems-1:
            separator=""
        numbers=list(problems_dict.get("Numbers")[problem_i])
        dash_length=int(problems_dict.get("Max_digits")[problem_i])+2
        top_row+=numbers[0].rjust(dash_length) + separator
        bottom_row+=problems_dict.get("Operators")[problem_i] + numbers[1].rjust(dash_length-1) + separator
        dashes+= "-"*dash_length +separator 
        solution+=problems_dict.get("Solutions")[problem_i].rjust(dash_length) + separator
    if show_answers==True:
        return'\n'.join((top_row,bottom_row,dashes,solution))
    return'\n'.join((top_row,bottom_row,dashes))



