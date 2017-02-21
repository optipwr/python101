# dictionary is the fancy pyhton term for a JS object
# Must put keys (properties) in quotes
# Called Key-value pairs in python as opposed to  properties:values

zombie = {
	'speed': 10,
	'power': 6,
	'hunger': 12,
	'name': 'Zombie'
}

# print zombie['speed'];

# You can add a new key just like you do in JS. Vars are dynamic in Python!
zombie['weapon'] = 'fist';
zombie['startX'] = 200;
zombie['startY'] = 100;
# print zombie;

# Change the value of an existing key just like JS
if zombie['speed'] < 5:
	zombie['position'] = zombie['startX'] + 2;
elif zombie['speed'] < 10:
	zombie['position'] = zombie['startX'] + 4;
else:
	zombie['position'] = zombie['startX'] + 6;

# you can delete a key with del
zombie['pointless'] = "duh";
del zombie['pointless'];
# print zombie;

# store all the techs we know in a dictionary and set the value from 1-10
hero = {
	'health': 100,
	'mana': 267,
	'influence': 100,
	'name': 'Irby',
	'weight': 'Enough',
	'weapon': 'JavaScript',
	'strengths': 'JavaScript',
	'weaknesses': 'CSS',
	'spells': 'FireGas'
}

# print hero;


# for loops through dictionaries start with key (placeholder), value
# for key, value in hero.items():
# 	print key;

# just like in JS, you can put dictionaries inside of lists (objects inside of arrays)

heroes = [];
heroes.append({
	'speed': 10,
	'power': 6,
	'hunger': 123,
	'name': 'Harley'
});

heroes.append({
	'speed': 101,
	'power': 61,
	'hunger': 1231,
	'name': 'Snoopy'
});

# print heroes;

# for hero in heroes:
# 	print hero['name'];

# just like JS objects, you can assign a list to a dictionary key
heroes[0]['awards'] = ['money', 'kittnes'];
print heroes[0];