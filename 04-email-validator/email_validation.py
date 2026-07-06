def validate_mail(email):
    return '.' in email and '@' in email


def write_log(message):
    with open (r"C:\Users\McImaga\Desktop\playground\04-email-validator\email activity.log", 'a') as file:
        file.write(message + '\n\n')


def email_cleaning(email):
    usermail = email.strip().lower()
    username, domain_name = usermail.split("@")
    return f"User name: {username}\n and Domain name: {domain_name}"




def user():
    write_log("This user is about to login... ")
    email = input("Enter your email address  ")

    if validate_mail(email):
        write_log(f"Welcome. These are the details you logged in with: {email_cleaning(email)}\nAnd this is your email address {email}")
    else:
        write_log("This is not a valid email address.")
    write_log("signing out...")


user()