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

    def rotateLeft(self, direction):
        if direction == "N":
            direction = "W"
        elif direction == "S":
            direction = "E"
        elif direction == "E":
            direction = "N"
        else:
            direction = "S"

        return direction
    

    def rotateRight(self, direction):
        if direction == "N":
            direction = "E"
        elif direction == "S":
            direction = "W"
        elif direction == "E":
            direction = "S"
        else:
            direction = "N"

        return direction
    

    # def checkEdges(self, grid, finalPosition):


    def auth(self, command, direction, x, y, pointer):
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

        error = ""
        finalPosition = ()

        while pointer < len(command):
            if direction is not None and command is not None:
                if direction in direc and command[pointer] in com:
                    if command[pointer] == "F":
                        x, y, direction =  self.moveForward(direction, x, y)
                        finalPosition = (x, y, direction)
                        pointer += 1
                        self.auth(command, direction, x, y, pointer)
                    elif command[pointer] == "B":
                        x, y, direction = self.moveBackward(direction, x, y)
                        finalPosition = (x, y, direction)
                        pointer += 1
                        self.auth(command, direction, x, y, pointer)
                    elif command[pointer] == "L":
                        direction = self.rotateLeft(direction)
                        finalPosition = (x, y, direction)
                        pointer += 1
                        self.auth(command, direction, x, y, pointer)
                    else:
                        direction = self.rotateRight(direction)
                        finalPosition = (x, y, direction)
                        pointer += 1
                        self.auth(command, direction, x, y, pointer)
                elif direction not in direc:
                    error = "Sorry, direction not found: " + direction 
                else:
                    error = "Sorry, command not found: " + command[pointer]

        if error:
            return error
        else:
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

        command = list(map(str, command))

        return self.auth(command, currentDir, x, y, 0)
            

print(plutoRover([0, 0, "N"], "FFRFF", [100, 100]).main())