class Guard:
    def __init__(self, canvas, facingIcon=None, posHeight=None, posWidth=None):
        self.facingArray = ["^", ">", "v", "<"]
        self.visited = []

        if posHeight == None or posWidth == None:
            for i in range(0, len(canvas)):
                for j in range(0, len(canvas[i])):
                    if canvas[i][j] in self.facingArray:
                        facingIcon = canvas[i][j]
                        posHeight = i
                        posWidth = j

        self.height = posHeight
        self.width = posWidth
        self.facingIcon = facingIcon
        self.facingIndex = find(self.facingArray, facingIcon)
        self.canvas = canvas
        self.add_position()

    def add_position(self):
        # Append the array [self.posWidth, self.posHeight] to self.visited
        pos = [self.width, self.height]
        
        ## debug
        # Convert the row (string) into a list of characters
        row = list(self.canvas[self.height])
        
        # Modify the specific position in the row
        if self.canvas[self.height][self.width] == ".":
            str = "*"
        elif self.canvas[self.height][self.width] == "*":
            strarr = ["▲", "▶", "▼", "◀"]
            str = strarr[self.facingIndex]
            #str = "x"
        elif self.canvas[self.height][self.width] == "x":
            str = "y"
        else:
            strarr = ["▲", "▶", "▼", "◀"]
            str = strarr[self.facingIndex]
  
        row[self.width] = str
        
        # Convert the list back into a string
        self.canvas[self.height] = "".join(row)
        ## end debug
        

        if pos in self.visited: 
            pass
        else:
            self.visited.append(pos)

# seems to work!
    def update_facing(self, facingIcon=None, facingIndex=None):
        if facingIcon != None:
            self.facingIndex = find(self.facingArray, facingIcon)
            self.facingIcon = self.facingArray[self.facingIndex]
        elif facingIndex != None:
            self.facingIcon = self.facingArray[facingIndex]
            self.facingIndex = facingIndex
        else:
            print("Error! No facing params")


# seems to work!
    def turn_90_deg(self):
        new_direction = self.facingArray[(self.facingIndex+1)%len(self.facingArray)]
        self.update_facing(facingIcon=new_direction)
# seems to work-ish
    def has_obstacle(self):
            width = self.width
            height = self.height
            # ["^", ">", "v", "<"]
            match self.facingIndex:
                case 0:
                    height -= 1
                case 1:
                    width += 1
                case 2:
                    height += 1
                case 3:
                    width -= 1
            try:
                if height<0: height=len(self.canvas)+10
                if width<0: width=len(self.canvas[height])+10
                if self.canvas[height][width] == "#":
                    return True
                else:
                    return False
            except IndexError as e:
                print("Done!")
                print(len(self.visited))
                raise StopIteration
                return False
#
    def move_forward(self):
        # ["^", ">", "v", "<"]

        match self.facingIndex:
            case 0:
                self.height -= 1
            case 1:
                self.width += 1
            case 2:
                self.height += 1
            case 3:
                self.width -= 1


    def move(self):
        while self.has_obstacle():
            self.turn_90_deg()
        self.move_forward()
        self.add_position()

def find(arr, var):
    for i in range(0, len(arr)):
        if arr[i] == var:
            return i
    return -1

def get_canvas():
    with open("input", "r") as f:
        canvas = []
        for line in f:
            canvas.append(line.strip())
    return canvas

def main():
    canvas = get_canvas() # canvas[height, width]
    guard = Guard(canvas)
    try:
        while(True):
            guard.move()
            if guard.height < 0 or guard.height >= len(canvas) or guard.width < 0 or guard.width >= len(canvas[0]):
                break
    except StopIteration:
        print("Out of Bounds, Program terminated.")
    

if __name__ == "__main__":
    main()