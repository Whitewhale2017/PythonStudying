people = {'wyy': {'phone': '18012592490', 'sex': 'male'}, 'hty': {'phone': '15625455695', 'sex': 'female'},
          'gll': {'phone': '18916058036', 'sex': 'female'}, 'sf': {'phone': '14256985623', 'sex': 'female'}}
name=input("Input the name U want to Check:")
requset=input("U want check?p/s :")

key=requset
label=requset
if requset== 'p':
    key= 'phone'
    label='phone number'
if requset== 's':
    key= 'sex'
    label='sex'
print(f"{name} 's {label} is {people.get(name,{}).get(key,'not available')}")