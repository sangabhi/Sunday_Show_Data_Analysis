import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# LOAD CSV (THIS DEFINES df)
df = pd.read_csv("sarthak_content_data.csv")

# CLEAN COLUMN NAMES
df.columns = df.columns.str.replace("\n", "").str.strip()

# FILTER FOR LOG SCALE (NOW df EXISTS)
df = df[(df["views"] > 0) & (df["likes"] > 0)]

print("DF LOADED. Rows:", df.shape[0])

# BASIC TEST PLOT
plt.figure(figsize=(10,6))
sns.scatterplot(
    data=df,
    x="days_since_upload",
    y="views",
    hue="content_type"
)
plt.yscale("log")
plt.title("Test Lifecycle Plot")
plt.show()
plt.figure(figsize=(12,7))

sns.scatterplot(
    data=df,
    x="days_since_upload",
    y="views",
    hue="content_type",
    alpha=0.6
)

plt.yscale("log")

# Reference lines
plt.axvline(30, color="gray", linestyle="--", alpha=0.5)
plt.axvline(90, color="gray", linestyle="--", alpha=0.5)
plt.axvline(365, color="gray", linestyle="--", alpha=0.5)

plt.text(30, df["views"].max(), "30 days", rotation=90, alpha=0.6)
plt.text(90, df["views"].max(), "90 days", rotation=90, alpha=0.6)
plt.text(365, df["views"].max(), "1 year", rotation=90, alpha=0.6)

plt.title("Content Lifecycle with Time Milestones")
plt.xlabel("Days Since Upload")
plt.ylabel("Total Views (log scale)")
plt.tight_layout()
plt.show()


plt.figure(figsize=(12,7))

sns.scatterplot(
    data=df,
    x="days_since_upload",
    y="views",
    hue="content_type",
    style="content_type",   # 👈 new
    alpha=0.6,
    s=80
)

plt.yscale("log")
plt.title("Content Lifecycle Curve (Color + Shape Encoding)")
plt.xlabel("Days Since Upload")
plt.ylabel("Total Views (log scale)")
plt.tight_layout()
plt.show()



centers = df.groupby("content_type")[["days_since_upload", "views"]].median().reset_index()

plt.figure(figsize=(12,7))

sns.scatterplot(
    data=df,
    x="days_since_upload",
    y="views",
    hue="content_type",
    alpha=0.4
)

# Plot centers
sns.scatterplot(
    data=centers,
    x="days_since_upload",
    y="views",
    hue="content_type",
    markers="X",
    s=300,
    legend=False
)

plt.yscale("log")
plt.title("Content Lifecycle with Median Centers")
plt.xlabel("Days Since Upload")
plt.ylabel("Total Views (log scale)")
plt.tight_layout()
plt.show()



plt.figure(figsize=(12,7))

sns.kdeplot(
    data=df,
    x="days_since_upload",
    hue="content_type",
    fill=True,
    alpha=0.4
)

plt.title("Density of Content Over Time")
plt.xlabel("Days Since Upload")
plt.ylabel("Density")
plt.tight_layout()
plt.show()



plt.figure(figsize=(12,7))

sns.scatterplot(
    data=df,
    x="days_since_upload",
    y="views",
    hue="content_type",
    alpha=0.6,
    s=70
)

plt.yscale("log")

# Lifecycle reference lines
plt.axvline(30, color="grey", linestyle="--", alpha=0.5)
plt.axvline(90, color="grey", linestyle="--", alpha=0.5)
plt.axvline(365, color="grey", linestyle="--", alpha=0.5)

# Text explanations
plt.text(10, df["views"].median(), "Early Spike Zone\n(Trend-driven)", fontsize=9)
plt.text(120, df["views"].median(), "Stability Zone", fontsize=9)
plt.text(400, df["views"].median(), "Long-Tail Zone\n(Evergreen strength)", fontsize=9)

plt.title("Content Lifecycle Curve: How Different Content Ages", fontsize=14)
plt.xlabel("Days Since Upload")
plt.ylabel("Total Views (log scale)")
plt.legend(title="Content Type")
plt.tight_layout()
plt.show()


plt.figure(figsize=(12,7))

sns.scatterplot(
    data=df,
    x="days_since_upload",
    y="views",
    hue="content_type",
    alpha=0.25
)

sns.lineplot(
    data=df,
    x="days_since_upload",
    y="views",
    hue="content_type",
    estimator="median",
    errorbar=None,
    linewidth=3
)

plt.yscale("log")

plt.text(250, df["views"].quantile(0.9),
         "Evergreen keeps accumulating views\n→ compounding effect",
         fontsize=9)

plt.text(30, df["views"].quantile(0.6),
         "Trend content peaks early\n→ fast decay",
         fontsize=9)

plt.title("Typical Growth Direction by Content Type (Median)", fontsize=14)
plt.xlabel("Days Since Upload")
plt.ylabel("Total Views (log scale)")
plt.tight_layout()
plt.show()


plt.figure(figsize=(12,7))

sns.scatterplot(
    data=df,
    x="days_since_upload",
    y="views",
    size="likes",
    sizes=(50, 700),
    hue="content_type",
    alpha=0.6
)

plt.yscale("log")

plt.text(200, df["views"].median(),
         "Large bubbles = strong engagement\nSmall bubbles = passive reach",
         fontsize=9)

plt.title("Reach vs Engagement Across Content Lifecycle", fontsize=14)
plt.xlabel("Days Since Upload")
plt.ylabel("Total Views (log scale)")
plt.tight_layout()
plt.show()


plt.figure(figsize=(10,5))

sns.heatmap(
    pivot,
    annot=True,
    fmt=".0f",
    cmap="YlOrRd"
)

plt.title("Where Each Content Type Performs Best Over Time", fontsize=14)
plt.xlabel("Video Age")
plt.ylabel("Content Type")

plt.text(3.5, 0.5, "Evergreen dominates\nolder buckets",
         fontsize=9, color="black")

plt.tight_layout()
plt.show()
