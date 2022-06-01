'''

Thomas Koutsidis

May 21st, 2022

Question 3

We modified the convert.py program so it uses a loop.
The loop computes and prints a table of Celsius temperatures.
It prints the Fahrenheit equivalents every 10 degrees from 0 C to 100 C.

'''

def main():
    print("Conversion table from Celsius to Fahrenheit")
    print("Celsius\tFahrenheit")
    print("-------------------")
    for i in range(0,101,10):
        print(i, "\t\t", ((9/5) * i +32))

main()
    
       
    