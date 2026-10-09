"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Arielle Gerald
Date: 10/23/2025

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
import os  # Used for file path checking and directory validation


# FUNCTION: calculate_stats
# PURPOSE: Calculates character stats based on class and level
# INPUTS: character_class (str), level (int)
# RETURNS: tuple (strength, magic, health)
def calculate_stats(character_class, level):
    if not character_class:
        cls = ""
    else:
        cls = character_class.lower()

    # Different stat growth per class
    if cls == "warrior":
        strength = 12 + 4 * level
        magic = 3 + 1 * level
        health = 140 + 20 * level
    elif cls == "mage":
        strength = 4 + 1 * level
        magic = 14 + 5 * level
        health = 90 + 12 * level
    elif cls == "rogue":
        strength = 8 + 3 * level
        magic = 6 + 2 * level
        health = 100 + 10 * level
    elif cls == "cleric":
        strength = 6 + 2 * level
        magic = 11 + 3 * level
        health = 120 + 18 * level
    # Default stats for unknown class
    else:
        strength = 7 + 2 * level
        magic = 7 + 2 * level
        health = 100 + 15 * level

    return strength, magic, health


# FUNCTION: create_character
# PURPOSE: Creates a new character with stats and starting gold
# INPUTS: name (str), character_class (str)
# RETURNS: dictionary containing character data
def create_character(name, character_class):
    level = 1  # New characters always start at level 1
    strength, magic, health = calculate_stats(character_class, level)

    cls = character_class.lower() if character_class else ""

    # Assign starting gold based on class
    if cls == "warrior":
        gold = 120
    elif cls == "mage":
        gold = 100
    elif cls == "rogue":
        gold = 110
    elif cls == "cleric":
        gold = 100
    else:
        gold = 100  # Default gold if class not recognized

    # Store all character data in a dictionary
    character = {
        "name": name,
        "class": character_class,
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": gold,
    }

    return character


# FUNCTION: save_character
# PURPOSE: Saves character data to a text file
# INPUTS: character (dict), filename (str)
# RETURNS: True if successful, False otherwise
def save_character(character, filename):
    if not character or not isinstance(character, dict):
        return False

    # Check if all required keys exist
    required_keys = ["name", "class", "level", "strength", "magic", "health", "gold"]
    for key in required_keys:
        if key not in character:
            return False

    # Get the directory from the filename
    directory = os.path.dirname(filename)

    # If there's a directory path and it does not exist, try to handle gracefully or return False
    if directory != "" and not os.path.exists(directory):
        return False

    try:
        with open(filename, "w") as file:
            file.write("Character Name: " + str(character["name"]) + "\n")
            file.write("Class: " + str(character["class"]) + "\n")
            file.write("Level: " + str(character["level"]) + "\n")
            file.write("Strength: " + str(character["strength"]) + "\n")
            file.write("Magic: " + str(character["magic"]) + "\n")
            file.write("Health: " + str(character["health"]) + "\n")
            file.write("Gold: " + str(character["gold"]) + "\n")
        return True
    except Exception:
        return False


# FUNCTION: load_character
# PURPOSE: Loads a saved character file into a dictionary
# INPUTS: filename (str)
# RETURNS: dictionary if successful, None if file not found or invalid
def load_character(filename):
    if not filename or not os.path.exists(filename):
        return None  # File doesn’t exist

    character = {}
    try:
        with open(filename, "r") as file:
            lines = file.readlines()

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

        # Ensure all required 7 fields were successfully parsed
        required_keys = ["name", "class", "level", "strength", "magic", "health", "gold"]
        if not all(k in character for k in required_keys):
            return None

        return character
    except Exception:
        return None


# FUNCTION: display_character
# PURPOSE: Displays character stats neatly formatted
# INPUTS: character (dict)
# RETURNS: None (prints to console)
def display_character(character):
    if not character or not isinstance(character, dict):
        return

    print("=== CHARACTER SHEET ===")
    print("Name: " + str(character.get("name", "")))
    print("Class: " + str(character.get("class", "")))
    print("Level: " + str(character.get("level", "")))
    print("Strength: " + str(character.get("strength", "")))
    print("Magic: " + str(character.get("magic", "")))
    print("Health: " + str(character.get("health", "")))
    print("Gold: " + str(character.get("gold", "")))
    print("========================")
    print("")


# FUNCTION: level_up
# PURPOSE: Increases level and recalculates stats
# INPUTS: character (dict)
# RETURNS: None
def level_up(character):
    if not character or not isinstance(character, dict):
        return

    character["level"] = character["level"] + 1  # Increase level by one

    # Recalculate stats based on new level
    strength, magic, health = calculate_stats(character["class"], character["level"])
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health

    # Announce the level-up
    print(str(character["name"]) + " has leveled up to level " + str(character["level"]) + "!")


# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")

    hero = create_character("Lyra the Swift", "Rogue")
    display_character(hero)

    sucess = save_character(hero, "lyra.txt")
    if sucess:
        print("Character saved successfully!")