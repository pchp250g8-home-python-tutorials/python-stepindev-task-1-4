# --coding:utf-8--
h1 = int(input("How many hours is now? (0-23)"))
m1 = int(input("How many minutes is now? (0-59)"))
m2 = h1 * 60 + m1  # Current time translated into minutes
m3 = 24 * 60  # Midnight time translated into minutes 
dm = m3 - m2  # Remaining time until midnight in minutes
h2 = dm // 60  # Remaining time until midnight in full hours
# Remaining quantity of minutes until end of the hour is calculated before
m2 = dm % 60
# --Output of information to display--
print(f"Current time: {h1} : {m1}")
print(f"{h2} : {m2} is remaining until midnight.")
