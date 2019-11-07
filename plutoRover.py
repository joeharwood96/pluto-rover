class plutoRover:
    def __init__(self, position, command, grid):
        self.position = position
        self.command = command
        self.grid = grid

    def moveForward(self, direction, x, y):
        if direction == "N":
            y += 1
        elif direction == "S":
            y -= 1
        elif direction == "E":
            x += 1
        else:
            x -= 1

        return x, y, direction

    # def moveBackward(self, direction, x, y):


    # def rotateLeft(self, direction):
    

    # def rotateRight(self, direction):
    

    # def checkEdges(self, grid, finalPosition):
    
         
    def main(self):
        currentPos = self.position

        if len(currentPos) == 3:
            currentDir = currentPos[2]
            x = currentPos[0]
            y = currentPos[1]
        else:
            return print("No position found")

        return self.moveForward(currentDir, x, y)
            

print(plutoRover([0, 0, "E"], "F", [100, 100]).main())