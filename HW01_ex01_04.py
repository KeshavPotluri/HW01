# HW01_ex01_04
# Start the Python interpreter and use it as a calculator. 
# Python's syntax for math operations is almost the same as 
# standard mathematical notation. For example, the symbols 
# +, - and / denote addition, subtraction and division, as you would expect. 
# The symbol for multiplication is *.

# If you run a 10 kilometer race in 43 minutes 30 seconds, what is your 
# average time per mile? What is your average speed in miles per hour? 
# (Hint: there are 1.61 kilometers in a mile).
# Average Speed in MPH:

#Take the distance into a variable
distance = 10.00 
#Convert time to seconds
time = 43*60 + 30 
# Divide the distance by time to get speed in Km/second
# and multiply it by 3600 to get speed in Km/hour
speedInKm = distance/time*3600 
# Divide speed in Km by 1.61 to get speed in Miles/hour
speedInMiles = speedInKm/1.61
# Print the result
print 'Average Speed in MPH: ' + str(speedInMiles)

# Get the time per mile
timePerMileInSeconds = 1/speedInMiles
# Print the result
print 'Time per Mile: ' + str(timePerMileInSeconds)
