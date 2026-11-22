"""Same product, several countries: typical Google Shopping price and the top offers in each.

Google ranks real offers of the product first; the very lowest prices are often marketplace
listings or accessories, so this looks at the median price and Google's top 3 instead.

    pip install apify-client
    export APIFY_TOKEN=...
    python compare_countries.py
"""
import os
import statistics

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
for country in ["US", "GB", "CA", "AU"]:
    run = client.actor("xpandalabs/google-shopping-price-monitor").call(run_input={
        "queries": ["sony wh-1000xm5"], "country": country, "condition": "new",
        "titleMustContain": ["xm5"], "titleMustNotContain": ["case", "cover", "cushion", "ear pads", "replacement", "skin"],
        "maxProductsPerQuery": 40, "trackChanges": False,
    })
    rows = [r for r in client.dataset(run["defaultDatasetId"]).iterate_items() if r["price"]]
    if not rows:
        continue
    median = statistics.median(r["price"] for r in rows)
    top = ", ".join(f"{r['priceText']} {r['seller']}" for r in rows[:3])
    print(f"{country}: median {median:,.2f} {rows[0]['currency']} over {len(rows)} offers | top: {top}")
