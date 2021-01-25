import time
import sys

fromIndex = 0
toIndex = 0

if len(sys.argv) == 3:
    fromIndex = int(sys.argv[1])
    toIndex = int(sys.argv[2])
else:
    print("please input index range.")
    sys.exit()

for i in range(fromIndex,toIndex):
    print(f">>>>>{i}")
    time.sleep(2)