import requests
import xml.etree.ElementTree as ET
import json

def presidential_ratings():
    url = "https://insideelections.com/api/xml/ratings/president"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Something went wrong with the request")
    content = response.text
    tree = ET.fromstring(content)
    root = tree
    data = _processXML(root)
    with open("out/ratings/presidential.json", "w") as f:
        print("writing data to", f.name)
        json.dump(data, f, indent=4)
        f.close()
    return data


def house_ratings():
    url = "https://insideelections.com/api/xml/ratings/house"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Something went wrong with the request")
    content = response.text
    tree = ET.fromstring(content)
    root = tree
    data = _processXML(root)
    with open("out/ratings/house.json", "w") as f:
        print("writing data to", f.name)
        json.dump(data, f, indent=4)
        f.close()
    return data


def senate_ratings():
    url = "https://insideelections.com/api/xml/ratings/senate"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Something went wrong with the request")
    content = response.text
    tree = ET.fromstring(content)
    root = tree
    data = _processXML(root)
    with open("out/ratings/senate.json", "w") as f:
        print("writing data to", f.name)
        json.dump(data, f, indent=4)
        f.close()
    return data



def governor_ratings():
    url = "https://insideelections.com/api/xml/ratings/governor"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Something went wrong with the request")
    content = response.text
    tree = ET.fromstring(content)
    root = tree
    data = _processXML(root)
    with open("out/ratings/governor.json", "w") as f:
        print("writing data to", f.name)
        json.dump(data, f, indent=4)
        f.close()
    return data



def _processXML(xml):
    data = {}
    for child in xml:
        if len(child) > 0:
            tag = child.tag
            result = _processXML(child)
            if tag == "race":
                if "race" not in data.keys():
                    data["race"] = []
                else:
                    data["race"].append(result)
            else:
                tmp = {}
                tmp[tag] = result
                data.update(tmp)

        else:
            tag = child.tag
            value = child.text
            data[tag] = value

    return data
