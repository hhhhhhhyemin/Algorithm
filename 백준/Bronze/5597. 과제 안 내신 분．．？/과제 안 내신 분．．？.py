student = list(range(1, 31))
for i in range(28) :
    student.remove(int(input()))
    
print(min(student))
print(max(student))