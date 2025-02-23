

#task-1

number = input("Enter any Binary Number: ")
counter = 0

for i in number:
    if int(i) == 1:
        counter += 1

print("number of 1 in given number: " + str(counter))



#task-2
given_string = input("Enter and String: ")

for s in given_string:
    if s == "-":
        x = given_string.index('-')
        print("- in given string: " + str(x))
        break



#task-3

given_string = input("Enter and String: ")
index = []

for s in range(len(given_string)):
    if given_string[s] == "-":
        index.append(s)

print("index: " + str(index))



#task-4

given_string = input("Enter 1st string: ")
given_string2 = input("Enter 2nd string: ")

if len(given_string) == len(given_string2):
    for s in range(len(given_string)):
        if(given_string[s] != given_string2[s]):
            print(s)
else:
    print("both strings are not of same length")


