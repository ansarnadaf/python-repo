import asyncio
import time

# An asynchronous function (coroutine)
async def fetch_data(task_id, delay):
    print(f"-> Task {task_id}: Starting (will take {delay}s)...")
    
    # Non-blocking sleep: allows other tasks to run while waiting
    await asyncio.sleep(delay) 
    
    print(f"<- Task {task_id}: Finished!")
    return f"Result from {task_id}"

async def main():
    start_time = time.perf_counter()

    # Create a list of tasks to run concurrently
    tasks = [
        fetch_data("A", 2),
        fetch_data("B", 1),
        fetch_data("C", 1.5)
    ]

    print("--- Starting Concurrent Tasks ---")
    
    # Run all tasks at once and wait for the results
    results = await asyncio.gather(*tasks)

    end_time = time.perf_counter()
    
    print("--- All tasks complete! ---")
    print(f"Results: {results}")
    print(f"Total time elapsed: {end_time - start_time:.2f} seconds")

# Run the entry point of the script
if __name__ == "__main__":
    asyncio.run(main())