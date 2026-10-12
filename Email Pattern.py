# Regular Expressions (Regex) - Email Pattern Matching
# Experiment 7: Based on the regular expressions theory and pseudocode

import re

def find_emails(text):
    # Standard email regex pattern matching username@domain.extension
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    
    # Use re.findall to find all matches of the pattern in the input string
    matches = re.findall(email_pattern, text)
    return matches


# Main Program
if __name__ == "__main__":
    sample_text = """
    Hello team, please reach out to the respective department leads for assistance:
    Support: support-team@mitadt.edu.in
    Admissions: admissions@mitadt.ac.in
    For general inquiries, you can also contact info@example.com or test.user+tag@sub.domain.org.
    """
    
    extracted_emails = find_emails(sample_text)
    
    print("Extracted Email Addresses:")
    for email in extracted_emails:
        print(f"- {email}")