def convert(text):
     text = text.replace(":)","🙂")
     text = text.replace(":(","🙁")
     return text

def main():
    myinput = input()
    myoutput = convert(myinput)
    print(myoutput, end="")

main()
