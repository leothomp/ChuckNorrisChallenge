#!/Users/leothomp/PycharmProjects/ChuckNorrisChallenge/ve-Chuck/bin/python
import requests
import json


urlRandomJoke="https://api.chucknorris.io/jokes/random"
urlJokeByCat="https://api.chucknorris.io/jokes/random?category="
urlJokeCatList="https://api.chucknorris.io/jokes/categories"

def getRandomJoke():
    try:
        response=requests.get(urlRandomJoke)
        response.raise_for_status()
    except requests.exceptions.HTTPError as error:
        print(error)
    jsonResponse=response.json()
    return(jsonResponse["value"])

def getJokeCatList():
    try:
        response=requests.get(urlJokeCatList)
        response.raise_for_status()
    except requests.exceptions.HTTPError as error:
        print(error)
    jsonResponse = response.json()
    return (jsonResponse)

def getJokeByCat(userCat):
    try:
        response=requests.get(
            f"{urlJokeByCat}{userCat.lower()}")
        response.raise_for_status()
    except requests.exceptions.HTTPError as error:
        print("Invalid Input")
        input("Press any key to continue...")
        main()
    jsonResponse = response.json()
    return (jsonResponse["value"])

def main():
# TESTS
#    randJoke=getRandomJoke()
#    print(randJoke)
#    catList=getJokeCatList()
#    print(*catList, sep='\n')
#    userCat=input("Enter cat: ")
#    jokeByCat=getJokeByCat(userCat)
#    print(jokeByCat)
# END TESTS

#MAIN MENU
    print("*****************\n**  Main Menu  **\n*****************\n1) Random Norris Joke\n2) List Joke Categories\n3) Norris Joke by Category\nX = Exit")
    choice=input("Enter Choice: ")
    if choice == "1":
        randJoke=getRandomJoke()
        print(randJoke)
        input("Press any key to continue...")
        main()
    elif choice == "2":
        catList=getJokeCatList()
        print(*catList, sep='\n')
        input("Press any key to continue...")
        main()
    elif choice == "3":
        userCat=input("Enter Joke Category: ")
        jokeByCat=getJokeByCat(userCat)
        print(jokeByCat)
        input("Press any key to continue...")
        main()
    elif choice == "X" or "x":
        exit()
    else:
        print("Invalid Selection")
        input("Press any key to continue...")
        main()



if __name__ == "__main__":
    main()