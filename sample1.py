import threading

def thread_function(thread_id):
    try:
        for i in range(50):
            print(f"Thread {thread_id} - Count {i}")
            if thread_id == "Thread 1" and i == 5:
                raise Exception("An error occurred in Thread 1")
    except Exception as e:
        print(f"Thread {thread_id} encountered an error: {str(e)}")

# Create two Thread objects with different target functions
thread1 = threading.Thread(target=thread_function, args=("Thread 1",))
thread2 = threading.Thread(target=thread_function, args=("Thread 2",))

# Start both threads
thread1.start()
thread2.start()

# Wait for both threads to finish; ensures that the main program waits for the threads to complete their execution before continuing
thread1.join()
thread2.join()
