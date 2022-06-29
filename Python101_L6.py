'''
______________________________________________________
______________________________________________________
'''

# 6-1
# مفهوم المعاملات

#Arithmetic Operators

#معامل الجمع
'''result= 2+5
print(result)'''

#معامل الطرح
'''result = 4-12
print(result)'''

# معامل الضرب
'''result = 2*2
print(result)'''

# معامل القسمة
'''result = 2/6
print(result)'''

#معامل باقي القسمة
'''result = 10%3
print(result)'''

#صيغة مختصرة
'''result = 10
result -=5 # short of (result = result - 5)
print(result)'''
#نقدر نطبقها على العمليات الحسابية الأخرى
'''result = 10
result *=5
print(result)'''

'''result = 10
result /=5
print(result)'''

'''result = 10
result +=5
print(result)'''

"______________________________________________________"

# Comparison Operators
'ترجع لنا قيمة True أو False'

#معامل التساوي
'''result = 6==3
print(result) '''

# معامل عدم التساوي
'''result = 8!=7
print(result)'''

# معامل أكبر من , و أكبر من أو يساوي
'''result = 3>2
print(result)'''

'''result = 3>=3
print(result)'''

# معامل أصغر من، وأصغر من أو يساوي
'''result = 1<4
print(result)'''

'''result = 7<=3
print(result)'''

"______________________________________________________"

# Logical Operators

# المعامل AND
'''not_raining = True
not_foggy = True

is_sunny = not_raining and not_foggy
print(is_sunny)'''

# المعامل OR
'''is_raining = True
is_foggy = False

not_sunny = is_raining or is_foggy
print(not_sunny)'''

# المعامل NOT

'''is_student = True
print(not is_student)'''

# الفرق بين And و Or و Not

'''first, second = True,False

and_result = first and second
or_result = first or second
not_result = not second

print(and_result)
print(or_result)
print(not_result)'''

'''
______________________________________________________
______________________________________________________
'''
#6-2
# أنواع البيانات

'''# النوع String
name = 'Ahmed'

# النوع Integer
age = 20

# النوع Float
age_float = 20.00

# النوع Boolean
is_student = True
is_employee = False

# النوع None
home_address = None # فارغ أو يحتوي قيمة غير معروفة'''


"______________________________________________________"

# معرفة نوع البيانات
"""
عبر دالة
type()
"""

'''print(type(name))
print(type(age))
print(type(age_float))
print(type(is_student))
print(type(home_address))'''

'''
______________________________________________________
______________________________________________________
'''
#6-6
# أنواع البيانات في الأرقام

'''age = 25
weight = 50.5
complex_num = 10j
comp_number = 10J

print(type(age))
print(type(weight))
print(type(complex_num))
print(type(comp_number))'''

'''
______________________________________________________
______________________________________________________
'''

#6-7
"""
الدوال
str() , int() , float()
"""
name = "Salman"
age = 28
weight = 55.7

age_float = float(age)
print(age_float)

weight_int = int(weight)
print(weight_int)

age_string = str(age)
print(age_string)

print(type(age_string))