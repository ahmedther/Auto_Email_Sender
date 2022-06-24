import smtplib
import base64

filename = "Query OPD Data.xlsx"


# Read a file and encode it into base64 format
fo = open(filename, "rb")
filecontent = fo.read()
# encodedcontent = base64.b64encode(filecontent)  # base64

sender = 'sarika.jadhav@kokilabenhospitals.com'
receivers = ['ahmed.qureshi@kokilabenhospitals.com']

marker = "AUNIQUEMARKER"

body ="""
This is a test email to send an attachement (body).
"""
# Define the main headers.
part1 = """From: Sarika Jadhav <sarika.jadhav@kokilabenhospitals.com>
To: To Person <ahmed.qureshi@kokilabenhospitals.com>
Subject: OPD Data via API
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary=%s
--%s
""" % (marker, marker)

# Define the message action
part2 = """Content-Type: text/plain
Content-Transfer-Encoding:8bit

%s
--%s
""" % (body,marker)

# Define the attachment section
part3 = """Content-Type: multipart/mixed; name=\"%s\"
Content-Transfer-Encoding:base64
Content-Disposition: attachment; filename=%s

--%s--
""" %(filename, filename,  marker)
message = part1 + part2 + part3

try:
   smtpObj = smtplib.SMTP('172.20.200.29',25)
   smtpObj.sendmail(sender, receivers, message)
   print("Successfully sent email")
except Exception:
   print("Error: unable to send email")




# message = """From: Sarika Jadhav <sarika.jadhav@kokilabenhospitals.com>
# To: To Person <ahmed.qureshi@kokilabenhospitals.com>
# Subject: OPD Data via API

# This is a test e-mail message.
# """