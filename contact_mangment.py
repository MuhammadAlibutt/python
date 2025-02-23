import json


def add_contant(people):
    name = input('Name: ')
    emmail = input('Email: ')
    phone = input('Phone: ')

    person = {"name" : name, "email" : emmail, "phone" : phone}
    return person

def display_contant(people):
    for p, person in enumerate(people):
        print( p + 1 , '-' , 'Name:', person['name'] , '|' , 'Email:' , person['email'] , '|' , 'Phone:' , person['phone'] )
def delete_contant(people):
    display_contant(people)
    no = input('Enter Id you want to delete: ')
    while True:
        try:
            number = int(no)
            if number <= 0 or number > len(people):
                print('record not found')
            else:
                break
        except:
            print('Invalid input')
    
    people.pop(number - 1)

def search_content(people):
    display_contant(people)
    results = []
    search = input("Enter Name to Search: ").lower()
    for person in people:
        name = person['name'].lower()
        if search in name:
            results.append(person)

    print()
    print("Searched Content")
    display_contant(results)      

    


print("Hello, Welcom to  Contact Mangment Systemm!")
print()

with open("contact_data.json" , "r") as f:
    people = json.load(f)["content"]

while True:
    print('Number of Content: ' , len(people))
    print()
    command = input("What you want 'ADD' , 'Search' , 'Delete' and 'Q' to quite: ").lower()
    print()
    if command == "add":
        person = add_contant(people)
        people.append(person)
        print('Content Added')
        print(people)
    elif command == "search":
        search_content(people)
    elif command == "delete":
        deleted_person = delete_contant(people)
        print('Content Deleted')
        display_contant(people)
    elif command == "q":
        break
    else:
        print("Invalid Command")


with open("contact_data.json" , "w") as f:
    json.dump({"content": people} , f)
