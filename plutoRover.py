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

    def moveBackward(self, direction, x, y):
        if direction == "N":
            y -= 1
        elif direction == "S":
            y += 1
        elif direction == "E":
            x -= 1
        else:
            x += 1

        return x, y, direction

    # def rotateLeft(self, direction):
    

    # def rotateRight(self, direction):
    

    # def checkEdges(self, grid, finalPosition):


    def auth(self, command, direction, x, y):
        direc = {
            "N",
            "S",
            "E",
            "W"
        }

        com = {
            "F",
            "B",
            "L",
            "R"
        }

        if direction is not None and command is not None:
            if direction in direc and command in com:
                if command == "F":
                    x, y, direction =  self.moveForward(direction, x, y)
                    finalPosition = (x, y, direction)
                elif command == "B":
                    x, y, direction = self.moveBackward(direction, x, y)
                    finalPosition = (x, y, direction)

        return finalPosition
    
         
    def main(self):
        currentPos = self.position
        command = self.command

        if len(currentPos) == 3:
            currentDir = currentPos[2]
            x = currentPos[0]
            y = currentPos[1]
        else:
            return print("No position found")

        return self.auth(command, currentDir, x, y)
            

print(plutoRover([2, 0, "E"], "B", [100, 100]).main())