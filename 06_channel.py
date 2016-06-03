
"""
Hint title: now there are pairs
Hint image: a zipper

Right now I'm confident I need to use zip() to do something, but on what data?

... Actually I think it's talking about a zip file after visiting zip.html


"""

import requests
import zipfile
import io
import re


zipbytes = requests.get("http://www.pythonchallenge.com/pc/def/channel.zip").content

zipf = io.BytesIO(zipbytes)
zip = zipfile.ZipFile(zipf)

"""Found a readme inside the list"""

print(zip.read("readme.txt").decode("utf-8"))

"""This appears to be a rehash of linkedlist"""

print("----")

current = "90052"
commentart = ""

while True:
    fname = current + ".txt"
    fdata = zip.read(fname).decode("utf-8")
    commentart += zip.getinfo(fname).comment.decode("utf-8") # funfact: zip files can have comments associated with them
    try:
        current = re.search("nothing is ([0-9]+)", fdata).group(1)
    except AttributeError:
        break


print(commentart)


