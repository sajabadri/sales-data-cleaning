import pandas as pd

df=pd.read_csv("messy_sales_practice.csv")

clean=[]
for product in df["product"]:
    p1=product
    p1=p1.strip().lower()
    clean.append(p1)

df["product"]=clean
df=df.drop_duplicates()

df["unit_price"]=pd.to_numeric(
    df["unit_price"],errors="coerce"
)

need_review=df[
    df["unit_price"].isna() |
    (df["quantity"] <=0) |
    df["quantity"].isna()
]

df=df.drop(index=need_review.index)

df["total"]=df["quantity"] * df["unit_price"]

print(need_review)
print("")
print(df)

df.to_csv("clean_sales.csv",index=False)
need_review.to_csv("needs_review.csv",index=False)
