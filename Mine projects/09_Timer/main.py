import time

user = int(input("Enter the time in seconds:"))

for x in range(user ,0 ,-1):
    seconds = int(x % 60)
    mints = int( x / 60 ) % 60
    hours = int(x / 3600)
    print(f"{hours:02} : {mints:02} : {seconds:02} ")
    time.sleep(0.80)

print("Time up!")