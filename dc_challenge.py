# Question 1
full_name = "Michael Irby";
age = 30;

# Question 2
myArray = [];
myArray.extend([full_name, age]);
print myArray;

# Question 3
def say_hello():
	print "Hello!";

say_hello();

# Question 4
split_name = full_name.split(' ');
print split_name;

# Question 5
def my_age():
	print "Hello, " + split_name[0] + "!";

my_age();

# Question 6
def my_age(year):
	born = 2017 - year;
	print born;

my_age(1986);

# Question 7
def sum_odd_numbers():
	sum = 0;
	for i in range(1, 5001, 2):
		sum += i;
	print sum;

sum_odd_numbers();