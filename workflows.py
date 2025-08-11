from temporalio import workflow
from temporalio import workflow
from datetime import timedelta

@workflow.defn
class WooCommerceWorkflow:
    @workflow.run
    async def run(self, creds: dict, fetch_type: str):
        return await workflow.execute_activity(
            "fetch_products",                # Activity name
            args=[creds, fetch_type],         # ✅ Correct way to pass arguments
            start_to_close_timeout=timedelta(seconds=30)
        )

