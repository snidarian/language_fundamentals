#!/usr/bin/python3
# Illustrates supplying unlimited arguments to a function


# simply use the '*' asterisk to signigy that 'args' and an argument can reoccur indefinitely
def main(*args):
    list0 = []
    for integer in args:
        integer=(integer*2)
        list0.append(integer)
    return list0


if __name__ == "__main__":
    resulting_list = main(2, 4, 8, 16, 32)
    print(resulting_list)







