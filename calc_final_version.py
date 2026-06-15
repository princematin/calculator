

# the main project : a Calculator with Addition, Subtraction, Multiplication, Division, Percent and last used func
class Calculator:
    last_ans = ''

    def __init__(self):
        pass

    def Expression(self):
        TorF_val = False
        expression = input('Expression : enter your expression : ')
        for i in expression:
            if ('a' <= i <= 'z') or ('A' <= i <= 'Z'):
                print('Expression : Error: only num values are allowed!')
                break
            else :
                TorF_val = True
        if TorF_val == True:
            ans = eval(expression)
            print(f'Expression : this is your answer : {ans}')
            Calculator.last_ans = f'{expression} = {ans}'


    def Percent(self):
        TorF_val1 = False
        TorF_val2 = False
        while True:
            mode = input('Percent : 1 for percent / 2 for increase : ')
            if mode in ['1', '2']:
                break
            print('Percent : Invalid mode!')

        num1 = input('Percent : enter your number : ')
        num2 = input('Percent : enter your percent : ')
        for i in num1:
            if ('a' <= i <= 'z') or ('A' <= i <= 'Z'):
                print('Percent : Error: only num values are allowed!')
            else:
                TorF_val1 = True
        for i in num2:
            if ('a' <= i <= 'z') or ('A' <= i <= 'Z'):
                print('Percent : Error: only num values are allowed!')
            else:
                TorF_val2 = True
        if TorF_val1 and TorF_val2 == True:
            num1 = float(num1)
            num2 = float(num2)

            if mode == '1':
                ans = (num1 * num2) / 100
                print(f'Percent : this is your answer : {ans}')
                Calculator.last_ans = f'{num2}% of {num1} = {ans}'

            elif mode == '2':
                ans = num1 + ((num1 * num2) / 100)
                print(f'Percent : this is your answer : {ans}')
                Calculator.last_ans = f'{num1} increased by {num2}% = {ans}'
        else:
            print('Percent : Error: only num values are allowed!')


    def last_ans_func(self):
        if Calculator.last_ans is None or Calculator.last_ans == "":
            print('last_ans_func : you Calculator nothing!')
        else :
            print(f'last_ans_func : this is your last calculating : {Calculator.last_ans}')
        
    


# menu
nums = []
print('1 = Expression')
print('2 = Percent')
print('------------------------------------------------')
menu1 = input('Calculator : enter what do you want : ')

# add args and rum methods
q1 = Calculator()

if menu1 == '1':
    q1.Expression()
elif menu1 == '2':
    q1.Percent()

#last used calc
q1.last_ans_func()
