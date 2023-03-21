/*
    Queries for the data warehouse - 03-2023
*/

-- Nombre de match par mois sur l'année 2016 avec le cumul --
SELECT md.month, COUNT(*) as nb_match,
    SUM(COUNT(*))
    OVER (order by md.month
    ROWS UNBOUNDED PRECEDING) as cumul
FROM ADMI3.Match_Date md NATURAL JOIN ADMI3.FACTS f
WHERE md.year = '2015' AND f.type = 'possession'
GROUP BY md.month;



-- Tous les matchs et l'equipe qui les ont gagne --

SELECT f.match_id, COUNT(*) as nbGoals, COUNT(CASE WHEN f.away_team_id = f.involved_team_id THEN 1 END) awayGoals, COUNT(CASE WHEN f.home_team_id = f.involved_team_id THEN 1 END) homeGoals,
CASE
	WHEN COUNT(CASE WHEN f.away_team_id = f.involved_team_id THEN 1 END) > COUNT(CASE WHEN f.home_team_id = f.involved_team_id THEN 1 END) THEN f.away_team_id
	WHEN COUNT(CASE WHEN f.away_team_id = f.involved_team_id THEN 1 END) < COUNT(CASE WHEN f.home_team_id = f.involved_team_id THEN 1 END) THEN f.home_team_id
	ELSE Null
END as Winner
FROM facts f INNER JOIN Team t on f.involved_team_id = t.team_id
WHERE f.type='goal'
GROUP BY f.match_id, f.away_team_id, f.home_team_id;




-- Nombre de fautes, par equipe et par annee --


SELECT t.team_id, COUNT(*) as nbFautes 
FROM match_date d NATURAL JOIN Facts f INNER JOIN Team t ON t.team_id = f.involved_team_id
WHERE f.type = 'foulcommit'
GROUP BY CUBE (d.year, t.team_id);



-- Dans quel championnat y a t il le plus de fautes ?


SELECT COUNT(*) Nombre_de_fautes, l.name Ligue, RANK() OVER(ORDER BY COUNT(*)) rank
FROM facts f NATURAL JOIN league l
WHERE f.type = 'foulcommit'
GROUP BY l.name;



-- Dans quel championnat y a t il le plus de buts ?

SELECT  l.name Ligue, COUNT(*) Nombre_de_buts, RANK() OVER(ORDER BY COUNT(*)) rank
FROM facts f NATURAL JOIN league l
WHERE f.type = 'goal'
GROUP BY l.name;


-- Dans quel championnat y a t il le plus de tirs ?

SELECT  l.name Ligue, COUNT(*) Nombre_de_tirs, RANK() OVER(ORDER BY COUNT(*)) rank
FROM facts f NATURAL JOIN league l
WHERE f.type = 'shoton' or f.type = 'shotoff'
GROUP BY l.name;

-- Compte le nombre total de victoire par équipe (et crée pour ça une vue)

CREATE VIEW match_victoire AS
SELECT f.match_id,
    CASE
        WHEN COUNT(CASE WHEN f.away_team_id = f.involved_team_id THEN 1 END) > COUNT(CASE WHEN f.home_team_id = f.involved_team_id THEN 1 END) THEN f.away_team_id
        WHEN COUNT(CASE WHEN f.away_team_id = f.involved_team_id THEN 1 END) < COUNT(CASE WHEN f.home_team_id = f.involved_team_id THEN 1 END) THEN f.home_team_id
        ELSE Null
    END as Winner
    FROM facts f INNER JOIN Team t on f.involved_team_id = t.team_id
    WHERE f.type='goal'
    GROUP BY f.match_id, f.away_team_id, f.home_team_id;

SELECT t.team_long_name, mv.winner,COUNT(*) nbVictoires
FROM match_victoire mv JOIN team t ON t.team_id = mv.winner
GROUP BY t.team_long_name,mv.winner;

-- Affiche le nombre de cartons et de victoires de chaque equipe

CREATE VIEW carton_equipe AS
SELECT COUNT(*) as nbCartons, t.team_id , t.team_long_name
FROM match_date d NATURAL JOIN Facts f INNER JOIN Team t ON t.team_id = f.involved_team_id
WHERE f.type = 'card'
GROUP BY t.team_id, t.team_long_name;

CREATE VIEW carton_equipe_par_match AS
SELECT f.match_id, t.team_id, t.team_long_name, COUNT(*) as nbCartonsParMatch
FROM Facts f INNER JOIN Team t ON t.team_id = f.involved_team_id
WHERE f.type = 'card'
GROUP BY t.team_id, t.team_long_name, f.match_id;

CREATE VIEW equipe_victoire AS
SELECT t.team_long_name, mv.winner,COUNT(*) nbVictoires
FROM match_victoire mv JOIN team t ON t.team_id = mv.winner
GROUP BY t.team_long_name,mv.winner;

SELECT ce.team_long_name, ce.team_id, ev.nbvictoires, ce.nbcartons
FROM Facts f NATURAL JOIN equipe_victoire ev JOIN carton_equipe ce ON ce.team_id = ev.winner
WHERE f.type = 'card'
GROUP BY ce.team_long_name,ce.team_id, ev.nbvictoires, ce.nbcartons
ORDER BY ce.nbcartons DESC;

-- nb but par équipe --
SELECT team.team_long_name, facts.match_id, count(CASE WHEN type='goal' AND involved_team_id = home_team_id THEN 1 WHEN type='goal' AND involved_team_id = away_team_id THEN 1 END) AS Goal
FROM team JOIN facts ON team.team_id = facts.involved_team_id
GROUP BY CUBE (team_long_name, match_id);

-- nb de victoire en fonction du jour de la semaine --
SELECT t.team_long_name, md.weekday,COUNT(*) nbVictoires
FROM match_victoire mv JOIN team t ON t.team_id = mv.winner JOIN match_date md ON md.match_date=mv.match_date
GROUP BY CUBE (t.team_long_name, md.weekday);

