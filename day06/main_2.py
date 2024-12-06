counter = 0

class Guard:
    def __init__(self, canvas, facingIcon=None, posHeight=None, posWidth=None):
        self.facingArray = ["^", ">", "v", "<"]
        self.visited = []
        self.log = [] # what turn at which position (due to abstacle)

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
            global counter
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
                    arr = [self.height, self.width, self.facingIndex]
                    if arr in self.log:
                        counter+=1
                        raise StopIteration
                    else:
                        self.log.append(arr)
                    return True
                else:
                    return False
            except IndexError as e:
                #print("Done!")
                #print(len(self.visited))
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
    backupCanvas = get_canvas() # canvas[height, width]
    canvas = backupCanvas[:]
    guard = Guard(canvas)
    posHeight = 0
    posWidth = 0
    facingIcon = ""
    for i in range(0, len(canvas)):
        for j in range(0, len(canvas[i])):
            if canvas[i][j] in guard.facingArray:
                facingIcon = canvas[i][j]
                posHeight = i
                posWidth = j

    for line in range(0, len(guard.canvas)):
        for char in range(0, len(guard.canvas[line])):
            restore = canvas[line]
            
            # Convert the string at canvas[line] to a list
            canvas_line = list(canvas[line])

            # Modify the character
            canvas_line[char] = "#"

            # Convert the list back to a string
            canvas[line] = ''.join(canvas_line)

            try:
                while(True):
                    guard.move()
                    if guard.height < 0 or guard.height >= len(canvas) or guard.width < 0 or guard.width >= len(canvas[0]):
                        break
            except StopIteration:
                canvas[line] = restore
                break
            finally:
                # reset everything
                guard.log = []
                guard.visited = []
                guard.canvas[line] = restore
                guard.height = posHeight
                guard.width = posWidth
                guard.update_facing(facingIcon=facingIcon)
                continue



    print(counter)
    

if __name__ == "__main__":
    main()