# Functions | الدوال

# =_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=

'''
10-1
مفهوم الدوال Function
'''

# عمل برنامج بسيط لتحية المستخدم حسب الوقت

'''name = input("Please enter your name:")
time = input("Please enter the time of the day:")

print("Good " + time + "," + name + "!")'''

" ___________________________________________________ "

# نجرب التالي لتعريف الدالة

'''def greet():
    name = input("Please enter your name:")
    time = input("Please enter the time of the day:")

    print("Good " + time + "," + name + "!") 
    '''
    # ماراح تعطينا مخرجات

" ___________________________________________________ "

# ما راح يتم تنفيذ أوامر الدالة إلا عند استدعائها

'''
def greet():
    name = input("Please enter your name:")
    time = input("Please enter the time of the day:")

    print("Good " + time + "," + name + "!")

greet() # هذي طريقة استدعاء الدالة المعرفة سابقًا
'''

# =====================================================

'''
10-2
مقدمة
'''

'''
def print_message():
    print("Welcome to Python")

print_message()

'''
# =====================================================

'''
10-3
استدعاء الدالة
'''

"""
أقدر استدعي الدالة أكثر من مرة زي التالي
"""

'''
def greet():
    name = input("Please enter your name:")
    time = input("Please enter the time of the day:")

    print("Good " + time + "," + name + "!")

greet()
greet()

'''

# =====================================================

'''
10-4
العلاقة بين استدعاء الدالة وتعريفها
'''

'''
def print_numbers():
    print(1)
    print(2)
    print(3)
    print(4)

print_numbers()
print_numbers()
print_numbers()

# التعديل على تعريف الدالة راح يأثر على جميع الاستدعاءات

'''

# =====================================================

'''
10-5
مدخل الدالة
Parameter
'''

'''
def print_numbers():
    for i in range(1,4):
        print(i)

print_numbers()
print_numbers()
print_numbers()

'''
" ___________________________________________________ "

"""
كيف أخلي ال range قابل للتغيير حسب رغبة المستخدم
هنا يجي دور أهمية الـ parameter واللي تخلي المستخدم يقدر يحدد اللي يبغاه
"""
'''
def print_numbers(to):
    for i in range(to):
        print(i)

print_numbers(2)
print_numbers(3)
print_numbers(5)

'''
# =====================================================

'''
10-6
تمرير أكثر من مدخل للدالة
'''

'''def add(n1,n2):
    print(n1+n2)

add(5,6)'''

# =====================================================

'''
10-7
تمرير قيمة غير متوقعة
'''

"""
راح يتم شرحها في الدروس القادمة لكيفية تفادي المدخلات غير المتوقعة
"""

# =====================================================

'''
10-8
إرجاع قيمة من الدالة
Return
'''

'''def add(n1,n2):
    result = n1+n2

    return result

add(5,6)'''

# =====================================================

'''
10-9
إمكانية استدعاء الدالة بأكثر من موضع
'''

'''def add(n1,n2):
    result = n1 + n2

    return result

value = add(7,2) - add(3,2)
print(value)'''

# =====================================================

'''
10-10
تمرير مخرجات دالة إلى دالة أخرى
'''

'''def add(n1,n2):
    return n1 + n2

value = add(2,9)
print(value)'''

" ___________________________________________________ "

""" 
أدخل ناتج الدالة الأولى في الدالة الثانية
"""

'''def print_numbers(to):
    for i in range(to):
        print(i)

print_numbers(value)'''

" ___________________________________________________ "

'''def add(n1,n2):
    return n1 + n2

def print_numbers(to):
    for i in range(to):
        print(i)

print_numbers(add(2,7))'''
# =====================================================

def multi(n):
    print('result: ')
    return n*n

print(multi(2))
