def greeter(func):
    def actual_greeter(*args):
        name = func(*args)
        return f'Aloha {name.title()}'
    return actual_greeter


def sums_of_str_elements_are_equal(func):
    pass


def format_output(*required_keys):
    pass


def add_method_to_instance(klass):
    pass
