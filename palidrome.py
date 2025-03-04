#function to show a palidrome using stack



show_expected_result = False
show_hints = False

def is_palindrome(teststr):

    newstr = ""
    for char in teststr:
        if char.isalnum():
            newstr += char
    
    if newstr.lower() == newstr[::-1].lower():
        #print(clean_text[::-1].lower())
        show_expected_result = True
        #print(show_expected_result)
        return show_expected_result
    else:
        #print(remove_teststr.lower())
        show_expected_result = False
        return show_expected_result


total = 0
test_words = ["Hello World!","Radar","Mama?","Madam, I'm Adam.",
    "Race car!"]
for word in test_words:
    total += is_palindrome(word)

print(total)

