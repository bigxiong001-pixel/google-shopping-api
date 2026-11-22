#!/bin/sh
# One HTTP request in, JSON products out (waits for the run to finish).
curl -s -X POST \
  "https://api.apify.com/v2/acts/xpandalabs~google-shopping-price-monitor/run-sync-get-dataset-items" \
  -H "Authorization: Bearer $APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"queries": ["sony wh-1000xm5"], "country": "US", "maxProductsPerQuery": 20, "trackChanges": false}'
