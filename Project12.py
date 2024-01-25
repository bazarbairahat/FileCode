import random
import time

colors = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m']

while True:
    message = ''.join(random.choice(colors) + char for char in "Разноцветный текст, который разноцветно мигает!")
    print(message)
    time.sleep(0.2)
