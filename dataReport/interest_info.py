# 按照模板生成付息通知

import pandas  as pd
import pypandoc
from docxtpl import DocxTemplate

df = pd.read_excel("D:\工作文件\季度利息\/2024年4季度\四季度利息.xlsx",index_col='客户名称')
print(df.head(3))

for name,row in df.iterrows():
    print("客户名称：" ,name)
    doc = DocxTemplate("D:\工作文件\季度利息\付息通知书-template.docx")
    doc.render(dict(name=name,balance=format(row["交易金额"], ',.2f'),interest=format(row["调整后利息"], ',.2f')))
    doc.save(f"D:\工作文件\季度利息\/2024年4季度/付息通知书-{name}.docx")


