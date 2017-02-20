from random import randint;
answer = (randint(1,10));
response = 11;

while answer != response:
	response = int(raw_input("Please guess a number between 1 and 10. If you get it wrong you must keep guessing."));
