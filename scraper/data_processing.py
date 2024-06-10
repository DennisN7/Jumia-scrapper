import pandas as pd

def process_data(data):
    # Example of processing: converting to DataFrame and cleaning data
    df = pd.DataFrame(data)
    
    # Clean price column (e.g., remove currency symbols and commas)
    df['Price'] = df['Price'].replace({'KSh': '', ',': ''}, regex=True).astype(float)
    
    return df
