# Task 1 Data Collection
import requests
import time
import os
import json
from datetime import datetime

# defining HackerNews API endpoints
TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"
HEADERS = {"User-Agent": "TrendPulse/1.0"}

# Defining Categories and keywords
CATEGORIES = {
    "technology": ["AI", "software", "tech", "code", "computer", "data", "cloud", "API", "GPU", "LLM"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["NFL", "NBA", "FIFA", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "NASA", "genome"],
    "entertainment": ["movie", "film", "music", "Netflix", "game", "book", "show", "award", "streaming"]
}

#Creating Function to assign category based on keywords
def assign_category(title):
    title_lower = title.lower()
    for category, keywords in CATEGORIES.items():
        for kw in keywords:
            if kw.lower() in title_lower:
                return category
    return None

# Fetching top 500 story IDs
story_ids = requests.get(TOP_STORIES_URL, headers=HEADERS).json()[:500]

collected = []

# Processing of each category
for category in CATEGORIES.keys():
    count = 0
    for sid in story_ids:
        if count >= 25:  # limit 25 per category
            break
        story = requests.get(ITEM_URL.format(sid), headers=HEADERS).json()
        if not story or "title" not in story:
            continue
        cat = assign_category(story["title"])
        if cat == category:
            collected.append({
                "post_id": story.get("id"),
                "title": story.get("title"),
                "category": cat,
                "score": story.get("score", 0),
                "num_comments": story.get("descendants", 0),
                "author": story.get("by"),
                "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            count += 1
    # Sleep 2 seconds between categories
    time.sleep(2)

#Save the JSON file
os.makedirs("data", exist_ok=True)
filename = f"data/trends_{datetime.now().strftime('%Y%m%d')}.json"
with open(filename, "w", encoding="utf-8") as f:
    json.dump(collected, f, indent=2)

# Final output message
print(f"Collected {len(collected)} stories. Saved to {filename}")