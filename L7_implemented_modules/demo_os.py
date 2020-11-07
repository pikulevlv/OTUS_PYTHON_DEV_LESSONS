import os
import subprocess #

def demo_os_base():
    print(os.name)
    print(os.environ)  # переменные окружения
    print(os.environ['PATH'])
    print(os.environ['HOME'])
    print(os.environ['PYTHONUNBUFFERED'])
    print(os.environ['SECRET_KEY'])
    print(os.environ.get('SECRET_KEY'))
    print(os.environ.get('SECRET_KEY_2'))

    cwd = os.getcwd()  # текущая директория выполняемого файла
    print(cwd)

    subdir = os.path.join(cwd, "subdir")  # склеить пути
    print("subdir", subdir)
    print("subdir существует?", os.path.isdir(subdir))
    if os.path.isdir(subdir):
        print("subdir already exists")
    else:
        # os.makedirs() # будут созданы все папки, недостающие до той папки, которую мы создаем
        os.mkdir(subdir)  # если более высоких директорий нет, получим ошибку
        print("Made subdir.")
    print("subdir существует?", os.path.isdir(subdir))

    print('Сменим директорию и будем работать уже в ней')
    os.chdir(subdir)
    print(os.getcwd())
def demo_file():
    filename = "file.txt"
    with open(filename, 'w'):
        pass
    print(os.listdir(".")) # передаем точку, т.к. обращаемся к текущей директории. Аналог ls
    print("Rights:", os.stat("."))
    print("Remove subdir")
    # os.remove()
    os.unlink(filename)
    print("filename существует?", os.path.isdir(filename))
    res = os.system("ls -la") #system принимает привычные команды из командной строки
    print("res:", res)

def demo_walk():
    # пройтись по текущей директории. Вернет кортеж
    for root, dirs, files in os.walk(".", topdown=False):
        print("root", root)
        print("dirs:")
        for d in dirs:
            print("-", d)
        print("files:")
        for f in files:
            print("-", f)
cwd = os.getcwd()
print("cwd:", cwd)
print("base name cwd (имя текущей директории):", os.path.basename(cwd))
print("dir name cwd (абс.адрес родительской директории):", os.path.dirname(cwd))
print(os.path.exists(cwd))
print("Разделим путь и текущую директорию:\n", os.path.split(cwd))
file_path = os.path.join(cwd, 'filename.txt')
print("Разделим путь и имя файла:\n", os.path.split(file_path))
print("base name cwd (имя текущего файла):", os.path.basename(file_path))
print("dir name cwd (абс.адрес родительской директории):", os.path.dirname(file_path))

if __name__ == '__main__':
    # demo_os_base()
    # demo_file()
    # demo_walk()
    pass

