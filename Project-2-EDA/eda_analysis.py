"""
Project 2 - Exploratory Data Analysis (EDA)
=============================================
Pipeline suivi :
Dataset -> Data Understanding -> Descriptive Statistics -> Distributions
-> Correlation Analysis -> Trend Analysis -> Outlier Detection
-> Key Insights -> Visualizations

Input  : Cleaned_Dataset.xlsx (sortie du Projet 1 - Data Cleaning)
Outputs: charts/*.png  +  eda_report.txt (statistiques + insights)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

INPUT_FILE = "Cleaned_Dataset.xlsx"
CHART_DIR = "charts"
os.makedirs(CHART_DIR, exist_ok=True)

sns.set_style("whitegrid")
plt.rcParams["figure.dpi"] = 120
plt.rcParams["font.size"] = 10

report_lines = []


def log(msg=""):
    print(msg)
    report_lines.append(str(msg))


def save_fig(fig, name):
    path = os.path.join(CHART_DIR, name)
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)
    log(f"    -> graphique sauvegardé : {path}")


NUMERIC_COLS = ["Quantity", "UnitPrice", "TotalPrice", "ItemsInCart"]
CATEGORICAL_COLS = ["Product", "PaymentMethod", "OrderStatus", "CouponCode", "ReferralSource"]


# ============================================================
# 0. DATA UNDERSTANDING
# ============================================================
log("=" * 70)
log("0. DATA UNDERSTANDING")
log("=" * 70)

df = pd.read_excel(INPUT_FILE)
df["Date"] = pd.to_datetime(df["Date"])

log(f"Nombre de lignes  : {df.shape[0]}")
log(f"Nombre de colonnes: {df.shape[1]}")
log(f"Période couverte  : {df['Date'].min().date()} -> {df['Date'].max().date()}")
log(f"Colonnes          : {list(df.columns)}")
log("")
log("Variables numériques   : " + ", ".join(NUMERIC_COLS))
log("Variables catégorielles: " + ", ".join(CATEGORICAL_COLS))
log("")


# ============================================================
# 1. DESCRIPTIVE / BASIC STATISTICS (mean, median, count, ...)
# ============================================================
log("=" * 70)
log("1. BASIC STATISTICS (mean, median, count, std, min, max)")
log("=" * 70)

stats_table = df[NUMERIC_COLS].agg(["count", "mean", "median", "std", "min", "max"]).T
stats_table = stats_table.round(2)
log(stats_table.to_string())
log("")

# Statistiques par catégorie (utile pour les insights)
log("Nombre de commandes par produit :")
log(df["Product"].value_counts().to_string())
log("")
log("Chiffre d'affaires total par produit :")
revenue_by_product = df.groupby("Product")["TotalPrice"].sum().sort_values(ascending=False).round(2)
log(revenue_by_product.to_string())
log("")
log("Panier moyen (TotalPrice) par mode de paiement :")
log(df.groupby("PaymentMethod")["TotalPrice"].mean().round(2).sort_values(ascending=False).to_string())
log("")
log("Répartition des commandes par statut :")
log(df["OrderStatus"].value_counts().to_string())
log("")

stats_table.to_csv("descriptive_statistics.csv")
log("Tableau complet exporté -> descriptive_statistics.csv")
log("")


# ============================================================
# 2. DISTRIBUTIONS
# ============================================================
log("=" * 70)
log("2. DISTRIBUTIONS")
log("=" * 70)

# 2.1 Histogrammes des variables numériques
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
for ax, col in zip(axes.flatten(), NUMERIC_COLS):
    sns.histplot(df[col], kde=True, ax=ax, color="#2F5496")
    ax.set_title(f"Distribution de {col}")
fig.suptitle("Distributions des variables numériques", fontsize=14)
fig.tight_layout()
save_fig(fig, "01_distributions_numeriques.png")

# 2.2 Répartition des variables catégorielles
fig, axes = plt.subplots(2, 3, figsize=(16, 9))
for ax, col in zip(axes.flatten(), CATEGORICAL_COLS):
    order = df[col].value_counts().index
    sns.countplot(y=df[col], order=order, ax=ax, color="#2F5496")
    ax.set_title(col)
    ax.set_xlabel("Nombre de commandes")
axes.flatten()[-1].axis("off")
fig.suptitle("Répartition des variables catégorielles", fontsize=14)
fig.tight_layout()
save_fig(fig, "02_distributions_categorielles.png")
log("")


# ============================================================
# 3. CORRELATION ANALYSIS
# ============================================================
log("=" * 70)
log("3. CORRELATION ANALYSIS")
log("=" * 70)

corr = df[NUMERIC_COLS].corr().round(2)
log(corr.to_string())
log("")

fig, ax = plt.subplots(figsize=(6, 5))
sns.heatmap(corr, annot=True, cmap="coolwarm", center=0, ax=ax, vmin=-1, vmax=1)
ax.set_title("Matrice de corrélation")
fig.tight_layout()
save_fig(fig, "03_correlation_heatmap.png")

# Interprétation automatique des corrélations fortes/faibles
log("Interprétation :")
for i, c1 in enumerate(NUMERIC_COLS):
    for c2 in NUMERIC_COLS[i + 1:]:
        r = corr.loc[c1, c2]
        force = "forte" if abs(r) >= 0.7 else "modérée" if abs(r) >= 0.4 else "faible"
        log(f"    - {c1} vs {c2} : r = {r} ({force})")
log("")


# ============================================================
# 4. TREND ANALYSIS
# ============================================================
log("=" * 70)
log("4. TREND ANALYSIS")
log("=" * 70)

df["YearMonth"] = df["Date"].dt.to_period("M").astype(str)
monthly = df.groupby("YearMonth").agg(
    Revenue=("TotalPrice", "sum"),
    Orders=("OrderID", "count"),
    AvgOrderValue=("TotalPrice", "mean"),
).round(2)

log("Évolution mensuelle (extrait) :")
log(monthly.head(6).to_string())
log("...")
log("")

fig, axes = plt.subplots(2, 1, figsize=(13, 8), sharex=True)
axes[0].plot(monthly.index, monthly["Revenue"], marker="o", color="#2F5496")
axes[0].set_title("Chiffre d'affaires mensuel")
axes[0].set_ylabel("Revenue")
axes[0].tick_params(axis="x", rotation=90)

axes[1].plot(monthly.index, monthly["Orders"], marker="o", color="#C0504D")
axes[1].set_title("Nombre de commandes par mois")
axes[1].set_ylabel("Orders")
axes[1].tick_params(axis="x", rotation=90)

fig.tight_layout()
save_fig(fig, "04_tendances_mensuelles.png")

# Tendance par année
df["Year"] = df["Date"].dt.year
yearly = df.groupby("Year").agg(Revenue=("TotalPrice", "sum"), Orders=("OrderID", "count")).round(2)
log("Évolution annuelle (attention : 2025 est une année partielle, seulement Jan-Juin) :")
log(yearly.to_string())
log("")

# Comparaison à périmètre identique (Jan-Juin) pour ne pas biaiser par l'année 2025 incomplète
h1 = df[df["Date"].dt.month <= 6].groupby("Year").agg(
    Revenue_H1=("TotalPrice", "sum"), Orders_H1=("OrderID", "count")
).round(2)
log("Comparaison Jan-Juin (1er semestre) par année, pour une base comparable :")
log(h1.to_string())
h1_trend_pct = (h1["Revenue_H1"].iloc[-1] / h1["Revenue_H1"].iloc[0] - 1) * 100
log(f"-> Variation du CA sur Jan-Juin entre {h1.index[0]} et {h1.index[-1]} : {h1_trend_pct:.1f}%")
log("")

# Tendance : source de trafic la plus utilisée dans le temps
fig, ax = plt.subplots(figsize=(11, 5))
trend_source = df.groupby(["Year", "ReferralSource"])["OrderID"].count().unstack()
trend_source.plot(kind="bar", stacked=True, ax=ax, colormap="tab10")
ax.set_title("Sources de commande par année")
ax.set_ylabel("Nombre de commandes")
fig.tight_layout()
save_fig(fig, "05_sources_par_annee.png")
log("")


# ============================================================
# 5. OUTLIER DETECTION (méthode IQR)
# ============================================================
log("=" * 70)
log("5. OUTLIER DETECTION (méthode IQR)")
log("=" * 70)

outlier_summary = {}
for col in NUMERIC_COLS:
    q1, q3 = df[col].quantile([0.25, 0.75])
    iqr = q3 - q1
    lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    outliers = df[(df[col] < lower) | (df[col] > upper)]
    outlier_summary[col] = len(outliers)
    log(f"{col} : bornes normales [{lower:.2f} ; {upper:.2f}] -> {len(outliers)} outliers ({len(outliers)/len(df):.1%})")

log("")

fig, axes = plt.subplots(1, 4, figsize=(15, 5))
for ax, col in zip(axes, NUMERIC_COLS):
    sns.boxplot(y=df[col], ax=ax, color="#9DC3E6")
    ax.set_title(col)
fig.suptitle("Détection des outliers (boxplots)", fontsize=14)
fig.tight_layout()
save_fig(fig, "06_outliers_boxplots.png")
log("")


# ============================================================
# 6. KEY INSIGHTS
# ============================================================
log("=" * 70)
log("6. KEY INSIGHTS")
log("=" * 70)

top_product = revenue_by_product.idxmax()
top_product_share = revenue_by_product.max() / revenue_by_product.sum()
top_payment = df.groupby("PaymentMethod")["TotalPrice"].mean().idxmax()
best_month = monthly["Revenue"].idxmax()
worst_month = monthly["Revenue"].idxmin()
cancel_rate = (df["OrderStatus"] == "Cancelled").mean()
return_rate = (df["OrderStatus"] == "Returned").mean()
coupon_usage_rate = (df["CouponCode"] != "No Coupon").mean()
strongest_corr_pair = corr.where(~np.eye(len(corr), dtype=bool)).abs().stack().idxmax()
strongest_corr_val = corr.loc[strongest_corr_pair]

insights = [
    f"- Le produit générant le plus de chiffre d'affaires est '{top_product}' "
    f"({top_product_share:.1%} du CA total).",

    f"- Le mode de paiement associé au panier moyen le plus élevé est '{top_payment}'.",

    f"- Le mois le plus performant en CA est {best_month}, le plus faible est {worst_month} "
    f"-> il y a une variation temporelle notable des ventes.",

    f"- En comparant les 1ers semestres (Jan-Juin) de {h1.index[0]} à {h1.index[-1]} sur une base "
    f"comparable, le CA baisse de {h1_trend_pct:.1f}% -> tendance réellement baissière, "
    "pas juste un artefact d'année 2025 incomplète.",

    f"- Taux de commandes annulées : {cancel_rate:.1%} ; taux de retours : {return_rate:.1%}.",

    f"- {coupon_usage_rate:.1%} des commandes utilisent un coupon de réduction.",

    f"- La corrélation la plus forte est entre {strongest_corr_pair[0]} et {strongest_corr_pair[1]} "
    f"(r = {strongest_corr_val:.2f}) -- logique puisque TotalPrice est directement dérivé de ces variables.",

    f"- Outliers détectés (méthode IQR) : " +
    ", ".join(f"{col} ({n})" for col, n in outlier_summary.items()) +
    ". Ces valeurs correspondent à de grosses commandes (quantité ou prix élevés), "
    "pas nécessairement à des erreurs -- à vérifier au cas par cas plutôt qu'à supprimer automatiquement.",
]

for line in insights:
    log(line)
log("")

with open("eda_report.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(report_lines))

log("=" * 70)
log("Rapport complet exporté -> eda_report.txt")
log("6 graphiques exportés dans le dossier -> charts/")
log("=" * 70)
