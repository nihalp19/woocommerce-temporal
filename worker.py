import asyncio
from temporalio.worker import Worker
from temporalio.client import Client
from workflows import WooCommerceWorkflow
from activities import fetch_products

async def main():
    client = await Client.connect("localhost:7233")

    worker = Worker(
        client,
        task_queue="woocommerce-task-queue",
        workflows=[WooCommerceWorkflow],
        activities=[fetch_products],
    )

    print("Worker started... waiting for workflows")
    await worker.run()

if __name__ == "__main__":
    asyncio.run(main())
