# القوائم بشكل أعمق | Advanced Lists

# =_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=

"""
4-1
القوائم ثنائية الأبعاد | 2D Lists
"""
'''
value = [1, True, 'Python']
print(value[0])
'''
'___________________________________________'
'''
# نقدر نخلي العنصر الأول قائمة بدل رقم
value = [[1,2,3], True, 'Python']
print(value[0])

'''
'___________________________________________'
'''
# كيف أوصل للعنصر اللي بداخل العنصر الأول؟
value = [[1,2,3], True, 'Python']
print(value[0][2])
'''
'___________________________________________'

# توضيح للقوائم ثنائية الأبعاد
'''
value = [[1,2,3], [4,5,6], [7,8,9]]
print(value[0][2])
print(value[1][0])
print(value[2][2])
'''

# قكرة القوائم 2D
'''
value = [[1,2,3],
         [4,5,6],
         [7,8,9]
         ]
print(value[2][2])

'''
# =====================================================

"""
4-2 
الدالة filter
"""

#ages = [30,9,15,22,17,44,26,5]

# كيف أحصل على قائمة للي أعمارهم أقل من 18؟
'''
adults = []
def filtered_ages(ages):
    for age in ages:
        if age >= 18:
            adults.append(age)

    return adults

print(filtered_ages(ages))

'''

'___________________________________________'

# أقدر أختصر السابق في الدالة filter
'''
def filtered_ages(age):
    return age >= 18

print(filter(filtered_ages,ages))
print(list(filter(filtered_ages,ages)))
'''
# =====================================================

"""
4-3 
الدالة map
"""

#numbers = [5,10,20,25,50]

# كيف أخلي جميع عناصر القائمة السابقة مرفوعة للأس 2؟
'''
sq_numbers=[]
def square(numbers):
    for num in numbers:
        sq_numbers.append(num**2)

    return sq_numbers
print(square(numbers))
'''
'___________________________________________'

# في طريقة أسهل بالدالة map
'''
def square(num):
    return num ** 2

print(list(map(square,numbers)))

'''
# =====================================================

"""
4-4 
الدالة sort
"""

# line_one = [9,5,1,8]
# line_two = ['Khadijah', 'Asmaa','Zainab']
'''
line_one.sort()
line_two.sort()

print(line_one)
print(line_two)
'''
'___________________________________________'

# كيف نخلي الترتيب تنازلي؟
'''
line_one.sort(reverse=True)
line_two.sort(reverse=True)

print(line_one)
print(line_two)

'''
# =====================================================

"""
4-5 
الدالة reverse
"""
'''
names = ['Aljawharah', 'Ghadah','Eman', 'Hind']
print(names)
'''
'___________________________________________'

# كيف أقلب المصفوفة السابقة؟
'''
names = ['Aljawharah', 'Ghadah','Eman', 'Hind']
names.reverse()
print(names)
'''
# =====================================================

"""
4-6 
مفهوم List Comprehension
"""

# lst = [1,2,3,4]

# كيف أنشئ قائمة أخرى من القائمة السابقة لكن ضرب 2
'''
multiplied_list = []

for num in lst:
    multiplied_list.append(num*2)

print(multiplied_list)
'''
'___________________________________________'

# كيف اختصر السطور السابقة في سطر واحد
'''
multiplied_list = [num*2 for num in lst]
print(multiplied_list)
'''
'___________________________________________'

# ضرب الأعداد اللي أكبر من 3
'''
multiplied_list = []

for num in lst:
    if (num>3):
        multiplied_list.append(num*2)

print(multiplied_list)
'''
'___________________________________________'

# نقدر نختصرها في سطر واحد
'''
multiplied_list = [num*2 for num in lst if num > 3]
print(multiplied_list)
'''
'___________________________________________'

# أكبر من 3 وتقبل القسمة على خمسة

# lst = [1,2,3,4,5]
'''
multiplied_list = []

for num in lst:
    if (num>3) and num%5 == 0:
        multiplied_list.append(num*2)

print(multiplied_list)
'''
'___________________________________________'

# نختصرها في سطر واحد
'''
multiplied_list = [num*2 for num in lst if num > 3 and num%5 == 0]
print(multiplied_list)
'''
# =====================================================

countries = [
        ['KSA', 'Saudi Arabia'],
        ['KWT', 'Kuwait'],
        ['BHR', 'Bahrain'],
        ['UAE', 'The United Arab Emirates    '],
        ['OMN', 'Oman']
]

print(countries[2][0])