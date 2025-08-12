from temporalio import activity
from woocommerce import API
import csv

@activity.defn
async def fetch_products(creds: dict, fetch_type: str):
    """Fetch data from WooCommerce and save to CSV."""
    wcapi = API(
        url=creds["url"],
        consumer_key=creds["consumer_key"],
        consumer_secret=creds["consumer_secret"],
        wp_api=True,
        version="wc/v3"
    )
    
    # Get WooCommerce data
    response = wcapi.get(fetch_type)
    data = response.json()

    # Save to CSV
    filename = f"{fetch_type}.csv"
    if isinstance(data, list) and len(data) > 0:
        keys = data[0].keys()  # CSV headers
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)
    
    return f"Data saved to {filename}"
