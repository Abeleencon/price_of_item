import uuid

from src.common.database import Database
from src.common.utils import Utils
import src.models.users.errors as UserErrors

__author__ = 'Abiodun'


class User(object):
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return "<User {}>".format(self.email)

    @staticmethod
    def is_login_valid(email, password):
        """
        This method checks if the email and password provided is valid and exists
        and checks if the email matches the password
        :param email: The user email
        :param password: The sha512 password
        :return: True if valid, false if not
        """

        user_data = Database.find_one("users", {"email": email})

        if user_data is None:
            # Tell user the email doesnt exist
            raise UserErrors.UserNotExistError("This user does not exist")

        if not Utils.check_hashed_password(password, user_data['password']):
            # tell the user password is wrong
            raise UserErrors.IncorrectPasswordError("Password Incorrect")
        return True

