import requests
import pickle

# I got spoiled on peak hill == pickle
# It really doesn't sound similar at all...

banner = requests.get("http://www.pythonchallenge.com/pc/def/banner.p").content
unknown = pickle.loads(banner)

# Unknown is a list of tuples ... at this point I'm thinking it might be instructions for building some ascii art

for i in unknown:
    for j in i:
        print(j[0] * j[1], end="")
    print("")
