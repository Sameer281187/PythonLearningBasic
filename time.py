import time

timestamp = time.strftime("%H:%M:%S")
print(timestamp)

greeting = "Good Morning"

if (12 <= int(time.strftime("%H")) < 16) & (int(time.strftime("%M")) > 0 or int(time.strftime("%S")) > 0):
    greeting = "Good Afternoon"
elif (16 <= int(time.strftime("%H")) < 20) & (int(time.strftime("%M")) > 0 or int(time.strftime("%S")) > 0):
    greeting = "Good Evening"
elif (20 <= int(time.strftime("%H")) < 24) & (int(time.strftime("%M")) > 0 or int(time.strftime("%S")) > 0):
    greeting = "Good Night"
elif (0 <= int(time.strftime("%H")) < 5) & (int(time.strftime("%M")) > 0 or int(time.strftime("%S")) > 0):
    greeting = "Good Night"

print(greeting)
