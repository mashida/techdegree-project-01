import csv
from datetime import datetime
import random

TEAMS = ['Sharks', 'Dragons', 'Raptors']

def generateFile(player, team): # function that generates additional files
    with open(player['Name'].lower().replace(" ", "_") + ".txt", "w") as file:
        file.write("Dear " + player['Guardian Name(s)'] +
                   "\n\n" +
                   "Player's Name: " + player['Name'] + "\n" +
                   "Team Name: " + team + "\n" +
                   "Date of time first practice: " + str(datetime(random.choice(range(1994,2000)), random.choice(range(1,13)), random.choice(range(1,29)), random.choice(range(0,23)), random.choice(range(0,59)), random.choice(range(0,59)))))

# Start of program here

if __name__ == '__main__':
    with open('soccer_players.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile) # I read data drom csv file and store in in the Ordered Dictionary

    # I create two lists with plyers name accrotding to their experinece
        teamNoExp = list()
        teamYesExp = list()
        for row in reader:
            if row['Soccer Experience'] == 'NO':
                teamNoExp.append(row)
            else:
                teamYesExp.append(row)

    # I write all the info into the teams.txt file and create additional text files
        file = open("teams.txt", "w")

        for team in TEAMS:
            file.write(team + "\n")

            for i in range(3):

                player = teamNoExp.pop()
                file.write(player['Name'] + ', ' + player['Soccer Experience'] + ", " + player['Guardian Name(s)'] + "\n")
                generateFile(player, team)

                player = teamYesExp.pop()
                file.write(player['Name'] + ', ' + player['Soccer Experience'] + ", " + player['Guardian Name(s)'] + "\n")
                generateFile(player, team)

            file.write("\n")

        file.close()
