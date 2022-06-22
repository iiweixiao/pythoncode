import pdfplumber
import pandas as pd

# 提取pdf表格
lst = []  # 用于保存每行数据
with pdfplumber.open("example.pdf") as pdf:
    # page01 = pdf.pages[0]  # 指定页码
    # table1 = page01.extract_table()  # 提取单个表格
    # table2 = page01.extract_tables()  # 提取多个表格
    for i in range(22):
        page = pdf.pages[i]  # 指定页码
        table = page.extract_table()  # 提取单个表格
        lst.extend(table)
        print(i+1, '完成一页表格转换')


# python+pandas 保存list到本地
def deal():
    # 二维list
    # list = [['腾讯', '北京'], ['阿里巴巴', '杭州'], ['字节跳动', '北京']]

    # list转dataframe
    df = pd.DataFrame(lst, columns=['1', '2', '3', '4', '5'])

    # 保存到本地excel
    df.to_excel("pdf_table.xlsx", index=False)


if __name__ == '__main__':
    deal()
