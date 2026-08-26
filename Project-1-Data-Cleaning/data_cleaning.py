"""
Data Cleaning - Dataset_for_Data_Analytics.xlsx
=================================================
Objectif : nettoyer le dataset brut selon les étapes standard de data cleaning
et produire un fichier propre "Cleaned_Dataset.xlsx".

Étapes réalisées :
  1. Recherche des valeurs manquantes (Missing Values)
  2. Détection et suppression des doublons (Duplicate Records)
  3. Vérification et standardisation du format des dates
  4. Suppression des espaces superflus dans les colonnes texte (Trim)
  5. Vérification que Quantity et UnitPrice sont bien numériques
  6. Vérification / recalcul de TotalPrice = Quantity x UnitPrice
  7. Sauvegarde du résultat sous Cleaned_Dataset.xlsx
"""

import pandas as pd
import numpy as np

INPUT_FILE = "Dataset for Data Analytics.xlsx"
OUTPUT_FILE = "Cleaned_Dataset.xlsx"

report_lines = []


def log(msg):
    print(msg)
    report_lines.append(msg)


# ----------------------------------------------------------------------
# 0. Chargement
# ----------------------------------------------------------------------
df = pd.read_excel(INPUT_FILE)
n_start = len(df)
log(f"[0] Dataset chargé : {n_start} lignes, {df.shape[1]} colonnes")
log(f"    Colonnes : {list(df.columns)}\n")


# ----------------------------------------------------------------------
# 1. Valeurs manquantes (Missing Values)
# ----------------------------------------------------------------------
log("[1] Valeurs manquantes par colonne :")
missing = df.isna().sum()
missing = missing[missing > 0]
if missing.empty:
    log("    Aucune valeur manquante détectée.")
else:
    for col, n in missing.items():
        log(f"    - {col} : {n} valeurs manquantes ({n/n_start:.1%})")

# CouponCode manquant = pas de coupon utilisé (valeur métier légitime, pas une erreur)
if "CouponCode" in df.columns:
    n_missing_coupon = df["CouponCode"].isna().sum()
    df["CouponCode"] = df["CouponCode"].fillna("No Coupon")
    log(f"    -> CouponCode manquant interprété comme 'pas de coupon' : "
        f"{n_missing_coupon} valeurs remplacées par 'No Coupon'\n")

# Pour les autres colonnes essentielles (clés/valeurs numériques), on ne comble pas
# artificiellement : une ligne avec un ID ou un prix manquant sera traitée aux étapes suivantes.


# ----------------------------------------------------------------------
# 2. Doublons (Duplicate Records)
# ----------------------------------------------------------------------
log("[2] Vérification des doublons :")
n_full_dup = df.duplicated().sum()
df = df.drop_duplicates()
log(f"    - Lignes 100% identiques supprimées : {n_full_dup}")

if "OrderID" in df.columns:
    n_id_dup = df.duplicated(subset="OrderID").sum()
    df = df.drop_duplicates(subset="OrderID", keep="first")
    log(f"    - Doublons sur la clé OrderID supprimés : {n_id_dup}\n")


# ----------------------------------------------------------------------
# 3. Format des dates
# ----------------------------------------------------------------------
log("[3] Vérification du format des dates :")
if "Date" in df.columns:
    before_na = df["Date"].isna().sum()
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    after_na = df["Date"].isna().sum()
    newly_invalid = after_na - before_na
    log(f"    - Dates non convertibles en date valide : {newly_invalid}")

    n_before_drop = len(df)
    df = df.dropna(subset=["Date"])
    log(f"    - Lignes supprimées car date invalide : {n_before_drop - len(df)}")

    today = pd.Timestamp.today().normalize()
    n_future = (df["Date"] > today).sum()
    log(f"    - Dates dans le futur détectées : {n_future}")
    log(f"    - Plage de dates finale : {df['Date'].min().date()} -> {df['Date'].max().date()}\n")


# ----------------------------------------------------------------------
# 4. Suppression des espaces superflus (Trim) dans les colonnes texte
# ----------------------------------------------------------------------
log("[4] Nettoyage des espaces dans les colonnes texte :")
text_cols = df.select_dtypes(include=["object", "string"]).columns.tolist()
trimmed_count = 0
for col in text_cols:
    original = df[col].astype("string")
    cleaned = original.str.strip()                        # espaces début/fin
    cleaned = cleaned.str.replace(r"\s+", " ", regex=True)  # espaces multiples internes
    changed = (original != cleaned).fillna(False).sum()
    trimmed_count += changed
    df[col] = cleaned
log(f"    - Colonnes texte traitées : {text_cols}")
log(f"    - Valeurs modifiées (espaces superflus retirés) : {trimmed_count}\n")


# ----------------------------------------------------------------------
# 5. Quantity et UnitPrice doivent être numériques
# ----------------------------------------------------------------------
log("[5] Vérification des types numériques (Quantity, UnitPrice) :")
for col in ["Quantity", "UnitPrice"]:
    before_na = df[col].isna().sum()
    df[col] = pd.to_numeric(df[col], errors="coerce")
    after_na = df[col].isna().sum()
    log(f"    - {col} : {after_na - before_na} valeurs non numériques converties en NaN")

n_before_drop = len(df)
df = df.dropna(subset=["Quantity", "UnitPrice"])
log(f"    - Lignes supprimées (Quantity/UnitPrice invalides) : {n_before_drop - len(df)}")

n_neg_qty = (df["Quantity"] <= 0).sum()
n_neg_price = (df["UnitPrice"] <= 0).sum()
log(f"    - Quantity <= 0 détectées : {n_neg_qty}")
log(f"    - UnitPrice <= 0 détectées : {n_neg_price}")
df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)]
log(f"    - Lignes restantes après filtrage : {len(df)}\n")


# ----------------------------------------------------------------------
# 6. Vérification / recalcul de TotalPrice = Quantity x UnitPrice
# ----------------------------------------------------------------------
log("[6] Vérification de TotalPrice = Quantity x UnitPrice :")
if "TotalPrice" in df.columns:
    recalculated = (df["Quantity"] * df["UnitPrice"]).round(2)
    mismatches = (recalculated != df["TotalPrice"].round(2)).sum()
    log(f"    - Incohérences détectées entre TotalPrice existant et le calcul : {mismatches}")
    df["TotalPrice"] = recalculated
    log("    - TotalPrice recalculé pour toutes les lignes (garantit la cohérence)\n")
else:
    df["TotalPrice"] = (df["Quantity"] * df["UnitPrice"]).round(2)
    log("    - Colonne TotalPrice absente : elle a été créée\n")


# ----------------------------------------------------------------------
# 7. Sauvegarde du fichier nettoyé
# ----------------------------------------------------------------------
df = df.reset_index(drop=True)
df.to_excel(OUTPUT_FILE, index=False)

log("=" * 60)
log(f"RÉSUMÉ : {n_start} lignes au départ -> {len(df)} lignes après nettoyage")
log(f"Fichier sauvegardé : {OUTPUT_FILE}")
log("=" * 60)

with open("cleaning_report.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(report_lines))
