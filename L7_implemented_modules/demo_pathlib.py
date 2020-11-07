import pathlib
print("pathlib очень удобен для работы с путями!")

cwd = pathlib.Path.cwd() # возвращает уже не строку, а объект
print(cwd)
print(str(cwd))
print(repr(cwd))

p = pathlib.Path("/var")
print(repr(p), "exists?", p.exists())

p = pathlib.Path("/qwerty")
print(repr(p), "exists?", p.exists())

home = pathlib.Path.home()
print(repr(home))

downloads = home / "Downloads" # здесь / не является делением (деление переопределено)
print(repr(downloads))
print("Склеим произвольный путь:", downloads / 'qwerty' / '123456')
print("value: %s" % 'val')

print(home.joinpath("scripts", "python", "main.py"))

file_name = "file.txt"
file_path = cwd / file_name
print(file_path)

with file_path.open(mode="w") as f:# pathlib дает альтренативную возможность записи
    res = f.write("Hello world!")
    print("res (в байтах):", res)

print(file_path.read_text()) # так удобнее читать

f_path = pathlib.Path(file_name)
print("Relative path to the file: \n", f_path)

path = f_path.resolve() # full path
print("Full path to the file: \n", path)

print("Parent directory's path: \n", path.parent)
print("Pre-Parent directory's path: \n", path.parent.parent)

print(path.name)
print(path.parent.name)

print("Имя файла без расширения:", path.stem)
print("Расширение файла:", path.suffix)
print("Корень:", path.anchor)

print("Заменим расширение файла:\n", path.with_suffix(".py"))
print("Заменим имя файла:\n", path.with_name("new.py"))

print("Выведем пути до всех файлов:")
for p in cwd.iterdir():
    print(p)