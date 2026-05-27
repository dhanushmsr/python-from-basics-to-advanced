import time
import datetime
import pywhatkit as kit
import random
import webbrowser as wb

# 💡 Motivational messages
quotes = [
    "Wake up and chase your dreams!",
    "Success starts with discipline.",
    "Every day is a fresh start!",
    "Push yourself, no one else will do it for you.",
    "You are stronger than you think!"
]

# 🌙 Bedtime messages
bed_quotes = [
    "Tonight, rest is productive too.",
    "Sleep is the best meditation.",
    "Let go of today. Tomorrow will handle itself.",
    "Your mind deserves a break. Close your eyes."
]

# ⏰ Alarm setup
print("Let's set your alarm...")
alarm_hour = int(input("Enter hour (0-23): "))
alarm_minute = int(input("Enter minute (0-59): "))

print("⏳ Alarm set... Waiting...")

# 🌙 Bedtime setup
bed_choice = input("Do you want to set your bedtime? (yes/no): ")

if bed_choice.lower() == "yes":
    print("Let's set your bedtime")
    
    bed_hour = int(input("Enter bedtime hour (0-23): "))
    bed_minute = int(input("Enter bedtime minute (0-59): "))
    
    print("🌙 Bedtime reminder is set!")
else:
    print("That's fine!")

# Flags to avoid repeating alerts
alarm_triggered = False
bed_triggered = False

while True:
    now = datetime.datetime.now()

    current_hour = now.hour
    current_minute = now.minute

    # 🔔 Morning Alarm
    if (
        current_hour == alarm_hour
        and current_minute == alarm_minute
        and not alarm_triggered
    ):
        print("\n🔔 Wake Up!")

        # Open motivational video
        wb.open("https://www.youtube.com/shorts/5WcIoWgL8-Q")

        # Random motivation
        message = random.choice(quotes)
        print("💬 Motivation:", message)

        # Send WhatsApp message
        kit.sendwhatmsg_instantly(
            "+916374547764",
            message,
            wait_time=10,
            tab_close=True
        )

        print("✨ Get refreshed!")

        time.sleep(5)

        video_choice = input(
            "Can I play a motivational video? (yes/no): "
        )

        if video_choice.lower() == "yes":
            kit.playonyt("morning motivation")
        else:
            print("Fine! Have a nice day 😊")

        alarm_triggered = True

    # 🌙 Bedtime Reminder
    if bed_choice.lower() == "yes":

        if (
            current_hour == bed_hour
            and current_minute == bed_minute
            and not bed_triggered
        ):
            print("\n🌙 Bed Time! Put your phone down and sleep")

            mes = random.choice(bed_quotes)

            # Send bedtime WhatsApp message
            kit.sendwhatmsg_instantly(
                "+916374547764",
                mes,
                wait_time=10,
                tab_close=True
            )

            # Play relaxing music
            kit.playonyt("night melody")

            bed_triggered = True

    # Prevent CPU overuse
    time.sleep(30)