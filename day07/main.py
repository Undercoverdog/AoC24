class Equation:
    def __init__(self, result:int, numbers):
        self.result:int = result
        self.numbers = numbers # type int array
        return




def getInput():
    equations = [] # type Equation array
    with open("input", "r") as f:
        for line in f:
        # example line'196487536: 7 3 6 4 393 4 1 93 3 7 9 7'
            line = line.strip()
            result = int(line.split(":")[0]) # example 196487536:int
            rest = line.split(":")[1] 
            rest = rest.strip()
            rest = rest.split(" ")
            numbers = list(map(int, rest)) # example [7, 3, ..., 9, 7]:int array

            equation = Equation(result, numbers)
            equations.append(equation)
    return equations



# example 5o7o10o3o5 -> evaluated like this ((((5 o 7)o 10) o 3) o 5)
# o is chosen freely every time from * or +
def evaluate(term):
    if len(term) == 0:
        return term

    termCur = ""
    termRest = ""
    mode = 1

    for char in term:
        if mode == 1:
            if char.isdigit():
                termCur += char
            elif char == "*" or char == "+":
                termCur += char
                mode = 2 # we are now at 2nd number after + or *
        elif mode == 2:
            if char.isdigit():
                termCur += char
            elif char == "*" or char == "+":
                termRest += char
                mode = 3

        elif mode == 3:
            termRest += char
    if mode == 2: # last term left ex. 69o20
        return eval(term)

    if mode != 3: # no allowed term
        return term

    # in our example termCur = 5o7 and termRest = o10o3o5

    result = eval(termCur)
    newTerm = str(result) + termRest
    final_res = evaluate(newTerm)

    return final_res
    

def get_everything(numbers, terms=[''], Operators = ['*', '+']):
    if len(numbers) == 0:
        return terms

    collect = [] # will later be ['5+4+1', '5*4+1', ...]

    for term in terms:
        for operator in Operators:
            if len(numbers) == 1:
                operator = ""
            newTerm = term + str(numbers[0]) + str(operator)
            collect.append(newTerm)
            continue
    new_numbers = numbers[1:]
    everything = get_everything(new_numbers, collect, Operators)
    return everything
    

def findValidEquation(equation:Equation, part=1):

    result = equation.result
    numbers = equation.numbers
    if part == 1:
        terms = get_everything(numbers)
    else:
        terms = get_everything(numbers, Operators=['*', '+', ''])
    for term in terms:
        eval_result = evaluate(term)
        if result == eval_result:
            return True
    return False



                    


def main():
    valid_equations = []
    bad_equations = []
    equations = getInput()
    for equation in equations:
        if findValidEquation(equation):
            valid_equations.append(equation)
        else: 
            bad_equations.append(equation)
    total = 0
    for equation in valid_equations:
        total += equation.result
    print (total)

    ## Part 2
    ## Not recommended for use, runtime is horrrible
    for equation in bad_equations:
        if findValidEquation(equation, 2):
            total += equation.result

    print(total)
    return


if __name__ == "__main__":
    main()