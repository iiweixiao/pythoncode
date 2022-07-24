import pandas as pd

df = pd.read_excel("e3.xlsx", sheet_name="Sheet")
# 先按"桃子"列数据升序，数据一致是按"西瓜"列升序
df_value = df.sort_values(by=["桃子", "西瓜"], ascending=True)  # True为升序，False为降序

writer = pd.ExcelWriter("e5.xlsx")

df_value.to_excel(writer, sheet_name="Sheet2", index=False)
writer.save()
