import random
import itertools
import csv
import string
from random import randint

# teams = ['Cook', 'Berners-Lee', 'Burton', 'Duncan', 'Robbins', 
#         'McGraw', 'Allen', 'Roth', 'Baland', 'Ber', 'Lee', 'Buktu', 
#         'Mid', 'Mothy', 'Chu', 'Possible', 'Kardashian', 'KathNiel', 'LizQuen', 'Jadine']
# numteams = len(teams)

#Generates truly random team names

def randomStrings(numTeams):
    
    letters = string.ascii_lowercase
    #[a,b,c....]

    teams = set() 
    #Sets must always have unique values, therefore this set will always have unique team names
    
    while len(teams) != numTeams:
        teamname = ''
        for i in range(randint(2,7)):
            teamname+=random.choice(letters)
        teams.add(teamname.capitalize())
    return list(teams)

#Assigns ids to Teams randomly
def idAssignment(a):
    team_ids = {}
    for id in range(1,len(a)+1):
        chosen_team = random.choice(a)
        a.remove(chosen_team)
        team_ids[id] = 'Team' +' '+chosen_team
    return team_ids
    
#Generates matchups randomly
def roundRobinMatchups(matches, matchnums,teams):

    ids = list(teams.keys())
    median = len(ids)//2

    num_rounds = len(ids) - 1
    #Round Robin rules dictate that to there will always be n-1 rounds

    for roundnum in range(num_rounds):
        #This is the generic formula for a round robin matchup found on Wikipedia
        teama = ids[:median]
        teamb = ids[median:]
        teamb.reverse()

        for i in range(len(teama)):

            winner_id = random.choice((teama[i],teamb[i]))
            #Choose the winner randomly

            loser_id = teama[i] if winner_id == teamb[i] else teamb[i]
            #Loser will be whoever is not the winner

            matches.append((matchnums,winner_id,loser_id))
            matchnums+=1

        ids.insert(1, ids.pop())
        #Teams rotate here
        #We keep index 0 as the pivot

    return matches, matchnums


def addRandomMatchups(matches, matchnums, teams2, numMatches):
    teams = teams2.copy()
    for i in range(numMatches):
        ids = list(teams.keys())
        teama_key, teamb_key = random.sample(ids, 2)
        teama = teams.pop(teama_key)
        teamb = teams.pop(teamb_key)

        print(teama_key,teamb_key)

        winner_id = random.choice((teama_key,teamb_key))
        loser_id = teama_key if winner_id == teamb_key else teamb_key
        matches.append((matchnums,winner_id,loser_id))
        matchnums+=1
    
    return matches, matchnums
        


matches = []
matchnums = 0


# id_assignment(teams)
teams = randomStrings(20)
assigned = idAssignment(teams)
matches, matchnums = roundRobinMatchups(matches, matchnums, assigned)
matches, matchnums = addRandomMatchups(matches, matchnums, assigned, 10)



csv_file_path = 'TeamIDs.csv'
# Open the file in write mode ('w') and specify newline='' to prevent extra blank lines
with open(csv_file_path, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Team ID', 'Team Name'])
    # Write data
    for assigned_id, team in assigned.items():
        csv_writer.writerow([assigned_id, team])


csv_file_path_2 = 'Matches.csv'
with open(csv_file_path_2, 'w', newline='') as csvfile2:
    csv_writer_2 = csv.writer(csvfile2)
    csv_writer_2.writerow(['Match Number', 'Winner ID', 'Loser ID'])
    csv_writer_2.writerows(matches)