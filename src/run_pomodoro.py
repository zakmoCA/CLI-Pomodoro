import time
import os
import chime


class Timer:
    def run_pomodoro(self, cycle_length, work_time, short_break, long_break):
        for i in range(cycle_length):
            print("Work timer started for", work_time, "minutes")
            chime.theme('material')
            chime.success()
            self.countdown(work_time * 60)

            if i < cycle_length - 1:  # last work period requires long break timer
                print("\nShort break timer started for", short_break, "minutes")
                chime.theme('zelda')
                chime.success()
                self.countdown(short_break * 60)

        print("\nLong break timer started for", long_break, "minutes")
        chime.theme('sonic')
        chime.success()
        self.countdown(long_break * 60)

    def countdown(self, t):
        while t:
            mins, secs = divmod(t, 60)
            # Formats mins and secs as 2-digit numbers
            timer = '{:02d}:{:02d}'.format(mins, secs)
            # Prints timer to console, replacing prev line with end="\r" every second for live self.countdown
            print(timer, end="\r")
            time.sleep(1)  # Pause for 1 second for each iteration
            t -= 1  # Decrement remaining time by 1 second
