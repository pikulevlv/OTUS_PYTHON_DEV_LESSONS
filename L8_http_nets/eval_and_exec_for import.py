import importlib
# math = importlib.import_module('math')
# exec('import math')
# print(math.sqrt(4))

print("Using eval()")
for i in ['1', '2', '3']:
    print(eval(f'{i} ** 2'), end=' ')

print('*'*30)

print('Using exec()')
module_list = ['math', 're', 'numpy', 'gdal2']
alias = {'numpy':'np',}
for m in module_list:
    if not m in alias.keys():
        try:
            exec(f'import {m}')
            print(f'import {m}: SUCCESS!')
        except Exception:
            print(f'import {m}: FAIL!')
    else:
        try:
            exec(f'import {m} as {alias[m]}')
            print(f'import {m}: SUCCESS!')
        except Exception:
            print(f'import {m}: FAIL!')

print(math.sqrt(4), np.array([1,2,3]) )
print('*'*30)