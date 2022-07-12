# الخصائص والدوال | Attributes and Methods

# =_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=

"""
2-1
الدالة dir
"""
'''
class Student:
    def __init__(self, name,age,id,grades):
        self.name = name
        self.age = age
        self.id = id
        self.grades = grades

        def talk(self):
            print('My name is: ',self.name)

std1 = Student('Nouf', 21, 'xx00', [95,98,99])
std2 = Student('Hessah', 19, 'xx01', 86)

print(dir(std1))
'''
# =====================================================
"""
2-2
إضافة Attribute
"""
# كيف أضيف attribute إضافية لـ object معين؟
# مثلُا إضافة الساعات التطوعية للطالب
'''
class Student:
    def __init__(self, name,age,id,grades):
        self.name = name
        self.age = age
        self.id = id
        self.grades = grades

        def talk(self):
            print('My name is: ',self.name)

std1 = Student('Nouf', 21, 'xx00', [95,98,99])
std2 = Student('Hessah', 19, 'xx01', 86)

# إضافة الساعات التطوعية للطالبة حصة (attribute)
std2.v_hours = 16
print(dir(std2))

'___________________________________________'

# هل تأثر الـ std1 بعد هذا التغيير

print(dir(std1))  # نلاحظ أنه ما تأثر

'''
# =====================================================
"""
2-3
حذف Attributes و Object
"""
'''
class Student:
    def __init__(self, name,age,id,grades):
        self.name = name
        self.age = age
        self.id = id
        self.grades = grades

        def talk(self):
            print('My name is: ',self.name)

std1 = Student('Nouf', 21, 'xx00', [95,98,99])
std2 = Student('Hessah', 19, 'xx01', 86)

std2.v_hours = 16
print(dir(std2))

# كيف نحذف ساعات التطوع اللي أضفناها سابقًا
del std2.v_hours
print(dir(std2))
'''
'___________________________________________'

# كيف أحذف object كامل
'''
class Student:
    def __init__(self, name,age,id,grades):
        self.name = name
        self.age = age
        self.id = id
        self.grades = grades

        def talk(self):
            print('My name is: ',self.name)

std1 = Student('Nouf', 21, 'xx00', [95,98,99])
std2 = Student('Hessah', 19, 'xx01', 86)

del std2

print(std1)
print(std2)  # NameError: name 'std2' is not defined لأنه تم حذفه

'''
# =====================================================
"""
2-4
مفهوم Class Attribute
"""
# هو لمن يكون لدي تكرار في الخصائص لمختلف المدخلات نقدر نحطه فقط في الـ class بدل إدخاله كل مرة
# يسمى بـ:
# Class Attribute
# Static Members
# Static Data

# =====================================================
"""
2-5
تطبيق Class Atrribute
"""

# نلاحظ هنا الإدخال لقيم اسم الجامعة تكرر لكلا الطالبين
'''
class Student:
    def __init__(self, name,age,id,grades,university_name):
        self.name = name
        self.age = age
        self.id = id
        self.grades = grades
        self.university_name = university_name


std1 = Student('Nouf', 21, 'xx00', [95,98,99], 'King Saud University')
std2 = Student('Hessah', 19, 'xx01', 86, 'King Saud University')

print(std2.university_name)
print(std1.university_name)
'''
'___________________________________________'

# كيف أحول هذا التكرار إلى Static Member (Class Attribute)
'''
class Student:
    university_name = 'King Saud University'  # Static Member
    def __init__(self, name,age,id,grades):
        self.name = name
        self.age = age
        self.id = id
        self.grades = grades


std1 = Student('Nouf', 21, 'xx00', [95,98,99])
std2 = Student('Hessah', 19, 'xx01', 86)

print(std2.university_name)
print(std1.university_name)
'''
# =====================================================
"""
2-6
نظرة على Setter و Getter
"""

# مهمة عشان ما نغير على البيانات المدخلة بشكل مباشر
# يعتبر هذا الإجراء لاتباع الـ encapsulation
# واللي تعني المحافظة على الـ Data Integrity سلامة البيانات من التغييرات المفاجئة
# لضمان أن أي object أو اي شي خارج الـ class أنه يأثر على البيانات حقنا
'''
class MyClass:
    # Setter
    def set_val(self, value):
        self.value = value

    # Getter
    def get_val(self):
        return self.value

a = MyClass()
b = MyClass()

a.set_val(10)
b.set_val(100)

print(a.get_val())
print(b.get_val())

'''
'___________________________________________'

# نقدر نغيير البيانات بشكل مباشر زي كذا
'''
class MyClass:
    # Setter
    def set_val(self, value):
        self.value = value

    # Getter
    def get_val(self):
        return self.value

a = MyClass()
b = MyClass()

a.set_val(10)
a.value = 'hello'
b.set_val(100)

print(a.get_val())
print(a.value)
print(b.get_val())

'''
# =====================================================
"""
2-7
تطبيق Setter و Getter
"""

