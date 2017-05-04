

def get_initials(fullname):
	caps = fullname.upper().split()
	
	if len(caps) == 2:
		first_n = caps[0][0]
		last_n = caps[1][0]
		return first_n + last_n
	elif len(caps) == 3:
		first_n = caps[0][0]
		middle_n = caps[1][0]
		last_n = caps[2][0]
		return first_n + middle_n + last_n
	else:
		first_n = caps[0][0]
		return first_n

	

def main():
	fullnameinp = raw_input("what is your full name? \n")
	print(get_initials(fullnameinp))

if __name__ == '__main__':
    main()
