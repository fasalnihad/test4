import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    low_Salary_count = accounts[accounts['income'] < 20000].shape[0]
    average_Salary_count = accounts[(accounts['income'] >= 20000) & (accounts['income'] <= 50000)].shape[0]
    high_Salary_count = accounts[accounts['income'] > 50000].shape[0]

    result = pd.DataFrame({
        'category': ["Low Salary", "Average Salary", "High Salary"],
        'accounts_count':[low_Salary_count, average_Salary_count, high_Salary_count]
    })
    return result
