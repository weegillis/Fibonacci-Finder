# Fibonacci-Finder
A too simple Python algorithm that appears to run extremely fast taking less than 10 seconds to find the 1000001 Fibonacci
This code was written around eight years ago when it must have been a subject of interest. It got tucked away and only resurfaced on going through some old examples. Being a demo means it has no documentation or even annotation so one must glean what we can from the code itself.

A few timed test runs were done using the following script:
```
import time as t
x = 1000001
start = t.perf_counter()
fib_n = fibonacci_finder(x)
end = t.perf_counter()
print (fib_n)
print (end - start)
```
The resulting output was 2613 lines times 80 digits taking 9.65 seconds on a 2015 i5 machine with just 8 GB of RAM. Can't imagine this running slower on a modern computer, or even a phone.

Would be interested to learn the Big-O as well as other's reported run times. At what point does it fail?
