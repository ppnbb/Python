user_id = input('id?')
user_pwd = input('password?')

'''
if user_input == '111111':
    print('Hello master')
else:
    print('Who r u?')
'''

'''
if user_id == 'egoing':
    if user_pwd == '111111':
        print('Hello master')
    else:
        print('Who r u?')
else:
    print('Who r u?')
'''

#logical operator
if user_id == 'egoing' and user_pwd == '111111':
    print('Hello master')
elif user_id == 'leezche' and user_pwd == '222':
    print('Hello master')
else:
    print('Who r u?')