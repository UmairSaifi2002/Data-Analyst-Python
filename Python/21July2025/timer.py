import time

def countdown_timer():
    try:
        seconds = int(input("Enter the number of seconds: "))
        while seconds:
            mins, secs = divmod(seconds, 60)
            timer = f'{mins:02d}:{secs:02d}'
            print(timer, end='\r')
            time.sleep(1)
            seconds -= 1
        print("⏰ Time's up!")
    except ValueError:
        print("Please enter a valid number.")

# Run the function
countdown_timer()
