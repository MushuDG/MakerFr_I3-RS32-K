################################################################################
# General Information
################################################################################
# Author:               MushuDG
# Project:              MakerFr_I3-RS32-K
# File:                 pins.py
# Creation Date:        Aug. 31, 2024
# Modification Date:    Aug. 31, 2024
# Description:          This script parses a Klipper printer configuration file
#                       to identify and list all the GPIO pins used in the setup.
#                       It reads the configuration file, searches for pin 
#                       definitions (e.g., PA1, PB2), and then outputs the pins 
#                       in a sorted order, ensuring numerical sorting within 
#                       each pin group (e.g., PA1, PA2, PA10). This is useful 
#                       for verifying pin assignments and ensuring that all 
#                       necessary pins are accounted for in a 3D printer setup.
################################################################################

########################################
# Import
########################################
import re

########################################
# Functions
########################################
def sort_pins(pins):
    def pin_key(pin):
        # Extracts the letter and number from the pin, e.g., ("PA", 1) for "PA1"
        match = re.match(r"([A-Z]+)(\d+)", pin)
        return match.group(1), int(match.group(2))

    # Sorts the pins using the pin_key function to ensure proper numerical order
    return sorted(pins, key=pin_key)

def list_used_pins(config_file_path):
    # Opens the configuration file and reads all lines
    with open(config_file_path, 'r') as file:
        lines = file.readlines()

    # Compiles a regular expression to match pins like PA1, PB2, etc.
    pin_pattern = re.compile(r'pin:\s*(PA\d+|PB\d+|PC\d+|PD\d+|PE\d+|PF\d+|PG\d+)')
    used_pins = set()

    # Iterates through each line and searches for pin matches
    for line in lines:
        match = pin_pattern.search(line)
        if match:
            # Adds the matched pin to the set of used pins
            used_pins.add(match.group(1))

    # Returns the sorted list of used pins
    return sort_pins(used_pins)

########################################
# Main
########################################
if __name__ == "__main__":
    # Path to the printer configuration file
    config_file = "../Klipper_Config/TMC2209/TFT35-SPI/printer.cfg"
    pins = list_used_pins(config_file)
    print("Pins used in configuration:")
    # Prints each used pin in the sorted order
    for pin in pins:
        print(pin)
