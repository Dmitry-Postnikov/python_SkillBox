import re

list_english_words = ['aden', 'diem', 'post', 'lodz']


def is_strong_password(password: str):
    password = password.lower()
    result = re.findall("\D{4,}", password)
    for word in result:
        if word in list_english_words:
            return False
    return True


if __name__ == "__main__":
    print(is_strong_password("4die22m40p7ost"))
