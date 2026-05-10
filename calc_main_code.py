import time

class Calculator:
    last_ans = ''
    def __init__(self, *num):
        self.nums = list(num)

    def Addition(self):
        ans = sum(self.nums)
        print(f'this is your answer : {ans}')
        Calculator.last_ans = ans

    def Subtraction(self):
        ans = self.nums[0]
        for i in range(1,len(self.nums)):
            ans = ans - self.nums[i]
        print(f'this is your answer : {ans}')
        Calculator.last_ans = ans
    
    def Multiplication(self):
        ans = self.nums[0]
        for i in range(1,len(self.nums)):
            ans = ans * self.nums[i]
        print(f'this is your answer : {ans}')
        Calculator.last_ans = ans

    def Division(self):
        ans = self.nums[0]
        for i in range(1,len(self.nums)):
            ans = ans / self.nums[i]
        print(f'this is your answer : {ans}')
        Calculator.last_ans = ans
    
    def last_ans_func(self):
        print(f'this is your last answer : {self.last_ans}')
    