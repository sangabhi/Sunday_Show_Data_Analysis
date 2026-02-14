# Content Lifecycle Analysis of a YouTube Channel

This project analyzes how different types of YouTube content perform over time, with a focus on **short-term spikes vs long-term value**.  
The goal is to understand which content types contribute to sustainable growth and which are primarily driven by immediate trends.

---

## 📌 Objective

Creators often intuitively feel that some videos perform only briefly while others keep gaining views over time.  
This project aims to **quantify that intuition using data** by answering:

- Which content types have long-term (long-tail) value?
- Which content types peak early and decay quickly?
- How do reach and engagement differ across content types?

---

## 📊 Data Source

- Data was collected using the **official YouTube Data API**
- Only **publicly available information** was used
- No private analytics or restricted data was accessed

### Extracted Fields
- Video title  
- Publish date  
- Total views  
- Total likes  
- Days since upload (computed)

The processed data is stored in:



---

## 🧠 Content Categorization

Each video was manually categorized into one of the following types based on **time relevance and intent**:

- **Evergreen**  
  Content that remains relevant over long periods (conceptual, explanatory, systemic topics)

- **Trend**  
  Content tied to current events, news cycles, or time-sensitive topics

- **Opinion**  
  Personal commentary, reactions, or viewpoint-driven content

This step required **human judgment**, as automated metrics alone cannot capture content intent.

---

## 🔬 Methodology

1. Collect public video data via YouTube Data API  
2. Compute `days_since_upload` for lifecycle analysis  
3. Categorize videos into content types  
4. Visualize performance using time-based and engagement-based plots  
5. Compare short-term vs long-term behavior across content types  

All analysis was performed using **Python**, primarily with:
- Pandas
- Matplotlib
- Seaborn

---

## 📈 Key Visualizations

### 1. Content Lifecycle Curve (Log Scale)
Shows how total views change as videos age.

**Insight:**  
Trend content spikes early but fades quickly, while evergreen content continues accumulating views over long periods.

---

### 2. Median Growth Direction
Shows the typical lifecycle behavior (median trend) for each content type.

**Insight:**  
Evergreen content exhibits sustained long-term growth, whereas trend content plateaus early.

---

### 3. Reach vs Engagement (Bubble Chart)
Bubble size represents likes, acting as a proxy for engagement.

**Insight:**  
High reach does not always imply high engagement; some videos attract views without strong interaction.

---

### 4. Long-Tail Performance Heatmap
Shows how each content type performs across different age buckets.

**Insight:**  
Evergreen content dominates older time buckets, highlighting its long-term strategic value.

---

## 🧩 Key Findings

- **Trend content** is effective for quick reach but has a short lifespan  
- **Evergreen content** provides sustained, long-term value and authority  
- **Opinion content** sits between trend and evergreen, with moderate longevity  
- A balanced content strategy benefits from using trends for discovery and evergreen for compounding growth  

---


