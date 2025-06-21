def load_emails(filename):
    try:
        with open(filename, "r") as file:
            data = file.read()
            emails = [email.strip() for email in data.split(";") if email.strip()]
            return emails
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return []

def search_emails(emails, keyword):
    keyword = keyword.lower()
    return [email for email in emails if keyword in email.lower()]

def main():
    filename = input("Enter the path to the email file: ")
    emails = load_emails(filename)

    if not emails:
        print("No emails to search.")
        return

    keyword = input("Enter the name or keyword to search for: ")
    results = search_emails(emails, keyword)

    if results:
        print(f"\nEmails containing '{keyword}':")
        for email in results:
            print(f"- {email}")
    else:
        print(f"No emails found containing '{keyword}'.")

if __name__ == "__main__":
    main()