# الدوال بشكل أعمق | Advanced Functions

# =_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=

"""
5-1
مفهوم Positional Arguments
"""

# تسمى كذلك بالـ Required Arguments
'''
يتم استقبالها بالترتيب 
والعدد لازم يتوافق مع عدد الـ Arguments 
'''
'''
def info(name, age):
    print('My name is {} and I am {} years old'.format(name,age))

info('Jameel', 29)

'''
'___________________________________________'

# لو بدلنا راح يصير خطأ أو نقصنا
'''
def info(name, age):
    print('My name is {} and I am {} years old'.format(name,age))

info('Jameel') # TypeError: info() missing 1 required positional argument: 'age'

info(29, 'Jameel') # My name is 29 and I am Jameel years old
'''
# =====================================================

"""
5-2 
مفهوم Keyword Arguments
"""

# الترتيب لا يهم لأنه استخدمنا الـ keyword
'''
def info(name, age):
    print('My name is {} and I am {} years old'.format(name,age))

info(age = 19, name = 'Jameel')
'''
'___________________________________________'
'''
def info(name, age):
    print('My name is {} and I am {} years old'.format(name,age))
    
info( name = 'Jameel',19) # SyntaxError: positional argument follows keyword argument
'''
'___________________________________________'

# بس نقدر نستخدم التالي بحيث يكون الـ positional أول واحد
'''
def info(name, age):
    print('My name is {} and I am {} years old'.format(name, age))


info('Jameel', age = 19) # My name is Jameel and I am 19 years old
'''
# =====================================================

"""
5-3
مفهوم Default Parameter
"""
# of Optional Parameter بدون ما نمرر قيم
# المقصود أنه توجد قيمة افتراضية للـ parameter
'''
def info(name = 'Jameel', age = 16, course = 'Python'):
    print('My name is '+ name + ', I am ',age,'years old and I am taking '+course+' course.')

info()
'''
'___________________________________________'

# طيب لو مررنا قيمة أيش ممن يصير
'''
def info(name = 'Jameel', age = 16, course = 'Python'):
    print('My name is '+ name + ', I am ',age,'years old and I am taking '+course+' course.')

info('جميل أحمد') # My name is جميل أحمد, I am  16 years old and I am taking Python course.

info('Jameel Ahmed', 28, 'Java') # My name is Jameel Ahmed, I am  28 years old and I am taking Java course.
'''
# =====================================================

"""
5-4 
مفهوم Argument Packing
"""

'''
يتم استقبال عدد لا محدود من الـ argument في parameter واحد
وتخزن على شكل Tuple

وهي طريقة عشان نسهل على المستخدم ادخال فقط أعداد بدون ما يدخل list

تستخدم مثلًًا في حساب متوسط الأعداد المدخلة
'''
'''
def avg(*args):
    total = sum(args)
    leng = len(args)

    average = total / leng

    print(average)

avg(7,8,5,8,5,8)
'''
'___________________________________________'

# عشان نشوف نوع البيانات
'''
def avg(*args):
    print(args)
    print(type(args)) # <class 'tuple'>

avg(7,8,5,8,5,8)

'''
'___________________________________________'

# نقدر نغير args إلى اسم آخر لكن المتعارف عليه بين المبرمجين هو args
'''
def avg(*num):
    print(num)
    print(type(num)) # <class 'tuple'>

avg(7,8,5,8,5,8)
'''
# =====================================================

"""
5-5 
مفهوم Argument Unpacking
"""

# كيف استخدم عناصر list, tuple or string  كـ  positional argument
'''
def info(name1, name2, name3):
    print("First student's name: ", name1)
    print("Second student's name: ", name2)
    print("Third student's name: ", name3)

names = 'Abdullah', 'Sara', 'Ahmed' # Tuple
info(names[0], names[1],names[2])
'''
'___________________________________________'

# توجد طريقة أخرى لاستخدام عناصر الـ Tuple بدل ما نكتبها زي السابق
'''
def info(name1, name2, name3):
    print("First student's name: ", name1)
    print("Second student's name: ", name2)
    print("Third student's name: ", name3)

names = 'Abdullah', 'Sara', 'Ahmed' # Tuple
info(*names)
'''
# =====================================================

"""
5-6 
استخدام Packing و Unpacking
"""

# Packing Tuple (Argument Tuple Packing):
'''
def my_func(*items):
    print(items)

my_func('a','b','c')
'''
'___________________________________________'

'''
def my_func(*items):
    print(items)

items = ['a','b','c']
my_func(items) # (['a', 'b', 'c'],)

'هنا تم أخذ الـ list كاملة كـ argument وحدة فقط'

# Unpacking (Argument Tuple Unpacking):

my_func(*items) # ('a', 'b', 'c')

' تم فصل كل argument لوحده '

'''
# =====================================================

"""
5-7 
مفهوم Dictionary Packing
"""

'''
راح نستقبل keyword Argument على شكل dictionary

راح يكون الاسم هو kwargs من keyword argument
وراح نستخدم العلامة ** عشان نعمل packing في الـ dictionary
'''
'''
def info(**kwargs):
    print(kwargs) # {'name': 'Ali', 'age': '17'}
    print(type(kwargs)) # <class 'dict'>

info(name = 'Ali', age = '17')
'''
'___________________________________________'

# كيف نوصل للـ Value
'''
def info(**kwargs):
    print('My name is', kwargs['name']) # My name is Ali

info(name = 'Ali', age = '17')
'''
'___________________________________________'

# طيب لو مررنا positional argument بدل الـ keyword argument
'''
def info(**kwargs):
    print('My name is', kwargs['name']) # My name is Ali

info('Ali', '17') # TypeError: info() takes 0 positional arguments but 2 were given
'''
# =====================================================

"""
5-8 
مفهوم Dictionary Unpacking
"""
'''
def info(name, age):
    print('My name is {} and I am {} years old'.format(name,age))

d={'name': 'Ali', 'age':17}
info(name='Ali', age=17) # My name is Ali and I am 17 years old
'''
'___________________________________________'

# أقدر أعمل Unpacking زي كذا
'''
def info(name, age):
    print('My name is {} and I am {} years old'.format(name,age))

d={'name': 'Ali', 'age':17}
info(**d) # My name is Ali and I am 17 years old
'''
# =====================================================

def my_func(*nums):
    print(nums)

nums = [1,2,3]

my_func(nums)
