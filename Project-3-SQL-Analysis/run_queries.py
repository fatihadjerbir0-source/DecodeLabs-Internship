"""
Project 3 - SQL Data Analysis (DecodeLabs Internship, Batch 2026)
=====================================================================
Pipeline :
    Cleaned_Dataset.xlsx -> run_queries.py -> ecommerce.db -> queries.sql -> resultats SQL

1. Charge Cleaned_Dataset.xlsx dans une base SQLite locale (ecommerce.db, table "orders")
2. Lit toutes les requetes du fichier queries.sql (chaque requete est precedee
   d'un commentaire "-- TITLE: ...")
3. Execute chaque requete et affiche le resultat (console + fichier texte)

Pas besoin de serveur MySQL/PostgreSQL : SQLite utilise le meme SQL standard
(SELECT, WHERE, GROUP BY, HAVING, ORDER BY). ecommerce.db peut aussi etre
ouvert avec un outil gratuit comme "DB Browser for SQLite" si tu veux
l'explorer visuellement pour tes captures d'ecran.
"""

import re
import sqlite3
import pandas as pd

EXCEL_FILE = "Cleaned_Dataset.xlsx"
DB_FILE = "ecommerce.db"
SQL_FILE = "queries.sql"
RESULTS_FILE = "query_results.txt"

report_lines = []


def log(msg=""):
    print(msg)
    report_lines.append(str(msg))


# ----------------------------------------------------------------------
# 1. Cleaned_Dataset.xlsx -> ecommerce.db
# ----------------------------------------------------------------------
df = pd.read_excel(EXCEL_FILE)
conn = sqlite3.connect(DB_FILE)
df.to_sql("orders", conn, if_exists="replace", index=False)
log(f"[1] {len(df)} lignes chargees dans la table 'orders' -> {DB_FILE}\n")


# ----------------------------------------------------------------------
# 2. Lecture de queries.sql (parsing des blocs "-- TITLE: ..." + requete)
# ----------------------------------------------------------------------
with open(SQL_FILE, "r", encoding="utf-8") as f:
    sql_content = f.read()

pattern = re.compile(r"--\s*TITLE:\s*(.+?)\n(.*?);", re.DOTALL)
queries = pattern.findall(sql_content)
log(f"[2] {len(queries)} requetes trouvees dans {SQL_FILE}\n")


# ----------------------------------------------------------------------
# 3. Execution de chaque requete + affichage du resultat
# ----------------------------------------------------------------------
for i, (title, query) in enumerate(queries, start=1):
    title = title.strip()
    query = query.strip()

    log("=" * 78)
    log(f"Q{i}. {title}")
    log("-" * 78)
    log(query)
    log("-" * 78)

    try:
        result = pd.read_sql_query(query, conn)
        if result.empty:
            log("(aucun resultat)")
        else:
            log(result.to_string(index=False))
    except Exception as e:
        # Cas volontaire de la Section 4 : la requete "FAUX" doit echouer.
        # On affiche l'erreur SQL telle quelle, c'est l'objectif pedagogique.
        log(f"[ERREUR SQL - attendue pour la demo de l'Alias Trap] {e}")

    log("")

conn.close()

with open(RESULTS_FILE, "w", encoding="utf-8") as f:
    f.write("\n".join(report_lines))

log("=" * 78)
log(f"[3] Resultats complets sauvegardes -> {RESULTS_FILE}")
log(f"    Base de donnees reutilisable -> {DB_FILE}")