import machine
import time

# print("Wake up")
# machine.deepsleep(5000) #deepsleep 1 second
# print("this will never get printed!")

print("this will be printed before: " + str(time.ticks_ms()))

machine.sleep(1000 * 10, True)

print("this will be printed after 10 seconds: "+ str(time.ticks_ms()))
