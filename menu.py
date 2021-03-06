import json # used to parse the data from json to usable data
import requests # used to get the data from the API
import sys # used to exit the app
import connectivity # connecting with the main file that connects with the API

def menu():
    """
    This menu serves as the main hub of the program.
    Use stars to make it look 'pretty'.
    """

    # Getting the data
    print("Wait a second while I am getting the current League version")
    current_version = connectivity.get_current_version()
    print("Latest version retrieved!")
    print("\nGetting the champion's data for that patch - might take a milisecond or two")
    championsdata = connectivity.get_data(current_version)
    print("\nAll good and ready to go!")

    while True:
        print("**********************")
        print("1. Find champions stats")
        print("2. Get data on all champions")
        print("3. Get a list of champions sorted by a specific attribute")
        print("4. Stats sorted, but with the option to add level(1-18)")
        print("5. Exit the Program")
        print("**********************")
        users_choice = input()
        if users_choice == "":
            sys.exit()
        users_choice = int(users_choice)

        if users_choice == 1:
            name = input("What's the name of that champion? ")
            stats = connectivity.get_champion_data(name, championsdata)
            print('Here are the stats of your selected champion!')
            print(stats + "\n")

        elif users_choice == 2:
            print("Prepare for a slight lag")
            connectivity.get_every_champion(championsdata)
        elif users_choice == 3:
            print('Cool, now what\'s the stat (your options: hp, mp, movespeed, armor, spellblock, attackrange, hpregen, mpregen, crit, attackdamage, attackspeed)')
            stat = input()
            print(connectivity.sort_by_stat(championsdata, stat))
        elif users_choice == 4:
            print("Attackspeed (among others :( ) is broken currently!!!")
            print('Cool, now what\'s the stat (your options: hp, mp, movespeed, armor, spellblock, attackrange, hpregen, mpregen, crit, attackdamage, attackspeed)')
            stat = input()
            print("Now, please type in the level (press enter for level 1)")
            level = input()
            if level == "":
                print(connectivity.sort_by_stat_on_specific_level(championsdata, stat))
            else:
                print(connectivity.sort_by_stat_on_specific_level(championsdata, stat, level))
        elif users_choice == 5:
            sys.exit()
        #elif users_choice == 6:
        #    name = input('Name of the champion: ')
        #    level = input('Level: ')
        #    connectivity.get_champions_stat_on_specific_level(name, level, championsdata)
        else:
            print("The given input doesn't match any number from the list.")


# Makes it so the menu runs at startup!
if __name__ == "__main__":
    menu()