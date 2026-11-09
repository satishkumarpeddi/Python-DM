from mlxtend.preprocessing import TransactionEncoder 
from mlxtend.frequent_patterns import fpgrowth 
import pandas as pd

dataset = [
    ["milk","better","butter"],
    ["bread","butter"],
    ["milk","butter"],
    ["milk","bread"],
    ["milk","better","butter"]
]


te = TransactionEncoder()

te_array = te.fit(dataset).transform(dataset)

df = pd.DataFrame(te_array,columns=te.columns_)

frequent_items = fpgrowth(
    df,
    min_support=0.4,
    use_colnames=True
)


print(f"Frequent Itemsets: ")
print(frequent_items)