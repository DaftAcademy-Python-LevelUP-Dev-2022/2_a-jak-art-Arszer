from types import MethodType


def greeter(func):
    def actual_greeter(*args):
        name = func(*args)
        return f'Aloha {name.title()}'
    return actual_greeter

def sums_of_str_elements_are_equal(func):
    def inner(*args):
        txt = func(*args)
        txt_split = txt.split()
        numbers = [[], []]
        k = 0
        for i in txt_split:
            negative = False
            for j in i:
                if j == '-':
                    negative = True
                    continue
                if negative == True:
                    numbers[k].append(-int(j))
                else:
                    numbers[k].append(int(j))
            k += 1
        left_number = sum(numbers[0])
        right_number = sum(numbers[1])
        if left_number == right_number:
            return f'{left_number} == {right_number}'
        else:
            return f'{left_number} != {right_number}'
    return inner

def format_output(*required_keys):
    def decorator(func):
        def inner(*args):
            keys = required_keys
            received_dict = func(*args)
            new_dict = {}
            for i in keys:
                value = ''
                x = i.split("__")
                for j in x:
                    if value != '':
                        value += ' '
                    if j in received_dict:
                        if received_dict[j] == '':
                            value = "Empty Value"
                        else:
                            value += received_dict[j]
                    else:
                        raise ValueError
                new_dict[i] = value
            return new_dict
        return inner
    return decorator


def add_method_to_instance(klass):
    def decorator(func):
        def inner(*args):
            val = func()
            return val
        setattr(klass, func.__name__, inner)
        return inner
    return decorator
