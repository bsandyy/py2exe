'''
The purpose of this script is to say HI to the name given in conf file

'''

import configparser


parser = configparser.ConfigParser()
parser.read("conf.ini")
# print(parser.get('auth','email_account'))

user = parser.get('user', 'name')


def say_hi():
    print("Hi {}".format(user))


if __name__ == '__main__':
    say_hi()
