import io
import sys
import time

print('Original buffer size:', io.DEFAULT_BUFFER_SIZE)
for large_buffer in False, True:
    if large_buffer:
        print('Increasing buffer size...')
        sys.stdout = io.TextIOWrapper(io.BufferedWriter(sys.stdout.buffer, 100000))
    for i in range(2):
        time.sleep(2)
        print(str(i * 2) * 10000)
        time.sleep(2)
        print(str(i * 2 + 1) *10000)
        print(f'Flush #{i + 1}')
        sys.stdout.flush()