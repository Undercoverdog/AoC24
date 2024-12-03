def to_array(line):
    output = []
    temp = ""
    for i in range(0, len(line)):
        if line[i].isdigit():
            temp += line[i]
        else:
            output.append(int(temp))
            temp = ""

    if temp.isdigit(): output.append(int(temp))
    return output

