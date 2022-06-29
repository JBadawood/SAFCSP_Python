# مقدمة عن البرمجة الكائنية | Object Oriented Programming

# =_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=

"""
1-1
مقدمة عن البرمجة الكائنية
"""

# =====================================================

"""
1-2 
مقدمة عن Class و Object
"""

# =====================================================

"""
1-3 
مقدمة عن Attributes و Methods
"""

# =====================================================

"""
1-4 
إنشاء Class
"""
'''
class Student:
    def __init__(self, name, age, id, grades):
        self.name = name
        self.age = age
        self.id = id
        self.grades = grades

    def talk(self):
        print('My name is: ', self.name)

'''
# =====================================================

"""
1-5 
إنشاء Object
"""

'''
class Student:
    def __init__(self, name, age, id, grades):
        self.name = name
        self.age = age
        self.id = id
        self.grades = grades

    def talk(self):
        print('My name is: ', self.name)

# طريقة إنشاء الـ object؟
std1 = Student('Jameel', 29, '2300512',98)

'___________________________________________'

# كيف نوصل للـ Object؟
print(std1.name)

'___________________________________________'

# كيف أوصل للـ method؟
std1.talk()

'''
# =====================================================

"""
1-6 
نظرة على self
"""
'''
class Student:
    def talk(self):
        print(self)


std1 = Student()
std2 = Student()

std1.talk()
std2.talk()

'''
'___________________________________________'

# نقدر نحط بدل الـ self أي اسم ثاني
'''
class Student:
    def talk(x):
        print(x)


std1 = Student()
std2 = Student()

std1.talk()
std2.talk()

'''
# =====================================================

"""
1-7 
مفهوم Constructor الجزء الأول
"""

# طريقة مطولة لإسناد القيم لكل خاصية
'''
class Student:
    def talk(self):
        print('My name is: ', self.name)

std1 = Student()

std1.name = 'Nouf'
std1.age = 21
std1.id = 'xx00'
std1.grades = 95

std1.talk()

'''
'___________________________________________'

# طريقة أفضل وأسرع

'''
الشرح في الجزء الثاني
'''

# =====================================================

"""
1-8 
مفهوم Constructor الجزء الثاني
"""

# الطريقة الأسهل عن طريق الـ constructor

'''
لو جربنا نشغل الخاصية بدون إضافة init راح يطلع لنا error
لأنه في الـ class لا يوجد constructor يستقبل قيم للخصائص
'''
'''
class Student:
    def talk(self):
        print('My name is: ', self.name)

std1 = Student('Nouf',21,'xx00',95)
print(std1.name)
'''
# std1.name = 'Nouf'
# std1.age = 21
# std1.id = 'xx00'
# std1.grades = 95

'___________________________________________'
'''
 الطريقة الصحيحة لإنشاء constructor
 هي وجود الدالة __init__
 نستفيد منها بإسناد الخصائص attribute وقت إنشاء الـ Object
 بدل ما نسندها كل مرة وقت استدعائها
'''

'''
class Student:
    def __init__(self, name, age, id, grades):
        self.name = name
        self.age = age
        self.id = id
        self.grades = grades

    def talk(self):
        print('My name is: ', self.name)

std1 = Student('Nouf',21,'xx00',95)
print(std1.name)
'''
'___________________________________________'

# نقدر نكتب الـ parameters كالتالي
'''
class Student:
    def __init__(self, x, y, z, e):
        self.name = x
        self.age = y
        self.id = z
        self.grades = e

    def talk(self):
        print('My name is: ', self.name)

std1 = Student('Nouf',21,'xx00',95)
print(std1.name)
'''
# =====================================================

"""
1-9 
مفهوم Encapsulation
"""

# =====================================================
