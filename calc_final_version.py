# the main project : a Calculator with Addition, Subtraction, Multiplication, Division, Percent and last used func
class Calculator:
    last_ans = ''
    History = []

    def __init__(self):
        pass

    def Show_History(self):
        if not Calculator.History:
            print("Show_History : History is empty!")
            return

        print("Show_History : History:")
        for index, item in enumerate(Calculator.History, start=1):
            print(f"{index}. {item}")

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
            try:
                ans = eval(expression)
                print(f'Expression : this is your answer : {ans}')
                Calculator.last_ans = f'{expression} = {ans}'
                Calculator.History.append(Calculator.last_ans)
            except:
                print('Expression : Error: Invalid expression!')

    def Percent(self):
        while True:
            mode = input('Percent : 1 for percent / 2 for increase : ')
            if mode in ['1', '2']:
                break
            print('Percent : Invalid mode!')

        num1 = input('Percent : enter your number : ')
        num2 = input('Percent : enter your percent : ')

        try:
            num1 = float(num1)
            num2 = float(num2)
        except:
            print('Percent : Error: only num values are allowed!')
            return

        if mode == '1':
            ans = (num1 * num2) / 100
            print(f'Percent : this is your answer : {ans}')
            Calculator.last_ans = f'{num2}% of {num1} = {ans}'
            Calculator.History.append(Calculator.last_ans)

        elif mode == '2':
            ans = num1 + ((num1 * num2) / 100)
            print(f'Percent : this is your answer : {ans}')
            Calculator.last_ans = f'{num1} increased by {num2}% = {ans}'
            Calculator.History.append(Calculator.last_ans)

    def last_ans_func(self):
        if not Calculator.last_ans:
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

# last used calc
q1.last_ans_func()

# History method
q1.Show_History()

# task1 = history system 
# task2 = input error when type invalid caracter