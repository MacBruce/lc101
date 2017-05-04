
#inp_str = input("Count the amount of time charecters appear in a string! Input string!")




def count_char(str):
    #alphabet map
    alphabet = {
        'a' : 0,
        'b' : 0,
        'c' : 0,
        'd' : 0,
        'e' : 0,
        'f' : 0,
        'g' : 0,
        'h' : 0,
        'i' : 0,
        'j' : 0,
        'k' : 0,
        'l' : 0,
        'm' : 0,
        'n' : 0,
        'o' : 0,
        'n' : 0,
        'q' : 0,
        'r' : 0,
        's' : 0,
        't' : 0,
        'u' : 0,
        'v' : 0,
        'w' : 0,
        'x' : 0,
        'y' : 0,
        'z' : 0
    }

    #set string input to lower case
    new_str = str.lower()

    #loop over each item -- if i is a key in map add 1 to value at i and return
    for i in new_str:
        if alphabet.has_key(i):
            alphabet[i] += 1
    return alphabet


def main():
    #test strings
    test = """Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    Nunc accumsan sem ut ligula scelerisque sollicitudin. Ut at sagittis augue.
    Praesent quis rhoncus justo. Aliquam erat volutpat.
    Donec sit amet suscipit metus, non lobortis massa.
    Vestibulum augue ex, dapibus ac suscipit vel, volutpat eget massa.
    Donec nec velit non ligula efficitur luctus. """

    test2 = "My name is mac bruce"

    print(count_char(test2))

if _name_ = '_main_':
    main()
