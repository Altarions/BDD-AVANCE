--Tentative de VPD pour notre entrepôt de données


-- Les rôles ont été correctement attribués mais les privilèges liés à ces rôles ne fonctionnent pas

PROMPT *** Suppression de tous les rôles, du contexte et de la politique VPD
EXECUTE DBMS_RLS.DROP_POLICY('ADMI3','FACTS','FACTS_POLICY');
DROP ROLE MAINTENEUR;
DROP ROLE PRONOSTIQUEUR_TOUS_PAYS;
DROP ROLE PRONOSTIQUEUR_FRANCE;
DROP ROLE PRONOSTIQUEUR_PAYS_BAS;


-- Initialisation du contexte d'application utilisé dans cette VPD
CREATE OR REPLACE CONTEXT pronostiqueur_ctx USING set_pronostiqueur_ctx_pkg;

CREATE OR REPLACE PACKAGE set_pronostiqueur_ctx_pkg IS
	PROCEDURE set_prono;
END;
/

CREATE OR REPLACE PACKAGE BODY set_pronostiqueur_ctx_pkg IS
	PROCEDURE set_prono IS
		role_var VARCHAR2(100);
    BEGIN

    -- Requête permettant de récupérer le rôle de l'utilisateur qui est connecté
		SELECT granted_role INTO role_var
		FROM DBA_ROLE_PRIVS 
		WHERE granted_role like 'ADMI3%' AND GRANTEE=user 
		AND ROWNUM=1;

	-- Initialisation de la variable role du contexte
		DBMS_SESSION.SET_CONTEXT('pronostiqueur_ctx', 'role_nom', role_var);

	-- Si pas de données alors NULL
		EXCEPTION
			WHEN NO_DATA_FOUND THEN NULL;

     END set_prono;
END set_pronostiqueur_ctx_pkg;
/
SHOW ERROR;


-- Création des rôles de mainteneur et de pronostiqueur
PROMPT *** Création des rôles et attribution des droits
CREATE ROLE MAINTENEUR;
CREATE ROLE PRONOSTIQUEUR_TOUS_PAYS;
CREATE ROLE PRONOSTIQUEUR_FRANCE;
CREATE ROLE PRONOSTIQUEUR_PAYS_BAS;

-- Droits pour les mainteneurs
GRANT ALL ON FACTS TO MAINTENEUR;
GRANT ALL ON COUNTRY TO MAINTENEUR;
GRANT ALL ON LEAGUE TO MAINTENEUR;
GRANT ALL ON MATCH_DATE TO MAINTENEUR;
GRANT ALL ON TEAM TO MAINTENEUR;

-- Droits pour les pronostiqueurs voyant les événements de toutes les ligues présentes
GRANT SELECT ON FACTS TO PRONOSTIQUEUR_TOUS_PAYS;
GRANT SELECT ON COUNTRY TO PRONOSTIQUEUR_TOUS_PAYS;
GRANT SELECT ON LEAGUE TO PRONOSTIQUEUR_TOUS_PAYS;
GRANT SELECT ON MATCH_DATE TO PRONOSTIQUEUR_TOUS_PAYS;
GRANT SELECT ON TEAM TO PRONOSTIQUEUR_TOUS_PAYS;

-- Droits pour les pronostiqueurs voyant les événements d'une seule ligue
GRANT SELECT ON FACTS TO PRONOSTIQUEUR_FRANCE;
GRANT SELECT ON COUNTRY TO PRONOSTIQUEUR_FRANCE; 
GRANT SELECT ON FACTS TO PRONOSTIQUEUR_PAYS_BAS;

-- UTILISER UN CONTEXTE ??
-- UTILISER UN PACKAGE ??
-- UTILISER UN PACKAGE BODY ??
-- FAIRE LA FONCTION POUR LA POLICY_FUNCTION

PROMPT *** Création de la fonction qui crée le prédicat qui sera ajouté aux requêtes utilisateur
CREATE OR REPLACE FUNCTION PRONO_RES(
	schema_var IN VARCHAR2,
	table_var IN VARCHAR2)
	RETURN VARCHAR2
	IS
		return_val VARCHAR2 (400);
		le_role VARCHAR2(100);
	BEGIN	
		le_role :=SYS_CONTEXT('pronostiqueur_ctx','role_nom');
		IF le_role = 'PRONOSTIQUEUR_FRANCE' THEN
			return_val := 'ADMI3.country = France';
		END IF;
		RETURN return_val;
	END PRONO_RES;
/
 
BEGIN
	DBMS_RLS.ADD_POLICY (
		OBJECT_SCHEMA => 'ADMI3',
		OBJECT_NAME => 'FACTS',
		POLICY_NAME => 'FACTS_POLICY',
		FUNCTION_SCHEMA => 'ADMI3',
		POLICY_FUNCTION => 'PRONO_RES',
		STATEMENT_TYPES => 'SELECT, UPDATE, DELETE'
	);
END;
/

PROMPT *** Attribution des droits aux utilisateurs
GRANT PRONOSTIQUEUR_FRANCE to admin12;
GRANT PRONOSTIQUEUR_FRANCE to admi12;
GRANT PRONOSTIQUEUR_FRANCE to admin14;
GRANT PRONOSTIQUEUR_TOUS_PAYS to admin3;
