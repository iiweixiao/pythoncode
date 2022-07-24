from pathlib import Path
from filecmp import cmp


"""
一键删除重复文件
"""

src_folder = Path('./pictures')
dest_folder = Path('./pictures_重复')

if not dest_folder.exists():
    dest_folder.mkdir(parents=True)

file_list = []
result = list(src_folder.rglob('*'))

for i in result:
    if i.is_file():
        file_list.append(i)

for m in file_list:  # [1,2,3,1,2] [1,2,3,1,2]
    for n in file_list:
        if m!=n and m.exists() and n.exists():
            if cmp(n, m):
                n.replace((dest_folder/n.name))
                n.unlink()
