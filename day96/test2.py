from pathlib import Path
from PIL import Image


src_folder = "./pictures/赵云"

dest_folder = "./赵云-1"

src_folder = Path(src_folder)
dest_folder = Path(dest_folder)

if not dest_folder.exists():
    dest_folder. mkdir(parents=True)

file_List = list(src_folder.glob('*. jpg'))

for i in file_List:
    dest_file = dest_folder/i.name
    dest_file = dest_file.with_suffix(".png") 
    Image.open(i).save(dest_file)
    print(f'{i.name}成功完成转换！')