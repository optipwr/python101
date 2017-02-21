from string import maketrans
# Uppercase a String

# Given a string, print the string uppercased. #string #easy

# response = raw_input("Please say your name").upper();
# print response;

#----------------------------------------------------

# Capitalize a String

# Given a string, print the string capitalized. #string #easy

# response = raw_input("Please say your name in lowercase\n").title();
# print response;

#----------------------------------------------------

# Reverse a String

# Given a string, print the string reversed.

# response = raw_input("Input a string here!\n");
# response[::-1];
# print response;

# print 'test'[::-1]

#----------------------------------------------------

# Leetspeak

# Given a paragraph of text as a string, print the paragraph in leetspeak. To translate a string to leetspeak, you need to replace make the following character replacements (treat all input characters as uppercase):

# A => 4
# E => 3
# G => 6
# I => 1
# O => 0
# S => 5
# T => 7
# Example: Leet => l337

# intab = "aegiost";
# outtab = "4361057";
# trantab = maketrans(intab, outtab);

# str = "this is an example";
# print str.translate(trantab);

#----------------------------------------------------

# Long-long Vowels

# Given a word as a string, print the result of extending any long vowels to the length of 5. Examples:

# Good => Goooood
# Cheese => Cheeeeese
# Man => Man
# Spoon => Spooooon

# def long_vowel(string):
# 	string = string.replace('aa', 'aaaaa')
# 	string = string.replace('ee', 'eeeee')
# 	string = string.replace('ii', 'iiiii')
# 	string = string.replace('oo', 'ooooo')
# 	string = string.replace('uu', 'uuuuu')
# 	print string;

# long_vowel('graat');

#----------------------------------------------------

# Caesar Cipher

# Given a string, print the Caesar Cipher (or ROT13) of that string. What is Caesar Cipher? http://practicalcryptography.com/ciphers/caesar-cipher/

# Use your solution to decipher the following text: "lbh zhfg hayrnea jung lbh unir yrnearq"

normal_bet = 'abcdefghijklmnopqrstuvwxyz';
offset_bet = 'nopqrstuvwxyzabcdefghijklm';

translated = maketrans(normal_bet, offset_bet);
str = "lbh zhfg hayrnea jung lbh unir yrnearq";
print str.translate(translated);
