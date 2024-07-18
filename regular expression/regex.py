# task       
import re
para= """  i am jai kishore currntly pursuing a skill set in ocean academy my email id is jai123@gmail.com my phone number
            is 9012345123 and i am in puducherry my pincode is 606061 """

email_id= r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'
email_pattern=re.findall(email_id, para)
print("valid email:", email_id)

phone=r'^\+?[1-9]\d{1,14}$'
phone_pattern=re.findall(phone,para)
print("valid number:",phone)

pincode= r'^(?:\d{5}(?:\-\d{4})?|\D[A-Z]{1,2}\d[A-Z\d]? ?\d[A-Z]{2})$'

pincode_pattern=re.findall(pincode,para )
print("valid pincode:",pincode)





