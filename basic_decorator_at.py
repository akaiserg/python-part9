import functools


user = {
    'username': 'jasonw',
    'access_level': 'admin'
}

def user_has_permission(func):
    @functools.wraps(func)
    def secure_function():
        if user.get('access_level') == 'admin':
            return func()
    return secure_function

@user_has_permission
def my_function(): # my_function is replaced by secure_function. this is fixed with functools
    """
        return the pass for admin panel
    """
    return 'password for admin panel is 1234'



print(my_function())
print(my_function.__name__)
print(my_function.__doc__)