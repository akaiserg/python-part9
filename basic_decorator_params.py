import functools


user = {
    'username': 'jasonw',
    'access_level': 'admin'
}

def third_level(access_level):
    def user_has_permission(func):
        @functools.wraps(func)
        def secure_function(panel):
            if user.get('access_level') == access_level:
                return func(panel)
        return secure_function
    return user_has_permission

@third_level('admin')
def my_function(panel): # my_function is replaced by secure_function. this is fixed with functools
    """
        return the pass for admin panel
    """
    return f'password for admin  panel ({panel}) is 1234'



print(my_function('create users'))
