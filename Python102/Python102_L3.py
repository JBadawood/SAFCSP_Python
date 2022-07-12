# النصوص بشكل أعمق | Advanced Strings

# =_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=

"""
3-1
البحث باستخدام الدالة find
"""
# string.find(character)

'''
text ="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do"
print(text.find('do')) # راح تعطينا أول تطابق في البحث
'''
'___________________________________________'

# كيف أوصل لآخر تتطابق؟

'''
print(text.rfind('do'))
'''
'___________________________________________'

# لو بحثنا عن شيء غير موجود في النص السابق

'''
print(text.find('xxx'))
print(text.rfind('xxx')) # ترجع لنا النتيجة بـ -1
'''
'___________________________________________'

# أقدر أحدد نطاق البحث كالتي
'''
print(text.find('it'))
print(text.find('it',50,60))
'''
# =====================================================

"""
3-2
تحويل النص إلى قائمة
"""
# string.split(character)

'''
text = 'A, B, C'
string_to_list = text.split() # يفصلها لأن يوجد فراغات
print(string_to_list)
'''
'___________________________________________'
'''
text = 'A,B,C'
string_to_list = text.split() # ما فصلها لأنه لا يوجد فراغات
print(string_to_list)
'''
'___________________________________________'

# عشان كذا لازم أحدد فين تنفصل بالضبط
'''
text = 'A,B,C'
string_to_list = text.split(',') # يفصل لمن يلقى الفاصلة
print(string_to_list)
'''
'___________________________________________'
'''
text = 'This is a string'
string_to_list = text.split('s') # يفصل لمن يلقى حرف الـ s
print(string_to_list)
'''
'___________________________________________'

# تستقبل الدالة split كم مرة راح يتم التقسيم كالتي:
'''
text = 'This is a string'
string_to_list = text.split('s',1) # يفصل لمن يلقى حرف الـ s ومرة واحدة فقط
print(string_to_list)
'''
# =====================================================

"""
3-3
التحويل إلى نص
"""
# character.join(list)
'''
text = 'A, B, C, D'
string_to_list = text.split(',')
print(string_to_list)
'''
'___________________________________________'

# كيف أحول List إلى string؟ عن طريق join
'''
list_to_string = " ".join(string_to_list)
print(list_to_string)
'''
'___________________________________________'

# كذلك تحول الـ tuple و الـ dictionary
'''
list_to_string = "#".join(string_to_list)
print(list_to_string)
'''
# =====================================================

"""
3-4
التحقق من النص
"""
# string.isalnum()
# string.isdigit()

# كيف أشيك على نص معين؟
'''
استخدم هذه الـ methods عشان تختصر علي
بدل استخدام الـ loop
'''
'''
values = 'A987'
print(values.isalnum()) # True لان النص عبارة عن حروف وأرقام فقط

values = 'A9 87'
print(values.isalnum()) # False لأن النص فيها فراغ وهذا مايحسب كرقم أو حرف
'''
'___________________________________________'
'''
values = '987'
print(values.isdigit())
'''
# =====================================================

"""
3-5
الدالة replace
"""
# string.replace(old_char, new_char)
'''
values='1\n2\n3\n4\n5\n6'
print(values)

print(values.replace('\n',','))
'''
'___________________________________________'

# نقدر نحدد عدد مرات التبديل كالتالي:
'''
values='1\n2\n3\n4\n5\n6'
print(values.replace('\n',',',2))
'''
# =====================================================

"""
3-6
الدالة strip
"""
# string.strip()

# كيف أحذف الفراغات الزايدة في اللي موجودة في بداية ونهاية النص؟
'''
text = '     python course      '
print(text)
print(len(text))
print(text.strip())
'''
'___________________________________________'
'''
# لو أبغى أحذف فقط المسافة اللي في البداية استخدم lstrip
text = '     python course      '
print(text.lstrip())
print(text.rstrip())
'''
'___________________________________________'

# لو أبغى أتخلص من الـ Newline اكتب التالي:
'''
text = '\npython course'
print(text)
print(text.strip())
'''
# =====================================================

"""
3-7
التلاعب في النص
"""

# كيف أخلي النص بالأحرف الكبيرة أو الصغيرة؟
'''
string = 'This is Python Course'
print(string.lower())
print(string.upper())
print(string.swapcase()) # يعكس الأحرف الكبيرة لصغيرة والعكس
print(string.title())  # يخلي بس الحروف الأولى كبيرة
'''
# =====================================================

"""
3-8
مفهوم Raw String
"""
'''
string = "\tPython"
print(string)
'''
'___________________________________________'


'''
#كيف أطبع backslach في نص؟
file_path = 'C:\\xMyFolder\\xMySubFolder'
print(file_path)


# أو عن طريق الـ raw string بإضافة r أو R

file_path = r'C:\\xMyFolder\\xMySubFolder'
print(file_path)

file_path = R'C:\\xMyFolder\\xMySubFolder'
print(file_path)

'''
# =====================================================

"""
3-9
الدالة format
"""
'''
first_name = 'Saleh'
last_name = 'Mohammed'

age = 19
print('My name is {} {}, and I am {} years old'.format(first_name,last_name,age))
'''
'___________________________________________'

# نقدر نبدل المتغيرات بإضافة رقم الـ index
'''
print('My name is {1} {0}, and I am {2} years old'.format(first_name,last_name,age))
'''
'___________________________________________'

# أو نقدر نبدل هذه الاسماء كالتالي
'''
print('My name is {f_name} {l_name}, and I am {old} years old'.format(l_name=first_name,f_name = last_name,old = age))
'''
# =====================================================

