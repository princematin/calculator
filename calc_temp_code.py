from datetime import datetime

class Calculator:
    created_time = datetime.now()
    last_ans = ''
    def __init__(self, *num):
        self.nums = list(num)

    def Addition(self):
        if len(self.nums) <= 2 :
            ans = sum(self.nums)
            print(f'this is your answer : {ans}')
            Calculator.last_ans = ans
        else :
            print('Minimum 2 numbers')

    def Subtraction(self):
        if len(self.nums) <= 2 :
            ans = self.nums[0]
            for i in range(1,len(self.nums)):
                ans = ans - self.nums[i]
            print(f'this is your answer : {ans}')
            Calculator.last_ans = ans
        else :
            print('Minimum 2 numbers')
    
    def Multiplication(self):
        if len(self.nums) <= 2 :
            ans = self.nums[0]
            for i in range(1,len(self.nums)):
                ans = ans * self.nums[i]
            print(f'this is your answer : {ans}')
            Calculator.last_ans = ans
        else :
            print('Minimum 2 numbers')

    def Division(self):
        if len(self.nums) <= 2 :
            ans = self.nums[0]
            for i in range(1,len(self.nums)):
                ans = ans / self.nums[i]
            print(f'this is your answer : {ans}')
            Calculator.last_ans = ans
        else :
            print('Minimum 2 numbers')
    
    def last_ans_func(self):
        print(f'this is your last answer : {self.last_ans}')
        print(f'and time this result was created {self.created_time}')
    



nums = []
print('1 = Addition')
print('2 = Subtraction')
print('3 = Multiplication')
print('4 = Division')
menu1 = input('enter what do you want : ')
while True :
    print('type how many number you want to get in calc (press x for end)')
    menu2 = input('enter your number : ')
    if menu2 == 'x':
        break
    else :
        menu2 = int(menu2)
        nums.append(menu2)
for i in nums :
    q1 = Calculator(i)
match menu1:
    case '1':
        q1.Addition()
    case '2':
        q1.Subtraction()
    case '3':
        q1.Multiplication()
    case '4':
        q1.Division()