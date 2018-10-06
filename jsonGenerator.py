import math
import glob, os
import time
import json

# with open('data.json', 'w') as outfile:
#     json.dump(data, outfile)

def listDirectories(dir):
    return os.listdir(dir)

a = [x[0] for x in os.walk(".")]

b = listDirectories(".")

jsonFile = []

for i in b:
    if not os.path.isdir(i) or i == '.git':
        continue

    category = i;
    articles = os.listdir("./{}/".format(i));

    if (len(articles) == 0):
        continue;


    d1 = {}
    d1["articles"] = []
    d1["category"] = category;

    for article in articles:

        f = open("./{}/{}".format(i, article))
        title = f.readline().replace("#", "").strip("\n").strip()
        created_at = f.readline().replace("#", "").strip("\n").strip()
        f.close()

        d2 = {}
        d2["name"] = article
        d2["title"] = title
        d2["created_at"] = created_at

        d1["articles"].append(d2)

    jsonFile.append(d1)

print(jsonFile)
with open('articles.json', 'w') as outfile:
    json.dump(jsonFile, outfile)
# listDirectories(".")
