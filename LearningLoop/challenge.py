
def main():

    farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
        {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
        {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

    for x in farms:
        print(x.get("name", "farms"), end=":\n")

        for agri in x.get("agriculture"):
            print(" -", agri)

if __name__ == '__main__':
    main()
