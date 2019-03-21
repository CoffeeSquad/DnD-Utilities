import random

# First we generate race so we can base the name off of the character's race
race = random.choice([f for f in open("config/npc/races.txt").read().splitlines()])
name = random.choice([f for f in open("config/npc/names_{}.txt".format(race)).read().splitlines()])

# Now we generate other random info
age = random.choice([f for f in open("config/npc/ages.txt").read().splitlines()])
occupation = random.choice([f for f in open("config/npc/occupations.txt").read().splitlines()])
appearance = random.choice([f for f in open("config/npc/appearances.txt").read().splitlines()])
talent = random.choice([f for f in open("config/npc/talents.txt").read().splitlines()])
behavior = random.choice([f for f in open("config/npc/behaviors.txt").read().splitlines()])
mannerism = random.choice([f for f in open("config/npc/mannerisms.txt").read().splitlines()])
ideal = random.choice([f for f in open("config/npc/ideals.txt").read().splitlines()])
bond = random.choice([f for f in open("config/npc/bonds.txt").read().splitlines()])
flaw = random.choice([f for f in open("config/npc/flaws.txt").read().splitlines()])

# Write file to "npcs" folder using our randomly selected options
npc_file = open("npcs/{}-{}.txt".format(name, occupation), "w")
npc_file.write("Name: {}\nRace: {}\nAge: {}\nAppearance: {}\n\nOccupation: {}\nTalent: {}\nMannerisms: {}\nBehavior: {}\n\nIdeal: {}\nBond: {}\nFlaw: {}\n".format(name, race.capitalize(), age, appearance, occupation, talent, mannerism, behavior, ideal, bond, flaw))
