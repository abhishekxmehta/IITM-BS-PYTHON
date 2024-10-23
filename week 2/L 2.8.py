#if condition
#let us consider the movie "Avengers". This is a 13+ movie

print ('Please enter your date of birth')
birth_year=int(input())

current_year=2024

age=current_year-birth_year
if (age<13):
    print ('You are not allowed to watch this movie')
else:
    print ('You are allowed to watch this movie')