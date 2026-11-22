"""Every Google Shopping offer for a product, cheapest new ones first.

    pip install apify-client
    export APIFY_TOKEN=...   # https://console.apify.com/settings/integrations
    python quickstart.py
"""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("xpandalabs/google-shopping-price-monitor").call(run_input={
    "queries": ["sony wh-1000xm5"],
    "country": "US",
    "condition": "new",
    "titleMustContain": ["xm5"],   # drop accessories and look-alikes
    "sortBy": "price_low",
    "trackChanges": False,
})

for p in client.dataset(run["defaultDatasetId"]).iterate_items():
    was = f" (was {p['originalPrice']:,.2f})" if p.get("originalPrice") else ""
    print(f"{p['price']:>9,.2f} {p['currency']}{was:18} {(p['seller'] or '')[:28]:28} {p['title'][:60]}")
