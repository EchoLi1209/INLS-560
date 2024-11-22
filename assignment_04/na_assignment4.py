#constants for Skate Coach
MIN_YEARS_SKATING = 10
MIN_YEARS_COACHING = 2

years_skating = int(input('Enter your years of skating experience:'))
years_coaching = int(input('Enter how many years you have been a skating coach:'))

if years_skating >= MIN_YEARS_SKATING and years_coaching >= MIN_YEARS_COACHING:
    print('Congratulations! You are eligible for the Skating Coach Position.')
else:
# Multiple-line with f-string
    print(f'''
Sorry, you do not meet the requirements for the Skating Coach Position,
    
You need at least:
- {MIN_YEARS_SKATING} years of skating experience
- {MIN_YEARS_COACHING} years as a skating coach
''')