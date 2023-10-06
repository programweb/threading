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

We create a lock to protect access to the error_info list preventing
potential issues caused by concurrent access to shared data.
error_info is an instance of the threading.Lock class. 
A lock, short for "_mutex_" (short for "_mutual exclusion_"), 
is a synchronization mechanism used in multi-threaded programs 
to control access to shared resources or critical sections of 
code. It allows only one thread to access a particular 
resource or section of code at a time, ensuring that multiple 
threads do not interfere with each other when reading or 
modifying shared data.  While a thread holds the lock, no other 
thread can acquire it. This ensures that only one thread at a 
time can access or modify the error_info list, preventing data 
corruption.


POSSIBLE EXECUTION
```
$ python3 sample3.py 
Thread 1 - Count 0
Thread 1 - Count 1
Thread 1 - Count 2
Thread 1 - Count 3
Thread 1 - Count 4
Thread 1 - Count 5
Thread 1 - Count 6
Thread 1 - Count 7
Thread 2 - Count 0
Main thread processing real-time updates...
Thread 1 - Count 8
Thread 2 - Count 1
Main thread processing real-time updates...
Thread 1 - Count 9
Thread 2 - Count 2
Thread 2 - Count 3
Thread 2 - Count 4
Thread 1 - Count 10
Main thread processing real-time updates...
Thread 2 - Count 5
Thread 2 - Count 6
Thread 2 - Count 7
Thread 2 - Count 8
Thread 2 - Count 9
Thread 2 - Count 10
Thread 2 - Count 11
Thread 2 - Count 12
Thread 2 - Count 13
Thread 2 - Count 14
Thread 2 - Count 15
Thread 2 - Count 16
Thread 2 - Count 17
Thread 2 - Count 18
Thread 2 - Count 19
Thread 2 - Count 20
Thread 2 - Count 21
Thread 2 - Count 22
Thread 2 - Count 23
Thread 2 - Count 24
Thread 2 - Count 25
Thread 2 - Count 26
Thread 2 - Count 27
Thread 2 - Count 28
Thread 2 - Count 29
Thread 2 - Count 30
Thread 2 - Count 31
Thread 2 - Count 32
Thread 2 - Count 33
Thread 2 - Count 34
Thread 2 - Count 35
Thread 2 - Count 36
Thread 2 - Count 37
Thread 2 - Count 38
Thread 2 - Count 39
Thread 2 - Count 40
Thread 2 - Count 41
Thread 2 - Count 42
Thread 2 - Count 43
Thread 2 - Count 44
Thread 2 - Count 45
Thread 2 - Count 46
Thread 2 - Count 47
Thread 2 - Count 48
Thread 2 - Count 49
Thread 1 encountered an error: An error occurred in Thread 1 at iteration: 10
$
```
