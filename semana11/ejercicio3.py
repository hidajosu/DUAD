class Head:
    def __init__(self):
        self.eyes = 2
        self.ears = 2
        self.nose = 1
        self.mouth = 1

class Torso:
    def __init__(self):
        self.heart = 1
        self.lungs = 2
        self.stomach = 1

class Arm:
    def __init__(self, side):
        self.side = side  
        self.hand = Hand()

class Hand:
    def __init__(self):
        self.fingers = 5

class Leg:
    def __init__(self, side):
        self.side = side  
        self.feet = Feet()

class Feet:
    def __init__(self):
        self.toes = 5

class Human:
    def __init__(self):
        self.head = Head()
        self.torso = Torso()
        self.left_arm = Arm("left")
        self.right_arm = Arm("right")
        self.left_leg = Leg("left")
        self.right_leg = Leg("right")
    
    def my_full_body(self):
        print("The human has ",human.head.eyes,"eyes")
        print("The human's left hand has ",human.left_arm.hand.fingers,"fingers.")
        print("The human's right foot has ",human.right_leg.feet.toes," toes")


human = Human()
human.my_full_body()


