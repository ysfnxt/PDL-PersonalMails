import pandas as pd
import tldextract

# Define a function to classify an email address as personal or business
def classify_email(email):
    domain = tldextract.extract(email).domain
    personal_domains = ['gmail', 'yahoo', 'hotmail', 'outlook', 'aol']
    if domain in personal_domains:
        return 'Personal'
    else:
        return 'Business'

# Load the data into a Pandas DataFrame
data = pd.read_csv('sample.csv')

# Apply the function to the 'Email' column and create a new 'Type' column
data['Type'] = data['email'].apply(classify_email)

# Save the updated DataFrame to a new CSV file
data.to_csv('emails_with_types.csv', index=False)