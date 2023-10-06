# threading
Multi-threading examples

Similar samples in that all start 2 threads both of which call a "target function" named:
thread_function.

Make the file executable.
Execute multiple times like: python3 sample3.py
You will note in the output Thread 1 and Thread 2 are running independently—not necessarily
in sequence.

An error is raised for thread 1 to show handling.
Thread 1 stops at that point.

**SAMPLE 1**
&nbsp;
The error is printed from the target function itself.

**SAMPLE 2**
&nbsp;
A list called "error_info" holds tuples of error information.
This allows for the printing (and further handling if needed) of the error message
outside of the target function.

Note: "error_info" is a global variable. It's defined outside of any function or class, 
making it accessible from any part of the code. This allows you to store 
and access error information from different threads.

Keep in mind that when you use global variables in a multi-threaded program, you should be 
cautious about potential race conditions and thread safety. In this specific example, the 
code is relatively simple and doesn't involve complex data sharing or modification of 
error_info from multiple threads simultaneously, so it should work fine. However, in more 
complex scenarios, you might need to use additional synchronization mechanisms like locks 
to ensure thread safety when accessing shared data. This is demonstrated in the next 
sample.

**SAMPLE 3**
&nbsp;
Here we create a lock to protect access to the error_info list

Create a lock to protect access to the error_info list
It is an instance of the threading.Lock class. 
A lock, short for "mutex" (short for "mutual exclusion"), 
is a synchronization mechanism used in multi-threaded programs 
to control access to shared resources or critical sections of 
code. It allows only one thread to access a particular 
resource or section of code at a time, ensuring that multiple 
threads do not interfere with each other when reading or 
modifying shared data.  While a thread holds the lock, no other 
thread can acquire it. This ensures that only one thread at a 
time can access or modify the error_info list, preventing data 
corruption.
