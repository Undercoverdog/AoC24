
def getlines():
    lines = []
    with open("input", "r") as f:
        for line in f:
            lines.append(line[:-1])

    return lines

def part1(lines):
    counter = 0
    
    for line in range(0,len(lines)):
        for column in range(0, len(lines[line])):
            horizontal = ""
            vertical = ""
            diagr = ""
            diagl = ""
            for a in range(0,4):

                if column+a < len(lines[line]): horizontal += lines[line][column+a]

                if line+a < len(lines): vertical += lines[line+a][column]
                

                if line+a < len(lines) and column+a < len(lines[line]): diagr += lines[line+a][column+a]
                if line+a < len(lines) and column-a >= 0: diagl += lines[line+a][column-a]

            if horizontal == "XMAS" or horizontal == "SAMX": counter+=1
            if vertical == "XMAS" or vertical == "SAMX": counter+=1
            if diagr == "XMAS" or diagr == "SAMX": counter+=1
            if diagl == "XMAS" or diagl == "SAMX": counter+=1
            if horizontal == "XMXM": 
                pass


    return counter




def part2(array):
    counter = 0
    for line in range(0,len(array)-2):
        for column in range(0,len(array[line])-2):
            if array[line+1][column+1] == "A":
                if (array[line][column] == "M" and array[line+2][column+2] == "S") or (array[line][column] == "S" and array[line+2][column+2] == "M"):
                    if (array[line][column+2] == "M" and array[line+2][column] == "S") or (array[line][column+2] == "S" and array[line+2][column] == "M"):
                        counter+=1

    return counter



def main():
    lines = getlines()
    print(part1(lines))
    print(part2(lines))






    






if __name__ == "__main__":
    main()