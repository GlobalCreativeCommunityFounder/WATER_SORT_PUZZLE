"""
This file contains code for the game "Water Sort Puzzle".
Author: GlobalCreativeCommunityFounder
"""

# Importing necessary libraries
import copy
import sys
import os
import random


# Creating necessary functions to be used throughout the game.


def clear():
    # type: () -> None
    if sys.platform.startswith('win'):
        os.system('cls')  # For Windows System
    else:
        os.system('clear')  # For Linux System


def all_bottles_sorted(bottles: list) -> bool:
    if len(bottles) == 0:
        return True
    else:
        for bottle in bottles:
            if not bottle.sorted():
                return False

        return True


# Creating necessary classes


class Bottle:
    """
    This class contains attributes of a water bottle.
    """

    BOTTLE_CAPACITY: int = 5

    def __init__(self, water_levels=None):
        # type: (list) -> None
        if water_levels is None:
            water_levels = []
        self.__water_levels: list = water_levels

    def __str__(self):
        # type: () -> str
        res: str = ""  # initial value
        for i in range(self.BOTTLE_CAPACITY - 1, -1, -1):
            if i >= len(self.__water_levels):
                res += "|        |\n"
            else:
                curr_water_level: Water = self.__water_levels[i]
                if len(str(curr_water_level)) == 3:
                    res += "|   " + str(curr_water_level) + "  |\n"
                elif len(str(curr_water_level)) == 4:
                    res += "|  " + str(curr_water_level) + "  |\n"
                elif len(str(curr_water_level)) == 5:
                    res += "|  " + str(curr_water_level) + " |\n"
                else:
                    res += "| " + str(curr_water_level) + " |\n"

        return res

    def add_water_level(self, water):
        # type: (Water) -> bool
        if len(self.__water_levels) < self.BOTTLE_CAPACITY:
            self.__water_levels.append(water)
            return True
        return False

    def pour_water(self, other_bottle):
        # type: (Bottle) -> bool
        self_last: Water = self.get_last_water_level()
        other_last: Water = other_bottle.get_last_water_level()
        if len(other_bottle.get_water_levels()) >= self.BOTTLE_CAPACITY:
            return False
        if other_last is None or self_last.colour == other_last.colour or len(other_bottle.__water_levels) == 0:
            self.__water_levels.remove(self_last)
            other_bottle.add_water_level(self_last)
            return True
        return False

    def get_last_water_level(self):
        # type: () -> Water or None
        if len(self.__water_levels) > 0:
            return self.__water_levels[len(self.__water_levels) - 1]
        else:
            return None

    def sorted(self):
        # type: () -> bool
        if len(self.__water_levels) == 0:
            return True
        else:
            curr_colour: str = self.__water_levels[0].colour
            for water in self.__water_levels:
                if water.colour != curr_colour:
                    return False

            return True

    def get_water_levels(self):
        # type: () -> list
        return self.__water_levels

    def clone(self):
        # type: () -> Bottle
        return copy.deepcopy(self)


class Water:
    """
    This class contains attributes of water
    """

    POSSIBLE_COLOURS: list = ["BLUE", "RED", "ORANGE", "GREEN", "PURPLE", "YELLOW"]

    def __init__(self, colour):
        # type: (str) -> None
        self.colour: str = colour if colour in self.POSSIBLE_COLOURS else self.POSSIBLE_COLOURS[0]

    def __str__(self):
        # type: () -> str
        return str(self.colour)

    def clone(self):
        # type: () -> Water
        return copy.deepcopy(self)


# Creating main function used to run the game.


def main():
    """
    This function is used to run the game.
    :return: None
    """

    print("Welcome to 'Water Sort Puzzle' by 'GlobalCreativeCommunityFounder'.")
    print("In this game, you are required to make sure that each water bottle only contains one colour of water.")
    print("Enter 'Y' for yes.")
    print("Enter anything else for no.")
    level: int = 1  # initial value
    continue_playing: str = input("Do you want to continue playing 'Water Sort Puzzle'? ")
    while continue_playing == "Y":
        bottles: list = []  # initial value
        number_of_bottles: int = 5 + (level // 5)
        number_of_empty_bottles: int = number_of_bottles // 5
        possible_colours: list = Water.POSSIBLE_COLOURS if number_of_bottles >= 10 else Water.POSSIBLE_COLOURS[0:4]
        for i in range(number_of_empty_bottles):
            bottles.append(Bottle([]))

        for i in range(number_of_bottles - number_of_empty_bottles):
            water_levels: list = []  # initial value
            for j in range(4):
                water_levels.append(Water(possible_colours[random.randint(0, len(possible_colours) - 1)]))

            bottles.append(Bottle(water_levels))

        while not all_bottles_sorted(bottles):
            clear()

            print("You are now at level " + str(level))
            print("Current representation of each bottle is as below.\n")
            for bottle in bottles:
                print(str(bottle) + "\n")

            bottle_from_index: int = int(input("Please enter index of water bottle you want to pour bottle from "
                                               "(1 - " + str(len(bottles)) + "): "))
            bottle_to_index: int = int(input("Please enter index of water bottle you want to pour bottle to "
                                             "(1 - " + str(len(bottles)) + "): "))
            while bottle_from_index < 1 or bottle_from_index > len(bottles) or bottle_to_index < 1 or \
                    bottle_to_index > len(bottles) or bottle_from_index == bottle_to_index:
                print("Invalid input! A different input is expected!")
                bottle_from_index = int(input("Please enter index of water bottle you want to pour bottle from "
                                              "(1 - " + str(len(bottles)) + "): "))
                bottle_to_index = int(input("Please enter index of water bottle you want to pour bottle to "
                                            "(1 - " + str(len(bottles)) + "): "))

            bottle_from: Bottle = bottles[bottle_from_index - 1]
            bottle_to: Bottle = bottles[bottle_to_index - 1]
            bottle_from.pour_water(bottle_to)

        print("Enter 'Y' for yes.")
        print("Enter anything else for no.")
        continue_playing = input("Do you want to continue playing 'Water Sort Puzzle'? ")
    sys.exit()


if __name__ == '__main__':
    main()
