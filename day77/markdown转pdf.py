from pathlib import Path
import os

work_dir = Path.cwd()  # <class 'pathlib.PosixPath'>。终端中执行脚本的目录，如在/home目录下运行此脚本，结果为/home

export_pdf_dir = work_dir / 'pdf'  # <class 'pathlib.PosixPath'>  拼接pdf目录

if not export_pdf_dir.exists():
    export_pdf_dir.mkdir()

# Path. glob(pattern)
# 找出在这个路径下包含或与pattern相同的目录，匹配索引文件（任何类型）：

for md_file in list(work_dir.glob('*.md')):
    md_file_name = md_file.name
    pdf_file_name = md_file_name.replace('.md', '.pdf')
    pdf_file = export_pdf_dir / pdf_file_name
    cmd = "pandoc '{}' -o '{}' --pdf-engine=xelatex -V mainfont='PingFang SC' --template=template.tex".format(md_file, pdf_file)
    os.system(cmd)