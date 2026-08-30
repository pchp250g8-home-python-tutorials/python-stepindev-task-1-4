# --coding:utf-8--
n = int(input("Enter the number of seconds since midnight: "))
h = n // 3600 # Number of full hours
m = (n // 60) % 60 # Number of full minutes remaining
s = n % 60 # Number of seconds remaining
# --Display information on the screen--
print(f"Number of full hours since midnight:{h}")
print(f"Number of full minutes since midnight:{m}")
print(f"Number of seconds remaining since midnight:{s}")