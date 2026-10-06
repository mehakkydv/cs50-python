filename = input("File name: ")
newname = filename.strip().lower()
if newname.endswith(".gif"):
    print("image/gif")
elif newname.endswith(".jpg") or newname.endswith(".jpeg"):
    print("image/jpeg")
elif newname.endswith(".png"):
    print("image/png")
elif newname.endswith(".pdf"):
    print("application/pdf")
elif newname.endswith(".txt"):
    print("text/plain")
elif newname.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
