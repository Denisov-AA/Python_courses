from Hours_Minutes import Hours

# Seconds input
degrees = input('Enter the clockwise angle: ')
degrees = int(degrees)

# Converting
Answer = Hours(None, degrees)
Answer.degrees_convert()
