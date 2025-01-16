from emails import *

file_path = 'email.txt'

with open(file_path, 'r') as f:
    email_content = f.read()


def main():
    print(f'Sender email: {email_sender(email_content)}')
    print(f'Recipient email: {email_recipient(email_content)}')
    print(f'Subject: {email_subject(email_content)}')
    print(f'Body: \n{email_body(email_content)}')


if __name__ == '__main__':
    main()