# Given the following dictionary, representing a mapping from names to phone numbers:

phonebook_dict = {
	'Alice': '703-493-1834',
	'Bob': '857-384-1234',
	'Elizabeth': '484-584-2923'
}

# print phonebook_dict['Elizabeth'];
# phonebook_dict['Kareem'] = '938-489-2923';

# # print phonebook_dict;

# del phonebook_dict['Alice'];
# # print phonebook_dict;

# phonebook_dict['Bob'] = '968-345-2345';
# # print phonebook_dict;

# print phonebook_dict;

ramit = {
	'name': 'Ramit',
	'email': 'ramit@gmail.com',
	'interests': ['movies', 'tennis'],
	'friends': [
		{
			'name': 'Jasmine',
			'email': 'jasmine@yahoo.com',
			'interests': ['photography', 'tennis']
		},
		{
			'name': 'Jan',
			'email': 'jan@hotmail.com',
			'interests': ['movies', 'tv']
		}
	]
}
# 1. Write a python expression that gets the email address of Ramit.
# print ramit['email'];
# 2. Write a python expression that gets the first of Ramit's interests.
# print ramit['interests'][0];
# 3. Write a python expression that gets the email address of Jasmine.
# print ramit['friends'][0]['email'];
# 4. Write a python expression that gets the second of Jan's two interests.
# print ramit['friends'][1]['interests'][1];

#------------------------------------------------------------------------------------

# Write a letter_histogram function that takes a word as its input, and returns a dictionary
# containing the tally of how many times each letter in the alphabet was used in the word. For example:

# >>> letter_histogram('banana')
# {'a': 3, 'b': 1, 'n': 2}

