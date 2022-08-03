'''
Thomas Koutsidis
June 2nd, 2022

Question 5

This program has the ability to read a file; in this example it is "Twinkle.txt."
It then counts and prints the number of words in the file.
'''
def main():
    print("This program counts the number of words in an input file.")
    fname = input("Enter filename: ")
    infile = open(fname, 'r')
    word_count = 0
    for lines in infile:
        list = lines.split(" ")
        word_count = word_count + len(list)
    print("There are", word_count, "words in this file.")
    
    
main()
