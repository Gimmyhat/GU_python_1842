import re


def email_parse(str):
    pattern = re.compile(r"^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$")
    if pattern.search(str):
        sep = str.index('@')
        username = str[:sep]
        domain = str[sep+1:]
        return {'username': username, 'domain': domain}
    else:
        raise ValueError(f'wrong email: {str}')


if __name__ == '__main__':
    print(email_parse('gimmy.hat@gmail.com'))
