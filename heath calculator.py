''' BMI calculator'''

Height = eval(input('Enter the your Height'))
Weight = eval(input('Enter the your weight'))

BMI = Weight/(Height*Height)

if BMI<18.5:
    print('You are UNDERWEIGHT')
elif BMI>30:
    print('You are Obese')

else:
    for BMI in range(25,31):
        print('over weight')
