import re

from utils.exception import MobileNumberLengthException, MobileNumberFormatException, EmailFormatException, \
    UserNameAlreadyTakenException, AccountAlreadyExist, UserNameLengthException

EMAIL_REGEX = '\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?'
MOBILE_REGEX = '^[6-9]\d{9}$'


class Parser(object):

    @staticmethod
    def parse_email(mail, mail_list):
        is_valid = re.search(pattern=EMAIL_REGEX, string=mail)
        if not is_valid:
            raise EmailFormatException("Invalid Email id Format")
        if mail in mail_list:
            raise AccountAlreadyExist("Account Already exist")
        return True

    @staticmethod
    def parse_mobile_number(mobile_number):
        if len(mobile_number) != 10:
            raise MobileNumberLengthException("Invalid Mobile Number Length")

        is_valid = re.search(pattern=MOBILE_REGEX, string=mobile_number)
        if not is_valid:
            raise MobileNumberFormatException("Invalid Mobile Number Format")

        return True

    @staticmethod
    def parse_unique_user_name(user, user_list):
        if user in user_list:
            raise UserNameAlreadyTakenException("Username already taken")
        if len(user) < 8:
            raise UserNameLengthException("Username to be greater than 8 characters")
        return True

