import msvcrt as ms
import time

ESCAPE = chr(27)

workPending = True
cycle = 0

while workPending:
    print("Getting imaginary data %s..." % cycle)
    time.sleep(1.5)
    print("\tSaving imaginary data %s..." % cycle)
    time.sleep(1.5)

    if ms.kbhit():
        key = ms.getwch()
        if key == ESCAPE:
            print("Pre-termination on cycle %s..." % cycle)
            break
        else:
            print("Random keypress %r found on cycle %s..." % (key, cycle))

    cycle += 1
    time.sleep(1.5)
print("Termination")