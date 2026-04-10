def test(lst):
    result = {}
    for item in lst:
        result[item[0]] = item[1:]
    return result

students = [[1,'jean castro', 'v'], [2,'maria garcia', 'v'], 

[3,'john smith', 'v'], [4,'susan lee', 'v'], [5,'michael brown', 'v']]

print("/noriginal list of lists:")
print(students)
print("/nconverted to dictionary:")
print(test(students))