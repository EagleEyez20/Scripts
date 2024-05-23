import random

feet_in_mile = 5280
meters_in_kilometer = 1000
beatles = ["John", "Paul", "George", "Ringo"]


def get_file_contents(filename):
    return filename[filename.index(".") + 1:]

def roll_dice(num):
    return random.randint(1, num)
