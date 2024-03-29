-- attribution des rôles pour notre entrepôt de données

-- Création des rôles de mainteneur et de pronostiqueur
PROMPT *** Création des rôles et attribution des droits
CREATE ROLE ADMIN3_MAINTENEUR;
CREATE ROLE ADMIN3_PRONOSTIQUEUR;

-- Droits pour les mainteneurs
GRANT ALL ON FACTS TO ADMIN3_MAINTENEUR;
GRANT ALL ON COUNTRY TO ADMIN3_MAINTENEUR;
GRANT ALL ON LEAGUE TO ADMIN3_MAINTENEUR;
GRANT ALL ON MATCH_DATE TO ADMIN3_MAINTENEUR;
GRANT ALL ON TEAM TO ADMIN3_MAINTENEUR;

-- Droits pour les pronostiqueurs
GRANT SELECT ON FACTS TO ADMIN3_PRONOSTIQUEUR;
GRANT SELECT ON COUNTRY TO ADMIN3_PRONOSTIQUEUR;
GRANT SELECT ON LEAGUE TO ADMIN3_PRONOSTIQUEUR;
GRANT SELECT ON MATCH_DATE TO ADMIN3_PRONOSTIQUEUR;
GRANT SELECT ON TEAM TO ADMIN3_PRONOSTIQUEUR;


PROMPT *** Attribution des droits aux utilisateurs
GRANT ADMIN3_PRONOSTIQUEUR to admin12;
GRANT ADMIN3_MAINTENEUR to admin14;