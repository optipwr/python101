# Using a for loop and the range function, print out the numbers between 1 and 10 inclusive, one on a line. Example output:

# $ python 1_to_10.py
# 1
# 2
# 3
# 4 etc.

# for i in range(1, 11):
# 	print i;

#--------------------------------------------------
# Same as the previous problem, except you will prompt the user for the number to start on and the number to end on. Example session:

# $ python n_to_m.py
# Start from: 2
# End on: 8
# 2
# 3
# 4

# line_one = int(raw_input("Please select your starting number."));
# line_two = int(raw_input("Please select your ending number."));

# line_two += 1;
# for i in range(line_one, line_two):
# 	print i;
#--------------------------------------------------
# Odd Numbers

# Print each odd number between 1 and 10 inclusive. Example output:

# for i in range(1,11,2):
# 	print i;
#--------------------------------------------------
# Print a Square

# Print a 5x5 square of * characters. Example output:

# layer = '*****';
# for i in range(1,6):
# 	print layer;
#--------------------------------------------------
# Print a Square II

# Print a NxN square of * characters. Prompt the user for N. Example output:

# $ python square2.py
# How big is the square? 10

# star = '*';
# response = int(raw_input("Please select your number."));
# response += 1;
# star = star * response;
# for i in range(1, response):
# 	print star;
#--------------------------------------------------
# Print a Box

# Given a height and width, input by the user, print a box consisting of * characters as its border. Example session:

# $ python box.py
# Width? 6
# Height? 4
# star_width = '*';
# star_height = '*';
# width = int(raw_input("Please select your width."));
# height = int(raw_input("Please select your height."));
# star_width = star_width * width;
# star_heigh = star_height * height;

# for i in range(1, width):
# 	print star_width;
# 	for i in range(1, height):
# 		print star_height;


# width = int(raw_input("Declare a width: "))
# height = int(raw_input("Declare a height: "))

# boundary_aster = "*" * width;
# mid_aster = "*" + (" " * (width - 2)) + "*";

# for i in range(1,(height+1)):
# 	if i == 1 or i == height:
# 		print boundary_aster;
# 	else:
# 		print mid_aster;
#--------------------------------------------------
# Print a Triangle

# Print a triangle consisting of * characters like this:

#    *
#   ***
#  *****
# *******

star = '*';
for i in range(1, 5):
	star = star * 2;
	print star;

#--------------------------------------------------