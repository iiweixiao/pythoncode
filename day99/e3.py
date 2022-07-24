from openpyxl import Workbook

wb = Workbook()
ws = wb.active

rows = [
    ['月份', '桃子', '西瓜', '龙眼'],
    [1, 38, 28, 29],
    [2, 52, 21, 35],
    [3, 39, 20, 69],
    [4, 51, 29, 41],
    [5, 39, 39, 31],
    [6, 30, 41, 39]
]

for row in rows:
    ws.append(row)

# 设置过滤范围
ws.auto_filter.ref = "A1:D7"
# 按列表内容筛选（过滤）
ws.auto_filter.add_filter_column(1, ["39", "29", "30"])
# Flase为升序，True为降序
ws.auto_filter.add_sort_condition("c2:c7", False)

wb.save('e3.xlsx')
