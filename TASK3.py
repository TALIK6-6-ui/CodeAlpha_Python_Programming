import re
import os

def extract_emails(text):
    """
    Extracts all email addresses from the input text using regex.
    Returns a sorted list of unique emails.
    """
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, text)
    return sorted(set(emails))  # Remove duplicates and sort

def read_file(file_path):
    """
    Reads the content of the file at the given path.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def save_emails_to_file(emails, output_path):
    """
    Writes extracted email addresses to the output file.
    """
    with open(output_path, 'w', encoding='utf-8') as file:
        for email in emails:
            file.write(email + '\n')

def main():
    print("📧 Email Extractor from .txt File")
    input_path = input("Enter the path to the .txt file: ").strip()

    # Check file existence
    if not os.path.isfile(input_path):
        print(f"❌ File not found: {input_path}")
        return

    try:
        text = read_file(input_path)
        emails = extract_emails(text)

        if emails:
            output_path = "emails_extracted.txt"
            save_emails_to_file(emails, output_path)
            print(f"✅ {len(emails)} unique email(s) saved to '{output_path}'")
        else:
            print("⚠️ No email addresses found in the file.")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    main()
