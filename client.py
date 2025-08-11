import asyncio
import uuid
import json
from temporalio.client import Client
from workflows import WooCommerceWorkflow
import os
from dotenv import load_dotenv

load_dotenv()



async def main():
    client = await Client.connect("localhost:7233")

    workflow_id = f"woocommerce-workflow-{uuid.uuid4()}"

    result = await client.execute_workflow(
        WooCommerceWorkflow.run,
        args=[{
            "url": os.getenv("WC_URL"),
            "consumer_key": os.getenv("WC_CONSUMER_KEY"),
            "consumer_secret": os.getenv("WC_CONSUMER_SECRET")
        }, "products"],
        id=workflow_id,
        task_queue="woocommerce-task-queue"
    )

    print(f"\n✅ Workflow {workflow_id} completed")
    print("Fetched data:\n")
    # Pretty JSON output
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    asyncio.run(main())
