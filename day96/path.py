from pathlib import Path

path = '/Users/abc/Desktop'
path = Path(path)

search = '.md'

iter_a = path.rglob(f'*{search}*')

# print(type(path.rglob(f'*{search}*')))
l = list(path.rglob(f'*{search}*'))

for item in l:
    if item.is_dir():
        print(f'{item}是目录')
    else:
        print(f'{item}是文件')