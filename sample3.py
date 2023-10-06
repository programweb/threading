import threading

# Create a list to store error information
error_info = []
# Create a lock to protect access to the error_info list
error_lock = threading.Lock()

def thread_function(thread_id):
    try:
        for i in range(50):
            print(f"{thread_id} - Count {i}")
            if thread_id == "Thread 1" and i == 10:
                raise Exception(f"An error occurred in {thread_id} at iteration: {i}")
    except Exception as e:
        with error_lock:
            # Append error information to the shared list while holding the lock
            error_info.append((thread_id, str(e)))

# Create two Thread objects with same target function
thread1 = threading.Thread(target=thread_function, args=("Thread 1",))
thread2 = threading.Thread(target=thread_function, args=("Thread 2",))

# Start both threads
thread1.start()
thread2.start()

while thread1.is_alive():
    # Display real-time updates from thread1
    print("Main thread processing real-time updates...")
    # You can perform other tasks here too

# Wait for both threads to finish; ensures that the main program waits for the threads to complete their execution before continuing
thread1.join()
thread2.join()

# Print error information outside of the target function
with error_lock:
    for thread_id, error_message in error_info:
        print(f"{thread_id} encountered an error: {error_message}")
