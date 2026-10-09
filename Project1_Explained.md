COMP 163 – Project 1: Character Creator & Save/Load System
Name: Arielle Gerald
Date: 10/29/2025

My RPG world takes place in Emerald City, a fantasy realm where heroes begin their journeys as one of four classes — Warrior, Mage, Rogue, or Cleric. Each class represents a unique playstyle: the Warrior is strong and resilient, the Mage focuses on high magic power, the Rogue blends agility and cunning, and the Cleric balances healing and endurance. This program serves as the foundation for a larger text-based RPG, focusing on character creation, stat calculation, leveling, and file-based save/load functionality.

For stat design, I used simple linear formulas that scale with level. For example, Warriors gain high strength and health, Mages gain high magic, Rogues are balanced, and Clerics have strong health and magic. I chose this approach because it’s easy to understand, balanced across classes, and expandable for future features.

Unique features include a dynamic stat system that changes by class, a save/load mechanism that stores character data in a readable text file, and a level-up function that automatically updates stats as characters grow. The code is modular, making it easy to add future systems like battles or inventory management.

AI Usage: This entire project (including the README) was created with assistance from ChatGPT. All code was reviewed and tested by me to ensure understanding and correctness.

How to Run: Save the file as character_creator.py and run it using python character_creator.py. The program creates a character, displays its stats, and saves it to a text file (e.g., lyra.txt). You can reload the character later or modify the file to test loading and leveling functionality.