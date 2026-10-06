greeting = input("Greeting: ")
cleangreeting = greeting.strip().lower()
if cleangreeting.startswith("hello"):
    print("$0")
elif cleangreeting.startswith("h"):
    print("$20")
else:
    print("$100")
