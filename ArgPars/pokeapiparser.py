
import argparse

import requests

## for working with data in lots of formats
## python3 -m pip install pandas
import pandas

ITEMURL = "http://pokeapi.co/api/v2/item/"

def main():

    # Make HTTP GET request using requests
    # and decode JSON attachment as pythonic data structure
    # Also, append the URL ITEMURL with a parameter to return 1000
    # items in one response
    items = requests.get(f"{ITEMURL}?limit=1000")
    items = items.json()

    # create a list to store items with the word searched on
    matchedwords = []

    # Loop through data, and print pokemon names
    # item.get("results") will return the list
    # mapped to the key "results"
    for item in items.get("results"):
        # check to see if the current item's VALUE mapped to item["name"]
        # contains the search word
        if args.searchword in item.get("name"):
            # if TRUE, add that item to the end of list matchedwords
            matchedwords.append(item.get("name"))

    finishedlist = matchedwords.copy()
    ## map our matchedword list to a dict with a title
    matchedwords = {}
    matchedwords["matched"] = finishedlist

    ## list all words containing matched word
    print(f"There are {len(finishedlist)} words that contain the word '{args.searchword}' in the Pokemon Item API!")
    print(f"List of Pokemon items containing '{args.searchword}': ")
    print(matchedwords)

    ## export to excel with pandas
    # make a dataframe from our data
    itemsdf = pandas.DataFrame(matchedwords)
    # export to MS Excel XLSX format
    # run the following to export to XLSX
    # python -m pip install openpyxl
    # index=False prevents the index from our dataframe from
    # being written into the data
    itemsdf.to_excel("pokemonitems.xlsx", index=False)

    print("Gotta catch 'em all!")

def get_names():
    #need to make a request
    r = requests.get("https://pokeapi.co/api/v2/pokemon/?limit=1119").json
    print(r)
    print(r['results'][0]['name'])

    names = []

    for poke in r['results']:
        names.append(poke['name'])

    return names

def names_out(names: list):
    # text file
    with open("pokenames.txt", "w") as f:
        for name in names:
            f.write(f"{names}\n")

    pokes = {"Name": names}
    print(pokes)
    pokedf = pandas.DataFrame(pokes)
    print(pokedf)
    #json
    pokedf.to_json("pokemones.json")

    #excel
    pokedf.to_excel("pokenames.xlsx")


if __name__ == "__main__":
    #parser = argparse.ArgumentParser(description="Pass in a word to search\
    #the Pokemon item API")
    #parser.add_argument('searchword', metavar='SEARCHW',\
    #type=str, default='ball', help="Pass in any word. Default is 'ball'")
    #args = parser.parse_args()
    #main()
    names_out(get_names())