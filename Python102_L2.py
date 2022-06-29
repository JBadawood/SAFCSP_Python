# أنواع البيانات المتقدمة بشكل أعمق | Advanced Sequence

# =_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=

'''
2-1
مفهوم Indexing
'''
# string[index]
"""
alphabet = 'abcdefghijklmnopqrstuvwxyz'
print(alphabet[0]) # a
"""
" ___________________________________________"

"""
alphabet = 'abcdefghijklmnopqrstuvwxyz'
print(alphabet[-1]) # z
"""
" ___________________________________________"

# list[index]
"""
the_list = [1,2,3]
print(the_list[-1]) #3
"""
" ___________________________________________"

# tuple[index]
"""
the_tuple = (1,2,3)
print(the_tuple[-1]) #3
"""
# =====================================================

'''
2-2
مفهوم Slicing
'''
# string[start:end:step]
"""
text = "This is Python course"
print(text[8:14])
print(text[:7])
print(text[8:])
print(text[:])
print(text[-6:])
"""
" ___________________________________________"

# list[start:end:step]
"""
the_list = [1,2,3,4,5,6]
print(the_list[-3:])
"""
" ___________________________________________"

# tuple[start:end:step]
"""
the_tuple = (1,2,3,4,5,6)
print(the_tuple[-3:])
"""
# =====================================================

'''
2-3
مفهوم Slicing الجزء الثاني
'''
# string[start:end:step]
"""
alphabet = 'abcdefghijklmnopqrstuvwxyz'
print(alphabet[0:7:2])
print(alphabet[5:0:-1])
"""
" ___________________________________________"
"""
the_list = [1,2,3,4,5,6]
print(the_list[3:0:-2])
"""
" ___________________________________________"
"""
the_tuple = (1,2,3,4,5,6)
print(the_tuple[3:0:-2])
"""
# =====================================================

'''
2-4
الدالة slice
'''
# string(slice(start,end,step))
"""
alphabet = 'abcdefghijklmnopqrstuvwxyz'
s = slice(0,5,2)
print(alphabet[s])
"""
" ___________________________________________"
"""
the_list = [1,2,3,4,5,6]
s=slice(0,5,2)
print(the_list[s])
"""
" ___________________________________________"
"""
the_tuple = (1,2,3,4,5,6)
s=slice(0,5,2)
print(the_tuple[s])
"""
# =====================================================

'''
2-5
الدالة index
'''
# string.index("text")
"""
text ="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do"
print(text.index('do'))
"""
" ___________________________________________"
"""
the_list = [1,2,2,3]
the_tuple =(4,5)
print(the_list.index(2))
print(the_tuple.index(4))
"""
# =====================================================

'''
2-6
الدالة len
'''
# len(string)
"""
alphabet = 'abcdefghijklmnopqrstuvwxyz'
print(len(alphabet))
"""
" ___________________________________________"
"""
the_list = [1,2,3,4]
print(len(the_list))
"""
" ___________________________________________"
"""
the_tuple =(1,2,3)
print(len(the_tuple))
"""
# =====================================================

'''
2-7
الدالة count
'''
# string.count('letter' or 'word')
"""
the_string = "This is the student Noora"
print(the_string.count('s'))
print(the_string.count('Noora'))
"""
" ___________________________________________"
"""
the_list = [1,2,2,3,3,3,3]
print(the_list.count(3))
"""
" ___________________________________________"
"""
the_tuple = (4,4,4,4,5,5,5,5,5)
print(the_tuple.count(4))
"""
# =====================================================

'''
2-8
المعامل in
'''
"""
text ="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do"
print('dol' in text)
"""
" ___________________________________________"
"""
the_tuple = (4,4,4,4,5,5,5,5,5)
the_list = [1,2,2,3,3,3,3]
print(1 in the_list)
print(1 in the_tuple)
"""
# =====================================================

'''
2-9
الدمج والتكرار
'''
"""
first = 'Jameel'
second = 'Ahmed '

print(first + " "+second)
print(second *3)
"""
" ___________________________________________"
"""
list1 = [1,2,3]
list2 = [4,5,6]
print(list1+list2)
print(list1*3)
"""
" ___________________________________________"
"""
tuple1 = (1,2,3)
tuple2 = (4,5,6)
print(tuple1+tuple2)
print(tuple2*3)
"""
# =====================================================

txt = "Python"
print(txt[0:5:3])
