This program takes in two files:
	1) phone_dataset.csv (Used to initialize a phonebook)
	2) query.txt (List of last names separated by new lines to search for)


phone_dataset.csv is allowed to be formatted in 1 of 3 ways:

Lastname, Firstname, New York, (917) 958-1191
Firstname Lastname, 9179581191, New York
Firstname, Lastname, (917) 358-1291, California

Output returns all results that match any of the last names given
in query.txt.