#!/usr/bin/env python3
"""
Example of using the user verification functionality in the Arcade SDK.

This example demonstrates how to confirm a user in an OAuth flow.
"""

from arcadepy import Arcade

# Initialize the Arcade client
# (uses the ARCADE_API_KEY environment variable by default)
client = Arcade()


def confirm_user() -> None:
    """Example of confirming a user in an OAuth flow."""
    try:
        # Get the flow ID from the query string
        flow_id = "flow_id"  # In a real app, this would come from query params

        # Get the user ID from a session cookie or other secure storage
        user_id = "user_id"  # In a real app, this would come from your session

        # Confirm the user
        response = client.user_verification.confirm(flow_id, user_id)

        print("User confirmed successfully!")
        print(f"Auth ID: {response.auth_id}")

        if response.next_uri:
            print(f"Redirecting to: {response.next_uri}")
            # In a real application, you would redirect the user:
            # return redirect(response.next_uri)

    except Exception as e:
        print(f"Failed to confirm user: {e}")


async def confirm_user_async() -> None:
    """Example of confirming a user asynchronously."""
    from arcadepy import AsyncArcade

    async_client = AsyncArcade()

    try:
        response = await async_client.user_verification.confirm(flow_id="flow_id", user_id="user_id")

        print("User confirmed successfully (async)!")
        print(f"Auth ID: {response.auth_id}")
        print(f"Next URI: {response.next_uri}")

    except Exception as e:
        print(f"Failed to confirm user: {e}")


if __name__ == "__main__":
    # Run the synchronous example
    confirm_user()

    # Run the async example
    print("\n--- Async Example ---")
    import asyncio

    asyncio.run(confirm_user_async())
