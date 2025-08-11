from temporalio import activity
from woocommerce import API

@activity.defn
async def fetch_products(creds: dict, fetch_type: str):
    """Fetch data from WooCommerce based on fetch_type (e.g., 'products', 'orders')."""
    wcapi = API(
        url=creds["url"],
        consumer_key=creds["consumer_key"],
        consumer_secret=creds["consumer_secret"],
        wp_api=True,
        version="wc/v3"
    )
    response = wcapi.get(fetch_type)
    return response.json()
