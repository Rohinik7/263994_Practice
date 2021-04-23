"""Write a python program to check the user input abbreviation.
If the user enters "lol", print "laughing out loud".
If the user enters "rofl", print "rolling on the floor laughing".
If the user enters "lmk", print "let me know".
If the user enters "smh", print "shaking my head"."""
n=input("Enter the abbreviation: ").lower()
if n=='lol':
    print("laughing out loud")
elif n=='rofl':
    print("rolling on the floor laughing")
elif n=='lmk':
    print("let me know")
elif n=='smh':
    print("shaking my head")
