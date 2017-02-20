# name = "Michael Irby";
# name = "Michael " + "Irby";

# forty_two = 40 + 2;
# print forty_two;
# forty_two = 84 / 2;
# print forty_two;
# forty_two = 83 % 2;
# print forty_two;

# Array... pysche! Lists (in Python)
animals = [
	'wolf',
	'giraffe',
	'hippo'
];
# print animals;
# print animals[0];
# print animals[-1];

# How do we push a new element on a list? Append!
# animals.append("Alligator");
# print animals;

# # To delete an index use remove method
# animals.remove("wolf");
# print animals;

# # We can insert into any indicie with "insert"
# animals.insert(0,'zebra');
# print animals;
# animals[0] = "horse";
# print animals;

# # Pop works the same way... remove the last element
# animals.pop();
# print animals;

# split works the same way as well
dc_class = "Michael, Paul, Mason, Casey, Connie, Sarah, Andy";
dc_class_as_array = dc_class.split(", ");
# print dc_class_as_array;
# sorted_class = sorted(dc_class_as_array);
# print dc_class_as_array;

# dc_class_as_array.sort();
# print dc_class_as_array;

# # reverse method reverses the array, NOT on value but on index


# # len attribute, it works like .length in JS
# print len(dc_class_as_array);

# # slice in JS is [x:x]
# print dc_class_as_array[2:4];

# For loop
for student in dc_class_as_array:
	# Indentation matters in Python!
	print student;

for i in range(1,10):
	print i;

# a function in python is not a function. it is a definition (def)
def sayHello():
	# just like for loops, : is the curly brace
	# indentation matters
	print "Hello, World";

sayHello();

def say_hello_with_name(name):
	print "Hello, " + name;

say_hello_with_name("Michael");

