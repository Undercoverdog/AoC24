
 
def get_real_instructions(pInput):
    output=[]
    i=0
    pInput += " "*10
    while i<len(pInput)-10:
        if pInput[i:i+4] == "mul(":
            newterm = "mul("
            i += 4
            while(True):
                if pInput[i].isdigit():
                    newterm += pInput[i]
                    i+=1
                else:
                    break

            if pInput[i] == ",":
                newterm += pInput[i]
                i+=1
            else: continue

            while(True):
                if pInput[i].isdigit():
                    newterm += pInput[i]
                    i+=1
                else:
                    break
            if pInput[i] == ")":
                newterm += pInput[i]
                i+=1
            else: continue

            output.append(newterm)
        else:
            i+=1
            continue
    return output


def evaluate(pIn):
    pIn = pIn[4:]
    pIn = pIn[:len(pIn)-1]
    pIn = pIn.replace(",", "*")
    
    return eval(pIn)

def strip_dont(pIn):
    i=0
    output = ""
    do = True
    while i<len(pIn)-5:

        if pIn[i:i+5] == "don\'t":
            do = False
            i+=5
        elif pIn[i:i+2] == "do":
            do = True
            i+=2
        if do:
            output+=pIn[i]
        i+=1

    while i<len(pIn):
        if do: output+=pIn[i]
        i+=1
    
    return output





def main():
    with open("input", "r") as f:
        read = f.read()

        ## Part 1
        real = get_real_instructions(read)

        ret = 0
        for i in real:
            ret += evaluate(i)
        print(ret)


        ## Part 2
        ins = strip_dont(read)
        real = get_real_instructions(ins)

        ret = 0
        for i in real:
            ret += evaluate(i)
        print(ret)



if __name__ == "__main__":
    main()