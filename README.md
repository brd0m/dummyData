teams.py

1. Generates n Random Strings as Team Names, these are stored in a list
2. These Team Names are randomly assigned Team IDs, Team ID: Team Name pairs are stored in a dict (TeamIDs)
3. In a Round Robin fashion there will be n-1 Rounds with n/2 matches each. For n = 20 teams there will be an initial 190 matches total
4. To hit the 200 match quota, we will generate 1 round with randomized matchups
5. Matchups compromise of Match Number, Winner Id, and Loser Id. These are stored in a list of tuples (Matchups)
6. TeamIDs and Matchups are stored in separate csvs

TeamIDs

![Screenshot_20240415_142338](https://github.com/brd0m/dummyData/assets/113246520/79818f54-2298-4bb9-929b-62f4c19f3d37)

Matchups

![Screenshot_20240415_142423](https://github.com/brd0m/dummyData/assets/113246520/e80ad739-79b5-4b7a-a1df-529d5f74df27)


teams.sql
1. Start with TeamIDs, left join with Matches wherever a Match involves that specific Team ID
2. Group By Team Name (or Team Id) and COUNT all instances where a TeamID is under Winner ID as Wins, the opposite for loses
3. Use DENSE_RANK() as there may be ties to properly implement ranking

![Screenshot_20240415_142116](https://github.com/brd0m/dummyData/assets/113246520/d0417267-d364-4125-a1b0-751f984f5fd7)
