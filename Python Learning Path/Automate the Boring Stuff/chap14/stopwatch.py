#! python3
# stopwatch.py - A simple stopwatch program

import time

# Display the program's instructions
print("Press ENTER to begin. Afterwards, press ENTER to 'click' the stopwatch. Press Ctrl-C to quit")
input() # Press enter to begin
print("Started")
startTime = time.time()  # Time star to count here
lastTime = startTime # Last time time was measured
lapNum = 1

# TODO: Start stracking the lap times
try:
    while True:
        print("Code note: before input here")
        input()
        print("Code note: after input here")
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print("Lap #%s: %s (%s)" % (lapNum, totalTime, lapTime), end = "")
        lapNum += 1
        lastTime = time.time() # reset the last lap time

except KeyboardInterrupt:
    # Handle the Ctrl-C excepcion to keep its error message from displaying
    print("\nDone.")