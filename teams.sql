SELECT 
    `Team Name`,
    DENSE_RANK() OVER (ORDER BY Wins DESC) AS Ranking,
    Wins,
    Loses
    
FROM (
    SELECT 
        TeamIDs.`Team Name`,
        COUNT(CASE WHEN Matches.`Winner ID` = TeamIDs.`Team ID` THEN Matches.`Match Number` END) AS Wins,
        COUNT(CASE WHEN Matches.`Winner ID` <> TeamIDs.`Team ID` THEN Matches.`Match Number` END) AS Loses
    FROM TeamIDs
    LEFT JOIN Matches ON TeamIDs.`Team ID` = Matches.`Winner ID` OR TeamIDs.`Team ID` = Matches.`Loser ID`

    GROUP BY TeamIDs.`Team Name`
) AS SubQuery;