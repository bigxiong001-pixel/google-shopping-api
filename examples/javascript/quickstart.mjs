// npm i apify-client && APIFY_TOKEN=... node quickstart.mjs
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('xpandalabs/google-shopping-price-monitor').call({
    queries: ['air fryer'],
    country: 'GB',
    onlyOnSale: true,
    sortBy: 'discount',
    trackChanges: false,
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const p of items) console.log(`${p.priceText}  -${p.discountPct ?? '?'}%  ${p.seller}  ${p.title.slice(0, 60)}`);
