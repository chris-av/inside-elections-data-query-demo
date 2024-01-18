import os
import pandas as pd
from pprint import PrettyPrinter
from utils.ratings import presidential_ratings, house_ratings, senate_ratings, governor_ratings

pp = PrettyPrinter(indent=4)



# create directory if it doesn't exist
for p in ["out", "out/ratings"]:
    if not os.path.isdir(p):
        print(f"creating dir : {p}")
        os.mkdir(p)

data = presidential_ratings()
ratings = data["race"]
rating_data = []
for rating in ratings:
    dta = {}
    dta["state"] = rating["state"]["label"]
    dta["state_abbr"] = rating["state"]["id"]
    dta["electoral_votes"] = rating["electoral_votes"]
    dta["rating_score"] = rating["rating"]["id"]
    dta["rating_description"] = rating["rating"]["label"]
    dta["link"] = rating["link"]
    rating_data.append(dta)
df = pd.DataFrame(rating_data)
df.to_csv("out/ratings/presidential.csv", index=False)



data = house_ratings()
ratings = data["race"]
rating_data = []
for rating in ratings:
    dta = {}
    dta["state_abbr"] = rating["state"]
    dta["party"] = rating["party"]
    dta["district"] = rating["district"]
    dta["incumbent"] = rating["incumbent"]
    dta["rating_score"] = rating["rating"]["id"]
    dta["rating_description"] = rating["rating"]["label"]
    dta["link"] = rating["link"]
    rating_data.append(dta)
df = pd.DataFrame(rating_data)
df.to_csv("out/ratings/house.csv", index=False)




data = senate_ratings()
ratings = data["race"]
rating_data = []
for rating in ratings:
    dta = {}
    dta["state_abbr"] = rating["state"]
    dta["party"] = rating["party"]
    dta["class"] = rating["class"]
    dta["incumbent"] = rating["incumbent"]
    dta["rating_score"] = rating["rating"]["id"]
    dta["rating_description"] = rating["rating"]["label"]
    dta["link"] = rating["link"]
    rating_data.append(dta)
df = pd.DataFrame(rating_data)
df.to_csv("out/ratings/senate.csv", index=False)


data = governor_ratings()
ratings = data["race"]
rating_data = []
for rating in ratings:
    dta = {}
    dta["state_abbr"] = rating["state"]
    dta["party"] = rating["party"]
    dta["incumbent"] = rating["incumbent"]
    dta["rating_score"] = rating["rating"]["id"]
    dta["rating_description"] = rating["rating"]["label"]
    dta["link"] = rating["link"]
    rating_data.append(dta)
df = pd.DataFrame(rating_data)
df.to_csv("out/ratings/governor.csv", index=False)

