import pandas as pd
df=pd.read_csv("C:\\Users\\86183\\Desktop\\数模校赛\\C题附件.csv")
description = df.describe()
print(df.describe())
# 指定导出的文件路径和文件名
output_file = 'C:\\Users\\86183\\Desktop\\描述统计信息.xlsx'
# 将描述统计信息导出为Excel表格
description.to_excel(output_file, index=False)
