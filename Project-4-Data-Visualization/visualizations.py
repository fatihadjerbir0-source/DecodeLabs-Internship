"""
Project 4 - Data Visualization (DecodeLabs Internship, Batch 2026)
=====================================================================
Applique les 3 piliers du PDF :
  1. The Architect  -> le type de chart decoule de la question business,
                        axes honnetes (zero-baseline), jamais de pie chart
  2. The Editor      -> data-ink ratio maximal, pas de chartjunk, pas de
                        legende (direct labeling), couleur = spotlight
  3. The Storyteller -> titre "action" = la conclusion, pas le sujet,
                        + une ligne "So What" sous chaque graphique

4 insights, 4 fichiers PNG, un insight par slide (regle du PDF : une
slide = un message).
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# ----------------------------------------------------------------------
# Style global : palette sobre + une seule couleur d'accent (spotlight)
# ----------------------------------------------------------------------
GREY = "#B0B0B0"
DARK = "#333333"
ACCENT = "#2F6FED"    # bleu -> insight positif / neutre
ACCENT_WARN = "#D64545"  # rouge -> insight negatif, utilise avec parcimonie

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 12,
    "axes.edgecolor": "#DDDDDD",
    "axes.linewidth": 0.8,
    "figure.facecolor": "white",
    "axes.facecolor": "white",
})


def clean_ax(ax, keep_left_spine=False):
    """Retire le chartjunk : grilles, bordures inutiles."""
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    if not keep_left_spine:
        ax.spines["left"].set_visible(False)
        ax.tick_params(left=False)
    ax.spines["bottom"].set_color("#CCCCCC")
    ax.grid(False)


def add_title_block(fig, action_title, so_what):
    """Titre 'action' en gras + ligne 'So What' en bas, dans le style du PDF."""
    fig.text(0.06, 0.94, action_title, fontsize=15, fontweight="bold",
              color=DARK, wrap=True, ha="left", va="top")
    fig.text(0.06, 0.03, f"So what \u2192 {so_what}", fontsize=10.5,
              color="#555555", style="italic", ha="left", va="bottom")


df = pd.read_excel("Cleaned_Dataset.xlsx")
df["Date"] = pd.to_datetime(df["Date"])


# ============================================================
# INSIGHT 1 : Revenue is down ~19% YoY (base comparable, H1)
# ============================================================
h1 = df[df["Date"].dt.month <= 6].groupby(df["Date"].dt.year)["TotalPrice"].sum()
pct_change = (h1.iloc[-1] / h1.iloc[0] - 1) * 100

fig, ax = plt.subplots(figsize=(9, 5.5))
fig.subplots_adjust(top=0.80, bottom=0.16, left=0.10, right=0.95)

colors = [GREY, GREY, ACCENT_WARN]
ax.plot(h1.index.astype(str), h1.values, color="#CCCCCC", linewidth=2, zorder=1)
ax.scatter(h1.index.astype(str), h1.values, color=colors, s=140, zorder=2)

for x, y in zip(h1.index.astype(str), h1.values):
    ax.annotate(f"${y:,.0f}", (x, y), textcoords="offset points",
                xytext=(0, 14), ha="center", fontsize=11, fontweight="bold", color=DARK)

ax.annotate(f"{pct_change:.0f}%", xy=(h1.index.astype(str)[-1], h1.values[-1]),
            xytext=(-55, -28), textcoords="offset points",
            fontsize=13, fontweight="bold", color=ACCENT_WARN)

ax.set_ylim(0, h1.values.max() * 1.25)
ax.set_xlabel("")
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f"${v/1000:.0f}K"))
clean_ax(ax, keep_left_spine=True)

add_title_block(
    fig,
    f"Revenue is down {abs(pct_change):.0f}% year-over-year (Jan-Jun, comparable basis)",
    "investigate what changed between 2023 and 2025 before planning next year's targets.",
)
fig.savefig("insight_1_revenue_trend.png", dpi=160)
plt.close(fig)


# ============================================================
# INSIGHT 2 : Laptop orders are worth more on average than Phone orders
# (Total revenue by product is almost flat -- $195.6K vs $195.6K for the
#  top two -- so that comparison would be a false "leader" claim. The
#  average order value tells a real, defensible story instead.)
# ============================================================
avg_by_product = df.groupby("Product")["TotalPrice"].mean().sort_values(ascending=True)
top_product = avg_by_product.idxmax()
bottom_product = avg_by_product.idxmin()
gap_pct = (avg_by_product.max() / avg_by_product.min() - 1) * 100

fig, ax = plt.subplots(figsize=(9, 5.5))
fig.subplots_adjust(top=0.80, bottom=0.16, left=0.14, right=0.92)

bar_colors = [ACCENT if p == top_product else GREY for p in avg_by_product.index]
bars = ax.barh(avg_by_product.index, avg_by_product.values, color=bar_colors, height=0.6)

for bar, val in zip(bars, avg_by_product.values):
    ax.text(val + avg_by_product.max() * 0.015, bar.get_y() + bar.get_height() / 2,
            f"${val:,.0f}", va="center", fontsize=10.5, color=DARK)

ax.set_xlim(0, avg_by_product.max() * 1.18)
ax.xaxis.set_visible(False)
clean_ax(ax, keep_left_spine=False)

add_title_block(
    fig,
    f"{top_product} orders are worth {gap_pct:.0f}% more on average than {bottom_product} orders",
    "feature high-value products like this one more prominently in upsell and bundle offers.",
)
fig.savefig("insight_2_avg_order_value_by_product.png", dpi=160)
plt.close(fig)


# ============================================================
# INSIGHT 3 : 2 in 5 orders never complete successfully
# ============================================================
status = df["OrderStatus"].value_counts()
status_pct = (status / status.sum() * 100).sort_values(ascending=True)
problem_statuses = ["Cancelled", "Returned"]

fig, ax = plt.subplots(figsize=(9, 5.5))
fig.subplots_adjust(top=0.80, bottom=0.16, left=0.16, right=0.92)

bar_colors = [ACCENT_WARN if s in problem_statuses else GREY for s in status_pct.index]
bars = ax.barh(status_pct.index, status_pct.values, color=bar_colors, height=0.6)

for bar, val in zip(bars, status_pct.values):
    ax.text(val + 1, bar.get_y() + bar.get_height() / 2,
            f"{val:.1f}%", va="center", fontsize=10.5, color=DARK)

problem_total = status_pct[problem_statuses].sum()
ax.set_xlim(0, status_pct.max() * 1.25)
ax.xaxis.set_visible(False)
clean_ax(ax, keep_left_spine=False)

add_title_block(
    fig,
    f"{problem_total:.0f}% of orders end up cancelled or returned",
    "audit the checkout and fulfillment flow -- this is lost revenue, not just a support cost.",
)
fig.savefig("insight_3_order_status.png", dpi=160)
plt.close(fig)


# ============================================================
# INSIGHT 4 : Credit Card customers spend the most per order
# ============================================================
avg_val = df.groupby("PaymentMethod")["TotalPrice"].mean().sort_values(ascending=True)
top_pm = avg_val.idxmax()
bottom_pm = avg_val.idxmin()
gap = avg_val.max() - avg_val.min()

fig, ax = plt.subplots(figsize=(9, 5.5))
fig.subplots_adjust(top=0.80, bottom=0.16, left=0.16, right=0.92)

bar_colors = [ACCENT if p == top_pm else GREY for p in avg_val.index]
bars = ax.barh(avg_val.index, avg_val.values, color=bar_colors, height=0.6)

for bar, val in zip(bars, avg_val.values):
    ax.text(val + avg_val.max() * 0.015, bar.get_y() + bar.get_height() / 2,
            f"${val:,.0f}", va="center", fontsize=10.5, color=DARK)

ax.set_xlim(0, avg_val.max() * 1.18)
ax.xaxis.set_visible(False)
clean_ax(ax, keep_left_spine=False)

add_title_block(
    fig,
    f"{top_pm} orders are worth ${gap:,.0f} more on average than {bottom_pm} orders",
    "consider incentivizing Credit Card at checkout to lift average order value.",
)
fig.savefig("insight_4_avg_order_value_by_payment.png", dpi=160)
plt.close(fig)

print("4 fichiers PNG generes.")
