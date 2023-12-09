"""
DB File: Read and write content
"""
import timeit
def time_execution(f):
    """fuck"""
    def wrapper():
        st = timeit.default_timer()
        soma = f()
        end = timeit.default_timer() - st
        print(f"time spent: {end}")
        return soma
    return wrapper

FILE_NAME = 'dist/deezer.txt'


def save_on_db(file_name, content: dict):
    """
    Pass filename and object content to write in file
    """
    with open(file_name, "a", encoding="UTF-8") as file:
        line = ''
        for key, value in content.items():
            line += f'{key}:{value},'
        if line:
            file.write(line[:-1]+'\n')


def get_from_db(file_name):
    """
    Pass filename and return all content on array of objects
    """
    list_content = []
    with open(file_name, "r", encoding="UTF-8") as file:
        file = file.read()
        for lines in file.split('\n'):
            line = lines.split(",")
            if lines:
                object_person = {}
                for value in line:
                    key, value = value.split(':')
                    object_person.setdefault(key, value)
                list_content.append(object_person)
    return list_content

# save_on_db(FILE_NAME, {'name': 'Jorge', 'year': 212})
# get_from_db(FILE_NAME)
