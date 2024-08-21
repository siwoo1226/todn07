import random
result='my_number:'
for i in range(6): #0~5까지 6번 반복실행
    num=random.randint(1,46)
    result=result+f" {num}"
print(result)
