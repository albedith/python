sentence = "First Name,Last Name,Street Address,City,State,Zip Code"
separators = [".", ","]
results = []
current_word = ""

for letter in sentence:
    if letter in separators:
        results.append(current_word)
        current_word = ""
    else:
        current_word = current_word + letter
results.append(current_word)

print results