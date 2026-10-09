"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Arielle Gerald
Date: 10/23/2025

AI Usage: [Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function

AI Usage:
    This entire project was created with assistance from ChatGPT.
    AI assistance included:
        - Generating initial code structure and function templates
        - Writing logic for character creation, stat calculation, saving, and loading
        - Implementing file I/O operations with basic error handling
        - Writing display formatting and level-up logic
        - Adding explanatory comments and docstrings
    All code was reviewed and tested by the student to ensure understanding and correctness.
"""
import os # Used for file path checking and directory validation

# FUNCTION: create_character
# PURPOSE: Creates a new character with stats and starting gold
# INPUTS: name (str), character_class (str)
# RETURNS: dictionary containing character data

def create_character(name, character_class):
    level = 1 # New characters always start at level 1
    strength, magic, health = calculate_stats(character_class, level)

# Assign starting gold based on class
    if character_class.lower() == "warrior":
        gold = 120
    elif character_class.lower() == "mage":
        gold = 90
    elif character_class.lower() == "rogue":
        gold = 110
    elif character_class.lower() == "cleric":
        gold = 100
    else:
        gold = 100 # Default gold if class not recognized

 # Store all character data in a dictionary
    character = {}
    character["name"] = name
    character["class"] = character_class
    character["level"] = level
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health
    character["gold"] = gold

    return character



"""
    Creates a new character dictionary with calculated stats
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold
    Example:
    char = create_character("Aria", "Mage")
    # Should return: {"name": "Aria", "class": "Mage", "level": 1, "strength": 5, "magic": 15, "health": 80, "gold": 100}
"""

    # TODO: Implement this function
    # Remember to use calculate_stats() function for stat calculation


"""
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)
    
    Design your own formulas! Ideas:
    - Warriors: High strength, low magic, high health
    - Mages: Low strength, high magic, medium health  
    - Rogues: Medium strength, medium magic, low health
    - Clerics: Medium strength, high magic, high health
"""

# FUNCTION: calculate_stats
# PURPOSE: Calculates character stats based on class and level
# INPUTS: character_class (str), level (int)
# RETURNS: tuple (strength, magic, health)

def calculate_stats(character_class, level):
    character_class = character_class.lower()

# Different stat growth per class
    if character_class == "warrior":
        strength = 12 + 4 * level
        magic = 3 + 1 * level
        health = 140 + 20 * level
    elif character_class == "mage":
        strength = 4 + 1 * level
        magic = 14 + 5 * level
        health = 90 + 12 * level
    elif character_class == "rogue":
        strength = 8 + 3 * level
        magic = 6 + 2 * level
        health = 100 + 10 * level
    elif character_class == "cleric":
        strength = 6 + 2 * level
        magic = 11 + 3 * level
        health = 120 + 18 * level

        # Default stats for unknown class
    else:
        strength = 7 + 2 * level
        magic = 7 + 2 * level
        health = 100 + 15 * level

    return strength, magic, health

# FUNCTION: save_character
# PURPOSE: Saves character data to a text file
# INPUTS: character (dict), filename (str)
# RETURNS: True if successful, False otherwise

def save_character(character, filename):
    if character is None:
        return False

    # Get the directory from the filename
    directory = os.path.dirname(filename)

    # If there's a directory path and it does not exist, return False
    if directory != "" and not os.path.exists(directory):
        return False

    # Otherwise, write the file
    file = open(filename, "w")
    file.write("Character Name: " + character["name"] + "\n")
    file.write("Class: " + character["class"] + "\n")
    file.write("Level: " + str(character["level"]) + "\n")
    file.write("Strength: " + str(character["strength"]) + "\n")
    file.write("Magic: " + str(character["magic"]) + "\n")
    file.write("Health: " + str(character["health"]) + "\n")
    file.write("Gold: " + str(character["gold"]) + "\n")
    file.close()

    return True


"""
    Saves character to text file in specific format
    Returns: True if successful, False if error occurred
    
    Required file format:
    Character Name: [name]
    Class: [class]
    Level: [level]
    Strength: [strength]
    Magic: [magic]
    Health: [health]
    Gold: [gold]
"""
    # TODO: Implement this function
    # Remember to handle file errors gracefully

# FUNCTION: load_character
# PURPOSE: Loads a saved character file into a dictionary
# INPUTS: filename (str)
# RETURNS: dictionary if successful, None if file not found or invalid

def load_character(filename):
    if not os.path.exists(filename):
        return None # File doesn’t exist

    file = open(filename, "r") # Read all lines from the file
    lines = file.readlines()
    file.close()

    character = {}
    for line in lines:
        parts = line.strip().split(": ")
        if len(parts) == 2:
            key = parts[0]
            value = parts[1]
            if key == "Character Name":
                character["name"] = value
            elif key == "Class":
                character["class"] = value
            elif key == "Level":
                character["level"] = int(value)
            elif key == "Strength":
                character["strength"] = int(value)
            elif key == "Magic":
                character["magic"] = int(value)
            elif key == "Health":
                character["health"] = int(value)
            elif key == "Gold":
                character["gold"] = int(value)

    return character
"""
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
"""
    # TODO: Implement this function
    # Remember to handle file not found errors

# FUNCTION: display_character
# PURPOSE: Displays character stats neatly formatted
# INPUTS: character (dict)
# RETURNS: None (prints to console)

def display_character(character):
    print("=== CHARACTER SHEET ===")
    print("Name: " + character["name"])
    print("Class: " + character["class"])
    print("Level: " + str(character["level"]))
    print("Strength: " + str(character["strength"]))
    print("Magic: " + str(character["magic"]))
    print("Health: " + str(character["health"]))
    print("Gold: " + str(character["gold"]))
    print("========================")
    print("")
"""
    Prints formatted character sheet
    Returns: None (prints to console)
    
    Example output:
    === CHARACTER SHEET ===
    Name: Aria
    Class: Mage
    Level: 1
    Strength: 5
    Magic: 15
    Health: 80
    Gold: 100
"""
    # TODO: Implement this function


# FUNCTION: level_up
# PURPOSE: Increases level and recalculates stats
# INPUTS: character (dict)
# RETURNS: None

def level_up(character):

    character["level"] = character["level"] + 1 # Increase level by one

    # Recalculate stats based on new level
    strength, magic, health = calculate_stats(character["class"], character["level"])
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health

     # Announce the level-up
    print(character["name"] + " has leveled up to level " + str(character["level"]) + "!")
"""
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
"""
    # TODO: Implement this function
    # Remember to recalculate stats for the new level



# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")

    hero = create_character("Lyra the Swift", "Rogue")
    display_character(hero)

    sucess = save_character(hero, "lyra.txt")
    if sucess == True:
        print("Character saved successfully!")

    # Example usage:
    # char = create_character("TestHero", "Warrior")
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")
