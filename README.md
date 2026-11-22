# Google Shopping API (no API key): prices, sellers, discounts and price-drop alerts

Google's Merchant and Content APIs are for merchants managing their own listings, not for reading Google Shopping results. This repo shows how to get **Google Shopping search results as JSON** through the **[Google Shopping Scraper & Price Monitor](https://apify.com/xpandalabs/google-shopping-price-monitor)** on Apify. Call it like an API from Python, JavaScript, cURL, n8n, Make or Zapier: **no API key, no proxies or captchas to manage**.

## What you get

- **Every product on the results page**: price, original price and discount, Google's badge (`LOW PRICE`, `SALE`), seller and "more sellers", delivery and returns, new / used / refurbished, rating and review count.
- **31 countries** with the right Google domain and currency (US, UK, Canada, Australia, Germany, France, Japan, India, Brazil and more).
- **Filters and sorting**: price range, condition, on sale, free delivery, minimum rating, include or exclude sellers, words the title must contain; sort by price, rating, reviews or discount.
- **Price tracking**: each product is compared with your previous run (`changeType` up / down / new, `previousPrice`, `priceChangePct`, `lowestPriceSeen`), plus a target-price flag. With `onlyChanges` you only get, and only pay for, what moved.

## Quick start

1. Create a free [Apify account](https://console.apify.com/sign-up) and copy your API token from **Settings → Integrations**. The free plan includes $5 of monthly credit, about 2,500 products.
2. `pip install apify-client` and `export APIFY_TOKEN=...`
3. Run an example:

| Example | What it does |
|---|---|
| [`examples/python/quickstart.py`](examples/python/quickstart.py) | Every new Sony WH-1000XM5 offer in the US, cheapest first |
| [`examples/python/price_drop_alert.py`](examples/python/price_drop_alert.py) | Daily price-drop and target-price alert |
| [`examples/python/compare_countries.py`](examples/python/compare_countries.py) | Sony WH-1000XM5 in the US, UK, Canada and Australia: median price and top offers |
| [`examples/javascript/quickstart.mjs`](examples/javascript/quickstart.mjs) | Node.js: UK air fryer deals, biggest discount first |
| [`examples/curl/run-sync.sh`](examples/curl/run-sync.sh) | One HTTP request in, JSON rows out |

## Output

A real row: [`sample-output/product-row.json`](sample-output/product-row.json).

| Field | Meaning |
|---|---|
| `title`, `price`, `priceText`, `currency` | The product and its price |
| `originalPrice`, `discountPct`, `discountLabel`, `badge` | Crossed-out or "Usually" price, discount, Google's labels |
| `seller`, `moreSellers` | Store on the card, and whether other stores sell it too |
| `condition`, `isUsedOrRefurbished` | Pre-owned or refurbished offers |
| `delivery`, `freeDelivery`, `returns` | As Google shows them |
| `rating`, `reviewCount` | Product rating and number of reviews |
| `productId`, `position`, `googlePosition` | Google's id; position after your filters and on Google |
| `changeType`, `previousPrice`, `previousSeller`, `priceChangePct`, `lowestPriceSeen`, `belowTargetPrice` | Changes since your previous run |

## Main inputs

| Input | Example |
|---|---|
| `queries` | `["sony wh-1000xm5", "air fryer"]` or Google Shopping links |
| `country` | `"US"`, `"GB"`, `"DE"`, `"JP"`, ... |
| `maxProductsPerQuery`, `sortBy` | `40`, `"price_low"` / `"discount"` / `"rating"` |
| `minPrice`, `maxPrice`, `condition` | `100`, `400`, `"new"` |
| `onlyOnSale`, `onlyFreeDelivery`, `minRating` | `true`, `true`, `"4"` |
| `sellers`, `excludeSellers` | `["walmart"]`, `["ebay"]` |
| `titleMustContain`, `titleMustNotContain` | `["xm5"]`, `["case", "cover"]` |
| `trackChanges`, `onlyChanges`, `targetPrice` | `true`, `true`, `250` |

Full reference: [input schema](https://apify.com/xpandalabs/google-shopping-price-monitor/input-schema).

## Pricing

**$2 per 1,000 products**, **no start fee**, so a 40-product search costs $0.08. Paid Apify plans get up to 30% off. Set a maximum cost per run and the Actor stops at that limit.

## Limits

About 40–120 products per search (what Google Shopping shows), one offer per product card (not every store's price), no direct store links or images, texts in the page language. Details in the [Actor's README](https://apify.com/xpandalabs/google-shopping-price-monitor).

## AI agents and MCP

AI assistants (Claude, ChatGPT, Cursor and others) can call it as a tool through the [Apify MCP server](https://mcp.apify.com?tools=xpandalabs/google-shopping-price-monitor) to answer "where is this cheapest right now?" with live prices.

## Related

- [Google Hotels API](https://github.com/bigxiong001-pixel/google-hotels-api): hotel prices, every booking site's rate, rate parity
- [Google Flights API](https://github.com/bigxiong001-pixel/google-flights-api): flight prices, cheapest destinations, fare calendar
- [Google Trends API](https://github.com/bigxiong001-pixel/google-trends-api): trend verdicts, rising searches, keyword ideas

## Questions

Open an issue on the [Actor's Issues tab](https://apify.com/xpandalabs/google-shopping-price-monitor/issues) or in this repo.

The data is the public Google Shopping results page. You are responsible for using it in line with applicable laws and Google's terms. The code in this repo is MIT-licensed.
