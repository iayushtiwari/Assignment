
import time 
def sync_task(name, delay):
    print(f"Task {name} started at {time.strftime('%X')}")
    time.sleep(delay)  # Simulates non-blocking delay
    print(f"Task {name} finished at {time.strftime('%X')}")

def main():
    # Schedule multiple tasks to run concurrently
    start_time = time.time()
    sync_task("A", 5),  # Task A with 5 seconds delay
    sync_task("B", 3),  # Task B with 3 seconds delay
    sync_task("C", 1),  # Task C with 1 second delay
    end_time = time.time()
    print(f"All tasks completed in {end_time - start_time:.2f} seconds")
main()

