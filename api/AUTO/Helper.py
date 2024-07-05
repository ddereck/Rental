import re
from cryptography.fernet import Fernet
import json
from django.core.files.storage import FileSystemStorage
import os
from datetime import datetime

def isEmailOrPhone(chaine):
    """
    Check if the string is an email or a phone number.
    1 - If it is an email, it returns "C'est une adresse e-mail."
    2 - If it is a phone number, it returns "C'est un numéro de téléphone."
    0 - If it is neither, it returns "Ce n'est ni une adresse e-mail ni un numéro de téléphone
    """
    pattern_email = r'^[\w\.-]+@[\w\.-]+$'
    pattern_telephone = r'^[0-9]{10}$'

    if re.match(pattern_email, chaine):
        return 1

    elif re.match(pattern_telephone, chaine):
        return 2

    else:
        return 0

# def generateUniqueCode(length=4):
#     characters = string.digits
#     while True:
#         random_number = ''.join(random.choice(characters) for _ in range(length))
#         if not Users.objects.filter(code_otp=random_number).exists():
#             return random_number



def serialize(data):
    """ 
        Serialize data to JSON
        :param data: data to serialize
        :return: JSON representation of data

        Ex:

        serialize([
            {'id': 1, 'name': 'John'},
            {'id': 2, 'name': 'Jane'}
        ])
        => [{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]
    """
    return json.dumps(data)

def deSerialize(data):
    """
    Deserialize JSON data
    :param data: JSON data to deserialize
    :return: Python representation of data

    Ex:

    deSerialize('[{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]')

    => [
        {'id': 1, 'name': 'John'},
        {'id': 2, 'name': 'Jane'}
    ]
    """
    return json.loads(data)


def formatUserPictureUrl(request, file, isText=False):
    """
    Format the file url
    """
    if file:
        file = request.build_absolute_uri('/') + file.name if not isText else request.build_absolute_uri('/') + file
    else:
        file = None
    
    return file

def saveOrRemoveFile(image_file, old_file=None, location='medias/', isText=False):
    if image_file:
        if old_file:
            if os.path.isfile(old_file.path if not isText else old_file):
                os.remove(old_file.path if not isText else old_file)

        now = datetime.now()
        formatted_datetime = now.strftime("%d%m%Y%H%M%S")
        fs = FileSystemStorage(location=location)
        image_filename = fs.save(formatted_datetime + image_file.name, image_file)
        image_path = location + fs.url(image_filename)
        return image_path
    else: 
        return None
    
def removeFile(old_file):
    if old_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)