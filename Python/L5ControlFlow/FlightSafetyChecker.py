'''
Given 2 parameters, altitude(ft) and airspeed(knots), write a program that categorises entries into 'safe flying' and 'unsafe flying' based on the following criteria:

- An altitude of below 100ft or above 50000ft is considered unsafe flying.

- An airspeed of 60 knots and below or 500 knots and above is considered unsafe flying.

- Altitudes and airspeeds outside these ranges are considered safe flying.

CLUE: You will have to figure out the syntax for using __and__/__or__ keywords in if statements, __this may be tough but stick at it__.

Try to write this as cleanly as possible and test your code with the following by substituting in again:

- altitude 25000ft, airspeed 300kn

- altitude 50001ft, airspeed 250kn

- altitude 90ft, airspeed 125kn

- altitude 500ft, airspeed 45kn

- altitude 1000ft, airspeed 600kn

- altitude 65000ft, airspeed 700kn
'''

altitude = int(input('Please enter altitude in ft '))
airspeed = int(input('Please enter airspeed in knots '))

if (altitude < 100 or altitude > 50000) or (airspeed <= 60 or airspeed >= 500):
    print('Considered unsafe flying')
else:
    print('Considered safe flying')