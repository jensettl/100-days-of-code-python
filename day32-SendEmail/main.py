import smtplib

my_email = "testingsmtp.jens@gmail.com"
my_password = "testingsmtp"

# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()  # Transport Layer Security
# connection.login(user=my_email, password=my_password)
# connection.sendmail(
#     from_addr=my_email,
#     to_addrs="ettljens@gmail.com",
#     msg="Subject:Hello\n\nThis is the body of my email.",
# )
# connection.close()

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()  # Transport Layer Security
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="ettljens@gmail.com",
        msg="Subject:Hello\n\nThis is the body of my email.",
    )

# Note: Make sure to allow less secure apps in your Mail account by adding the following setting:
# https://myaccount.google.com/lesssecureapps

# Note: If you get an error message like this:
# smtplib.SMTPAuthenticationError: (534, b'5.7.14 <https://accounts.google.com/signin/continue?sarp=1&scc=1&plt=AKgnsbs

# Then you need to go to this link:
# https://accounts.google.com/DisplayUnlockCaptcha

# And then try to run your code again.

# run python code in the cloud with pythonanywhere.com
