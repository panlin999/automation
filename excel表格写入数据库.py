import pandas as pd
from sqlalchemy import create_engine

file = '建筑材料管理系统.xls'
df = pd.read_excel(file)

engine = create_engine("mysql+pymysql://root:root@localhost:3306/bank", encoding='utf-8')

df.to_sql('c0', con=engine, if_exists='replace', index=False)