# كيف نحافظ على الـ Data Integrity بواسطة الـ Setter و الـ Getter؟
# كيف راح تخدمنا عشان موضوع سلامة البيانات Data Integrity
'''
class MyInteger:
    def set_val(self, val):
        if(type(val) == int):
            self.val = val
        else:
            print('The value is not an integer')

    def get_val(self):
        return self.val

    def increment_val(self):
        self.val+= 1

i = MyInteger()

i.set_val(9)
print(i.get_val())

# هنا نلاحظ أهمية الـ Setter عشان ما يتعطل البرنامج
i.set_val('Hello')
print(i.get_val())

'''
'___________________________________________'

# لو مررنا القيمة بشكل مباشر بدون الـ setter راح يتعطل البرنامج
'''
class MyInteger:
    def set_val(self, val):
        if(type(val) == int):
            self.val = val
        else:
            print('The value is not an integer')

    def get_val(self):
        return self.val

    def increment_val(self):
        self.val+= 1

i = MyInteger()

i.val = 'hello'
i.increment_val() # TypeError: can only concatenate str (not "int") to str

'''
# =====================================================
"""
2-8
نظرة على Access Modifiers
"""

'''
هي طريقة لتقييد كل من:
- Attributes الخصائص
- Methods الدوال

يوجد ثلاث أنواع من الـ Access Modifiers:
1- Public (قابلة للوصول) (النوع الافتراضي لجميع الخصائص والدوال)
    x = 10
    
2- Protected (علامة على أنها Private ولكنها قابلة للوصل)
    _x = 10

3- Private (غير قابلة للوصول)
    __x = 10
    
    
الدرس التالي يوضح طريقة تمثيلها برمجيًا

'''

# =====================================================
"""
2-9
Access Modifiers مع الخصائص
Attributes
"""
'''
class Employee:
    def __init__(self,name):
        self.name = name  # public
        self._tel = '+96655xxxxxxx'  # protected
        self.__salary = 1700  # private

emp1 = Employee('Abdullah')

print(emp1.name)
print(emp1._tel)
print(emp1.__salary)  # AttributeError: 'Employee' object has no attribute '__salary' لأنها private

'''
'___________________________________________'

# الآن نعمل set للقيمة private ونشوف ايش يصير
'''
class Employee:
    def __init__(self,name):
        self.name = name  # public
        self._tel = '+96655xxxxxxx'  # protected
        self.__salary = 1700  # private

emp1 = Employee('Abdullah')

print(emp1.name)
print(emp1._tel)

emp1.__salary = 50
print(emp1.__salary)  # في هذه الحالة قدرنا نوصل للـ attribute بعد عمل set


#وهذه إحدى فوائد الـ Getter و الـ Setter
#في أننا نوصل للـ data بشكل غير مباشر

'''

'___________________________________________'

# نقدر نوصل للـ private attributes عن طريق الـ Getters
'''
class Employee:
    def __init__(self,name):
        self.name = name  # public
        self._tel = '+96655xxxxxxx'  # protected
        self.__salary = 1700  # private

    def get_salary(self):
        return self.__salary

emp1 = Employee('Abdullah')

print(emp1.get_salary())

'''
# =====================================================
"""
2-10
Access Modifiers مع الدوال
Methods
"""
'''
class Employee:
    def __init__(self,name):
        self.name = name  # public attribute
        self._tel = '+96655xxxxxxx'  # protected attribute
        self.__salary = 1700  # private attribute

    # _job_title() protected method
    def _job_title(self):
        print('Programmer')

    # __give_raise() private method
    def __give_raise(self):
        self.__salary = self.__salary + 500
        print('Your Salary now is: ', self.__salary)

emp1 = Employee('Abdullah')

# نحاول نوصل لكل من _job_title() و __give_raise()

emp1._job_title()
emp1.__give_raise()  # AttributeError: 'Employee' object has no attribute '__give_raise' لأنها private method

'''
'___________________________________________'

# كيف نوصل للـ private method خارج الـ Class
# في هذه الحالة نحتاج لـ getter

class Employee:
    def __init__(self,name):
        self.name = name  # public attribute
        self._tel = '+96655xxxxxxx'  # protected attribute
        self.__salary = 1700  # private attribute

    # _job_title() protected method
    def _job_title(self):
        print('Programmer')

    # __give_raise() private method
    def __give_raise(self):
        self.__salary = self.__salary + 500
        print('Your Salary now is: ', self.__salary)

    # Getter method
    def get_raise(self):
        self.__give_raise()

emp1 = Employee('Abdullah')

emp1.get_raise()  # قدرنا نوصلها عن طريق الـ getter method وليس الـ method نفسها

# =====================================================
