from googleapiclient.discovery import build
import pandas as pd
from datetime import datetime, timezone
import os

# =========================
# CONFIGURATION
# =========================

API_KEY = os.getenv("YT_API_KEY")  # API key from environment variable
CHANNEL_ID = "UC5fcjujOsqD-126Chn_BAuA"
MAX_VIDEOS = 100  # Fetch latest 100 videos

if not API_KEY:
    raise Exception("❌ API key not found. Set YT_API_KEY environment variable.")

# =========================
# YOUTUBE CLIENT
# =========================

youtube = build("youtube", "v3", developerKey=API_KEY)

# =========================
# HELPER FUNCTION
# =========================

def chunk_list(lst, size):
    """Split list into chunks of given size"""
    for i in range(0, len(lst), size):
        yield lst[i:i + size]

# =========================
# STEP 1: FETCH VIDEO IDS
# =========================

video_ids = []
next_page_token = None

while len(video_ids) < MAX_VIDEOS:
    request = youtube.search().list(
        part="id",
        channelId=CHANNEL_ID,
        maxResults=50,
        order="date",
        type="video",
        pageToken=next_page_token
    )
    response = request.execute()

    for item in response["items"]:
        video_ids.append(item["id"]["videoId"])

    next_page_token = response.get("nextPageToken")
    if not next_page_token:
        break

video_ids = video_ids[:MAX_VIDEOS]

print(f"✅ Collected {len(video_ids)} video IDs")

# =========================
# STEP 2: FETCH VIDEO DETAILS (BATCHED)
# =========================

video_data = []

for batch in chunk_list(video_ids, 50):
    request = youtube.videos().list(
        part="snippet,statistics",
        id=",".join(batch)
    )
    response = request.execute()

    for video in response["items"]:
        published_at = video["snippet"]["publishedAt"]
        published_at = datetime.fromisoformat(
            published_at.replace("Z", "+00:00")
        )

        days_since_upload = (
            datetime.now(timezone.utc) - published_at
        ).days

        video_data.append({
            "title": video["snippet"]["title"],
            "published_date": published_at.date(),
            "views": int(video["statistics"].get("viewCount", 0)),
            "likes": int(video["statistics"].get("likeCount", 0)),
            "days_since_upload": days_since_upload
        })

# =========================
# STEP 3: SAVE TO CSV
# =========================

df = pd.DataFrame(video_data)
df.sort_values("published_date", ascending=False, inplace=True)

df.to_csv("sarthak_content_data.csv", index=False)

print("🎉 SUCCESS: sarthak_content_data.csv created")
