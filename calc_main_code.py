# for last time calc used
from datetime import datetime

# the main project : a Calculator with Addition, Subtraction, Multiplication, Division, Percent, Expression and last used func
class Calculator:
    created_time = datetime.now()
    last_ans = ''
    def __init__(self, *num):
        self.nums = list(num)

    def Addition(self):
        if len(self.nums) >= 2 :
            ans = sum(self.nums)
            print(f'this is your answer : {ans}')
            Calculator.last_ans = ans
        else :
            print('Minimum 2 numbers')

    def Subtraction(self):
        if len(self.nums) >= 2 :
            ans = self.nums[0]
            for i in range(1,len(self.nums)):
                ans = ans - self.nums[i]
            print(f'this is your answer : {ans}')
            Calculator.last_ans = ans
        else :
            print('Minimum 2 numbers')
    
    def Multiplication(self):
        if len(self.nums) >= 2 :
            ans = self.nums[0]
            for i in range(1,len(self.nums)):
                ans = ans * self.nums[i]
            print(f'this is your answer : {ans}')
            Calculator.last_ans = ans
        else :
            print('Minimum 2 numbers')

    def Division(self):
        if len(self.nums) >= 2 :
            ans = self.nums[0]
            for i in range(1,len(self.nums)):
                ans = ans / self.nums[i]
            print(f'this is your answer : {ans}')
            Calculator.last_ans = ans
        else :
            print('Minimum 2 numbers')

    def Percent(self):
        if len(self.nums) == 2 :
            ans = (self.nums[0] * self.nums[1]) / 100
            print(f'this is your answer : {ans}')
            Calculator.last_ans = ans
        else :
            print('Only 2 numbers needed')

    def Expression(self):
        if len(self.nums) > 0 and self.nums[0] != '':
            ans = eval(self.nums[0])
            print(f'this is your answer : {ans}')
            Calculator.last_ans = ans
        else:
            print('Please enter a valid expression!')


    def last_ans_func(self):
        print(f'this is your last answer : {self.last_ans}')
        print(f'and time this result was created {self.created_time}')
    


# menu
nums = []
print('1 = Addition')
print('2 = Subtraction')
print('3 = Multiplication')
print('4 = Division')
print('5 = Percent')
print('6 = Expression')
menu1 = input('enter what do you want : ')

# add args
if menu1 == '6':
    menu2 = input('enter your expression : ')
    q1 = Calculator(menu2)
elif menu1 != '6':
    while True :
        print('type how many number you want to get in calc (press x for end)')
        menu3 = input('enter your number : ')
        if menu3 == 'x':
            break
        else :
            menu2 = int(menu3)
            nums.append(menu2)

    q1 = Calculator(*nums)

# run methods
match menu1:
    case '1':
        q1.Addition()
    case '2':
        q1.Subtraction()
    case '3':
        q1.Multiplication()
    case '4':
        q1.Division()
    case '5':
        q1.Percent()
    case '6':
        q1.Expression()

#last used calc
q1.last_ans_func()
