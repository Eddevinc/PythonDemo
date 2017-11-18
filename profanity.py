
from urllib.request import urlopen


def readtext():
    file = open("sample.txt")
    contents = file.read()
    file.close()
    profanitycheck(contents)


def profanitycheck(query):
    connection = urlopen("http://www.wdylike.appspot.com/?q="+query);
    response = connection.read()
    if b'true' in response:
        print("Profanity Alert!!")
    elif b'false' in response:
        print("No curse words found")
    else:
        print("Could not scan document")
    connection.close()


readtext()
