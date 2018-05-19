from random import Random
from hashlib import md5

class PasswordEcrypter(object):
    def __init__(self):
        self.__salt = None

    def create_salt(self, length=4):
        salt = ''
        chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
        len_chars = len(chars) - 1
        random = Random()
        for i in range(length):
            # 每次从chars中随机取一位
            salt += chars[random.randint(0, len_chars)]
        return salt


    def create_md5(self, pwd, salt):
        md5_obj = md5()
        md5_obj.update((pwd + salt).encode('utf8'))
        return md5_obj.hexdigest()
