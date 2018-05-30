import os

combined_list = []
prime_list = []
happy_list = []


def prime_num():
	#this function opens the file, reads it and then cleans the items in the list and appends them to a new list.
	with open('primenumbers.txt','r') as prime_file:
		
		for line in prime_file:
			new_line = line.strip()
			new_line = line.replace('\n','')
			prime_list.append(new_line)
		

		return prime_list

def happy_num():
	#this function opens the file, reads it and then cleans the items in the list and appends them to a new list.
	with open('happynumbers.txt', 'r') as happy_file:

		for line in happy_file:
			new_line_two = line.strip()
			new_line_two = line.replace('\n','')
			happy_list.append(new_line_two)
		
		return happy_list

def overlap(happy_l, prime_l):
	#this function will take both of the lists returned from the other function and will create a new list of only numbers that occur in both lists.
	happy_len = len(happy_l)
	prime_len = len(prime_l)

	if prime_len > happy_len:
		for item in prime_l:
			if item in happy_l and prime_l:
				combined_list.append(item)

		print(combined_list)

	else:
		for item in happy_l:
			if item in happy_l and prime_l:
				combined_list.append(item)
		print(combined_list)

def main():

	prime = prime_num()
	happy = happy_num()

	overlap(happy,prime)


if __name__ == '__main__':
	main()