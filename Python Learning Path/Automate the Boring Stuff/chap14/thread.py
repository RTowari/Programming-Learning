import threading, time
print("Start of the program")

def takeANap():
    time.sleep(5)
    print("Wake up!")

threadObj = threading.Thread(target=takeANap)
threadObj.start()

print("End of the program")