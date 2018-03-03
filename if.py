# import random
# from __builtin__ import raw_input
# secret = random.randint(1, 10)
# isdone = 0
# while (isdone < 4):
#     temp = input("Please input:")
#     guess = int(temp)
#     if guess == secret:
#         print('Yes')
#         # isdone=isdone+1
#         print(isdone)
#     else:
#         if guess > secret:
#             print('>')
#             isdone += 1
#             print(isdone)
#             print(id(isdone))
#         else:
#             print("<")
#             isdone = isdone + 1
#             print(isdone)
#             print(id(isdone))
# input("Press <enter>")
# for i in range(0,10):
#     print(i)

# while True:
#     word=input("enter a word:")
#     if not word:
#         print('Not enter')
#         break
#     print(word)

girls=['alice','beny','clark','cliss']
boys=['awk','bob','deck','alan']
lettergirs={}
for girl in girls:
    lettergirs.setdefault(girl[0],[]).append(girl)
# print(lettergirs.setdefault('a',[]))
# lettergirs.setdefault('a',[]).append('alwalk')
# print(lettergirs.setdefault('a',[]))
# for k,v in lettergirs.items():
#      print(k,v)
print([b+"+"+g for b in boys for g in lettergirs.get(b[0],[])])

# a = [1, 2, 4]
# b = (1, 2, 3)
# def cf(x):
#     for i in range(len(x)):
#         x[i] += x[i]
# cf(a)
# for i in range(len(a)):
#     print(a[i])
