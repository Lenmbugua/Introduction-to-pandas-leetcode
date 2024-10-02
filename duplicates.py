import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    print("customers shape before dropping rows:", customers.shape)
    
    # Drop rows with duplicate email addresses, keeping the first occurrence
    customers.drop_duplicates(subset="email", inplace=True)
    
    print("customers shape after dropping rows:", customers.shape)
    
    return customers

# Example to test with the given input
customers = pd.DataFrame({
    'customer_id': [1, 2, 3, 4, 5, 6],
    'name': ['Ella', 'David', 'Zachary', 'Alice', 'Finn', 'Violet'],
    'email': ['emily@example.com', 'michael@example.com', 'sarah@example.com', 'john@example.com', 'john@example.com', 'alice@example.com']
})

# Call the function
customers = dropDuplicateEmails(customers)

# Display the resulting DataFrame
print(customers)
