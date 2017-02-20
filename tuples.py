# Any array is great. But it's changeable! What if you wanted something that wasn't
# changeable to keep programmers from breaking your code or you just wanted to be functional

a_tuple = (1,3,8)
# print a_tuple;
# print a_tuple[2];
# a_tuple[2] = 5;

# loop through tuples the same way you do lists
for number in a_tuple:
	print number;

teams = ('falcons', 'hawks', 'atl_united', 'silverbacks');
for team in teams:
	if team == 'hawks':
		print 'Go Hawks!';
	else:
		print "It's Basketball season";

team_a = "Falcons";
print team_a == "Falcons";

# OR and AND work the same way, just ()
team_b = "Braves";
if team_a == "Falcons" and team_b == "Braves":
	print "Hooray!";

cond1 = team_a == "Falcons"
cond2 = team_b == "Braves"
if cond1 and cond2:
	print "HAYYYYYY";

for team in teams:
	if team == 'hawks':
		print "Go Hawks!";
	elif team == "falcons":
		print "Sad Super Bowel";

# message = raw_input("Please enter your name");
# height = raw_input("In inches, how tall are you?\n");
# if(int(height) >= 42):
# 	print "You are tall enough to go on the Batman roller coaster";
# else:
# 	print "Maybe try the kiddle coaster";

# While loop
current = 1;
# while current < 10:
# 	print current;
# 	current+=1;

answer = "play";
while answer != "quit":
	answer = raw_input("Say quit to stop the game!\n");

