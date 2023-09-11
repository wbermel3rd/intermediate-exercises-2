import time, random
import Fib

time1 = time.time()
toFib = random.randint(15, 35)
fibbed = Fib.fib(toFib)
time2 = time.time()
elapsed_time = time2 - time1
print("fib(" + str(toFib) + ")=" + str(fibbed))
print("fib(" + str(toFib) + ") took " + str(elapsed_time) + "seconds")


