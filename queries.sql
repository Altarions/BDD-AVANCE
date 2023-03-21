/*
    Queries for the data warehouse - 03-2023
*/

-- Nombre de match par mois sur l'année 2016 avec le cumul
SELECT md.month, COUNT(*) as nb_match,
    SUM(COUNT(*))
    OVER (order by md.month
    ROWS UNBOUNDED PRECEDING) as cumul
FROM ADMI3.Match_Date md NATURAL JOIN ADMI3.FACTS f
WHERE md.year = '2016' AND f.type = 'possession'
GROUP BY md.month;



-- Tous les matchs et l'équipe qui les ont gagné --

SELECT f.match_id, COUNT(*) as nbGoals, COUNT(CASE WHEN f.away_team_id = f.involved_team_id THEN 1 END) awayGoals, COUNT(CASE WHEN f.home_team_id = f.involved_team_id THEN 1 END) homeGoals,
CASE
	WHEN COUNT(CASE WHEN f.away_team_id = f.involved_team_id THEN 1 END) > COUNT(CASE WHEN f.home_team_id = f.involved_team_id THEN 1 END) THEN f.away_team_id
	WHEN COUNT(CASE WHEN f.away_team_id = f.involved_team_id THEN 1 END) < COUNT(CASE WHEN f.home_team_id = f.involved_team_id THEN 1 END) THEN f.home_team_id
	ELSE Null
END as Winner
FROM facts f INNER JOIN Team t on f.involved_team_id = t.team_id
WHERE f.type='goal'
GROUP BY f.match_id, f.away_team_id, f.home_team_id;




-- Nombre de fautes, par équipe et par année --

SELECT COUNT(*) as nbFautes, t.teamLongName
FROM Date d NATURAL JOIN Faits f INNER JOIN Team t ON t.teamId = f.involvedTeam 
WHERE f.type = 'foulcommit'
GROUP BY CUBE (d.year, teamId);



-- Dans quel championnat y’a t’il le plus de fautes ? --

SELECT COUNT(*) Nombre_de_fautes, l.name Ligue, RANK() OVER(ORDER BY COUNT(*)) rank 
FROM facts f NATURAL JOIN league l
WHERE f.type = 'foulcommit'
GROUP BY l.name;


-- Dans quel championnat y’a t’il le plus de buts ? --

SELECT COUNT(*) Nombre_de_buts, l.name Ligue, RANK() OVER(ORDER BY COUNT(*)) rank 
FROM facts f NATURAL JOIN league l
WHERE f.type = 'goal'
GROUP BY l.name;


-- Dans quel championnat y’a t’il le plus de tirs ? --

SELECT COUNT(*) Nombre_de_tirs, l.name Ligue, RANK() OVER(ORDER BY COUNT(*)) rank 
FROM facts f NATURAL JOIN league l
WHERE f.type = 'shoton' or f.type = 'shotoff'
GROUP BY l.name;

