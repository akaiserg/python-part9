def add_all(*args):
    return sum(args)

def pretty_print(**kwargs):
    for k,v in kwargs.items():
        print (f' For {k} we got {v}')
        


print(add_all(1,2,3,4,5,6))

pretty_print(username='jwill', access_level='admin')

pretty_print(**{'username':'jwill', 'access_level':'admin'})

