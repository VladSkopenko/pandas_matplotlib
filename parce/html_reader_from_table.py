import pandas as pd

tmp = pd.read_html("https://statisticstimes.com/tech/top-computer-languages.php", attrs={"id": "table_id1"})

print(tmp[0].head())

