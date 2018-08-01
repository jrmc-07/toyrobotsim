import unittest
from robsim import Robot

class TestToyRobot(unittest.TestCase):

    def assertEqualCoordinates(self,rb,x,y,f):
        self.assertEqual(rb.x, x)
        self.assertEqual(rb.y, y)
        self.assertEqual(rb.f, f)

    def test_move(self):
        rb = Robot()
        self.assertEqualCoordinates(rb,0,0,1)
        rb.move()
        self.assertEqualCoordinates(rb,0,1,1)

    def test_rotateClockwise(self):
        rb = Robot()
        self.assertEqualCoordinates(rb,0,0,1)
        rb.rotate(1)
        self.assertEqualCoordinates(rb,0,0,2)
        rb.rotate(1)
        self.assertEqualCoordinates(rb,0,0,4)
        rb.rotate(1)
        self.assertEqualCoordinates(rb,0,0,8)
        rb.rotate(1)
        self.assertEqualCoordinates(rb,0,0,1)

    def test_rotateCounterClockwise(self):
        rb = Robot()
        self.assertEqualCoordinates(rb,0,0,1)
        rb.rotate(0)
        self.assertEqualCoordinates(rb,0,0,8)
        rb.rotate(0)
        self.assertEqualCoordinates(rb,0,0,4)
        rb.rotate(0)
        self.assertEqualCoordinates(rb,0,0,2)
        rb.rotate(0)
        self.assertEqualCoordinates(rb,0,0,1)

    def test_moveIgnored(self):
        rb = Robot()
        rb.rotate(0)
        rb.move()
        self.assertEqualCoordinates(rb,0,0,8)
        rb.rotate(0)
        rb.move()
        self.assertEqualCoordinates(rb,0,0,4)

    def test_setCoords(self):
        rb = Robot()
        self.assertEqualCoordinates(rb,0,0,1)
        rb.setCoordinates(1,1)
        self.assertEqualCoordinates(rb,1,1,1)
        rb.setCoordinates(4,4)
        self.assertEqualCoordinates(rb,4,4,1)
        rb.setCoordinates(2,2)
        self.assertEqualCoordinates(rb,2,2,1)

    def test_setDir(self):
        rb = Robot()
        self.assertEqualCoordinates(rb,0,0,1)
        rb.setDir('NORTH')
        self.assertEqualCoordinates(rb,0,0,1)
        rb.setDir('EAST')
        self.assertEqualCoordinates(rb,0,0,2)
        rb.setDir('SOUTH')
        self.assertEqualCoordinates(rb,0,0,4)
        rb.setDir('WEST')
        self.assertEqualCoordinates(rb,0,0,8)
        rb.setDir('NORTH')
        self.assertEqualCoordinates(rb,0,0,1)
        rb.setDir('SOUTH')
        self.assertEqualCoordinates(rb,0,0,4)

    def test_invalidCoords(self):
        rb = Robot()
        rb.setCoordinates(5,5)
        self.assertEqualCoordinates(rb,0,0,1)
        rb.setCoordinates(-1,0)
        self.assertEqualCoordinates(rb,0,0,1)

    def test_invalidDir(self):
        rb = Robot()
        rb.setDir('a')
        self.assertEqualCoordinates(rb,0,0,1)
        rb.setDir('b')
        self.assertEqualCoordinates(rb,0,0,1)

    def test_moveExceedMap(self):
        rb = Robot()
        rb.rotate(0)
        rb.move()
        self.assertEqualCoordinates(rb,0,0,8)
        rb.rotate(0)
        rb.move()
        self.assertEqualCoordinates(rb,0,0,4)

    def test_moveAround(self):
        rb = Robot()
        rb.move()
        rb.move()
        rb.move()
        rb.move()
        rb.move()
        self.assertEqualCoordinates(rb,0,4,1)
        rb.rotate(1)
        rb.move()
        rb.move()
        rb.move()
        rb.move()
        rb.move()
        self.assertEqualCoordinates(rb,4,4,2)
        rb.rotate(1)
        rb.move()
        rb.move()
        rb.move()
        rb.move()
        rb.move()
        self.assertEqualCoordinates(rb,4,0,4)
        rb.rotate(1)
        rb.move()
        rb.move()
        rb.move()
        rb.move()
        rb.move()
        self.assertEqualCoordinates(rb,0,0,8)

    def test_spectrumExample1(self):
        rb = Robot()
        rb.move()
        self.assertEqualCoordinates(rb,0,1,1)

    def test_spectrumExample2(self):
        rb = Robot()
        rb.setDir('EAST')
        rb.setCoordinates(1,2)
        rb.move()
        rb.move()
        rb.rotate(0)
        rb.move()
        self.assertEqualCoordinates(rb,3,3,1)

    def test_spectrumExample3(self):
        rb = Robot()
        rb.rotate(0)
        rb.move()
        rb.move()
        rb.move()
        rb.rotate(1)
        rb.move()
        self.assertEqualCoordinates(rb,0,1,1)

if __name__ == '__main__':
    unittest.main()
