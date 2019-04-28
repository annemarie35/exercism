import random
import string

class Robot(object):
    def __init__(self):
        self.generate_name()

    def generate_name(self):
        random.seed()
        letters = random.sample(string.ascii_uppercase, 2)
        numbers = random.sample(string.digits,  3)
        robot_name = ''.join(map(str, letters + numbers))
        self.name = robot_name

    def reset(self):
        self.generate_name()
