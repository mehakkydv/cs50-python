answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
my_answer = answer.strip().lower()
if my_answer == "42" or my_answer == "forty-two" or my_answer == "forty two":
    print("Yes")
else:
    print("No")
