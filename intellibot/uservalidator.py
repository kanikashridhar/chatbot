import datetime,re
from intellibot.models import UserInfo

def validateUserResponse(text, context):
    validator = {
        'NAME' : validate_name,
        'GENDER' : validate_gender,
        'DOB' : validate_DOB,
        'SMOKER': validate_smoker
        }
    return validator.get(context.upper())(text)

def validate_name(text):
    return True 

def validate_gender(text):
    if 'MALE' in text.upper() or 'FEMALE' in text.upper():
       return True
    return False

def validate_smoker(text):
    if 'YES' in text.upper() or 'NO' in text.upper():
       return True
    return False

def validate_DOB(text):
    date_format = '%d-%m-%Y'
    date_string = ""
    try:
        date_capture = (re.search('\d{2}-\d{2}-\d{4}',text))
        date_string  = date_capture.group(0)
        date_obj = datetime.datetime.strptime(date_string, date_format)
        print(date_obj)
        return True
    except Exception:
        return False 