"""Daily Google Shopping price-drop alert for your products.

Run it once a day (cron, or save the input as an Apify task with a schedule). The first run saves a
baseline; later runs return only products whose price moved or that are at or below your target.

    pip install apify-client
    export APIFY_TOKEN=...
    python price_drop_alert.py
"""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("xpandalabs/google-shopping-price-monitor").call(run_input={
    "queries": ["apple airpods pro 3"],
    "country": "US",
    "condition": "new",
    "titleMustContain": ["airpods pro 3"],
    "titleMustNotContain": ["case", "cover", "skin", "ear tips"],
    "onlyChanges": True,      # unchanged products are not returned and not charged
    "targetPrice": 200,
})

for p in client.dataset(run["defaultDatasetId"]).iterate_items():
    if p["changeType"] == "down":
        print(f"DROP   {p['title'][:50]}: {p['previousPrice']} -> {p['price']} {p['currency']} at {p['seller']}"
              f" (was at {p['previousSeller']})")
    elif p["changeType"] == "up":
        print(f"UP     {p['title'][:50]}: {p['previousPrice']} -> {p['price']} {p['currency']}")
    elif p["belowTargetPrice"]:
        print(f"TARGET {p['title'][:50]}: {p['price']} {p['currency']} at {p['seller']}")
