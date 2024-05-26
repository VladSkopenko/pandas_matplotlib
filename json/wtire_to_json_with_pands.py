import pandas as pd

data = {
    "name": {"1": "Michael", "2": "John", "3": "Liza"},
    "country": {"1": "Canada", "2": "USA", "3": "Australia"}
}

employees = pd.DataFrame(data)

employees.to_json("employees.json", orient="split")
