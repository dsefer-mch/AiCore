'''
Given 2 parameters, height and weight, calculate the parameter BMI (Google the formula) (For simplicity, work in metres and kg).

Using the parameter BMI, write a series of if statements that print the following outcomes:

- below 18.5 –-> 'Your BMI is x. You're in the underweight range.'

- between 18.5 and 24.9 –-> 'Your BMI is x. You're in the healthy weight range.'

- between 25 and 29.9 –-> 'Your BMI is x. You're in the overweight range.'

- between 30 and 39.9 –-> 'Your BMI is x. You're in the obese range.'

Test your code with the following cases by substituting them in for weight and height values in your code:<br>

Height 1.83m, Weight 85kg

Height 1.55m, Weight 61kg

Height 2.09m, Weight 135kg

Height 1.71m, Weight 70kg

Height 1.71m, Weight 95kg

Height 1.71m, Weight 55kg

(Once again, this is a tedious process that will show the obvious value of for loops and functions when we cover them)
'''

Height = float(input('Please provide Your height in meters '))
Weight = float(input('Please provide Your weight in kilos '))


bmi = Weight / (Height**2)

if bmi < 18.5:
    print(f"Your BMI is {bmi}. You're in the underweight range.")
elif 18.5 <= bmi < 24.9:
    print(f"Your BMI is {bmi}. You're in the healthy weight range.")
elif 25 <= bmi < 29.9:
    print(f"Your BMI is {bmi}. You're in the overweight range.")
elif 30 <= bmi < 39.9:
    print(f"Your BMI is {bmi}. You're in the obese range.")
else:
    print(f"Your BMI is {bmi}. You're OUT of range.")
