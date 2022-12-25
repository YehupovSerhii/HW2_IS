# Написать декоратор call_times, который будет принимать в качестве параметра file_name,
# считать количество вызовов функций и записывать в файл в формате f'{func_name} была вызвана {count} раза.\n'

#boo была вызвана 1 раз(а)
#moo была вызвана 2 раз(а)
#voo была вызвана 1 раз(а)

#boo()
#moo()
#voo()
#moo()




# Пример:
# @call_times('foo.txt')
# def foo():
#   pass
# @call_times('foo.txt')
# def boo():
#   pass
# @call_times('calls.txt')
# def doo():
#   pass
# foo()
# boo()
# foo()
# foo()
# boo()
# doo()

# Файл foo.txt:
# foo была вызвана 3 раза
# boo была вызвана 2 раза
# Файл calls.txt:
# doo была вызвана 1 раза
# *****************************

def call_times(file_name):
    def decorator (func):
        def wrapper(*args,**kwargs):
            n = new_data = old_data = ''
            with open(file_name, 'r') as f:
                old_data = f.read()
            input_function_name = func.__name__
            func_exists = False
            if old_data:
                n = f'\n'
                for line in old_data.split('\n'):
                    words = line.split()
                    function_name = words[0].replace(' ', '')
                    count = int(words[3].replace(' ', ''))
                    # print(f'{function_name} => {count}')
                    if input_function_name == function_name:
                        new_data = old_data.replace(line, f'{func.__name__} была вызвана {count + 1} раза.')
                        func_exists = True
                        break
            if not func_exists:
                with open(file_name, "a") as f:
                    f.write(f'{n}{func.__name__} была вызвана 1 раза.')
            else:
                with open(file_name, "w") as f:
                    f.write(new_data)
        return wrapper

    return decorator


@call_times("foo.txt")
def foo():
    pass

@call_times("foo.txt")
def boo():
    pass

@call_times("foo.txt")
def boo():
    pass

@call_times("calls.txt")
def doo():
    pass

foo()
boo()
foo()
foo()
boo()
doo()


