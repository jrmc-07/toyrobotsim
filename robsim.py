import math

class Robot:

    def __init__(self, x=0, y=0, f=0x0001, dim_x=5, dim_y=5):
        self.x = x
        self.y = y
        self.f = f
        self.max_x = dim_x - 1
        self.max_y = dim_y - 1

    @staticmethod
    def rotateLeft(num, max=8):
        lmb = (max & num)
        return (num << 1) if lmb == 0 else ((num << 1) | (lmb>>int(math.log(lmb,2)))) & ~(max << 1)

    @staticmethod
    def rotateRight(num, max=8):
        rmb = (1 & num)
        return (num >> 1) if rmb == 0 else ((num >> 1) | (rmb << int(math.log(max,2))))

    def move(self):
        if self.f == 1: # f = 0001 == North
            if self.y + 1 <= self.max_y:
                self.setCoordinates(self.x, self.y + 1)
        elif self.f == 2: # f = 0010 == East
            if self.x + 1 <= self.max_x:
                self.setCoordinates(self.x + 1, self.y)
        elif self.f == 4: # f = 0100 == South
            if self.y - 1 >= 0:
                self.setCoordinates(self.x, self.y - 1)
        elif self.f == 8: # f = 1000 == West
            if self.x - 1 >= 0:
                self.setCoordinates(self.x - 1, self.y)

    def rotate(self, dir): # 1 - right; 0 - left
        self.f = self.rotateRight(self.f) if dir == 0 else self.rotateLeft(self.f) # rotate bits

    def getDirValueText(self, val):
        if val == 1:
            return 'NORTH'
        elif val == 2:
            return 'EAST'
        elif val == 4:
            return 'SOUTH'
        elif val == 8:
            return 'WEST'

    def getDirTextValue(self, txt):
        if txt == 'NORTH':
            return 1
        elif txt == 'EAST':
            return 2
        elif txt == 'SOUTH':
            return 4
        elif txt == 'WEST':
            return 8
        else:
            return 0

    def setDir(self, dir):
        dirTextValue = self.getDirTextValue(dir)
        f = self.f if dirTextValue == 0 else dirTextValue
        self.f = f

    def setCoordinates(self, x, y):
        if x <= self.max_x and x >= 0:
            if y <= self.max_y and y >= 0:
                self.x = x
                self.y = y
                return
        print("Invalid coordinates. 0 <= x <= %d, 0 <= y <= %d" % (self.max_x, self.max_y))

    def report(self):
        print("Output: %s,%s,%s" % (self.x, self.y, self.getDirValueText(self.f)))


class RobotController:
    def __init__(self):
        self.robot = Robot()

    def printHelp(self):
        print("""Toy Robot controls:
            PLACE <X,Y,F> : Initializes the position of the robot 
                            X - Position in the x-axis
                            Y - Position in the y-axis
                            F - Direction where the robot should face
                                (NORTH, EAST, SOUTH, WEST)
            MOVE          : Moves the robot 1 step forward in its current direction
            LEFT          : Rotate the robot 90 degrees to its left
            RIGHT         : Rotate the robot 90 degrees to its right
            REPORT        : Display the current position of the robot and where it is facing
            HELP          : Display help text
            """)

    def start(self):
        self.printHelp()
        print("Start")
        while True:
            command = input(">>")
            command = command.split()
            if len(command) == 2 and command[0] == "PLACE":
                x,y,dir = command[1].split(',')
                self.robot.setCoordinates(int(x),int(y))
                self.robot.setDir(dir)
            elif len(command) == 1:
                command = command[0]
                if command == "MOVE":
                    self.robot.move()
                elif command == "LEFT":
                    self.robot.rotate(0)
                elif command == "RIGHT":
                    self.robot.rotate(1)
                elif command == "REPORT":
                    self.robot.report()
                elif command == "HELP":
                    self.printHelp()
                else:
                    print("Invalid command. Check HELP for commands")


if __name__ == '__main__':
    rc = RobotController()
    rc.start()

