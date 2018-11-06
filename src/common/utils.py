from passlib.hash import pbkdf2_sha512

__author__ = 'Abiodun'


class Utils(object):

    @staticmethod
    def hash_password(password):
        """
        Hashes a password using pbkdf2_sha512
        :param password: The sha512 password from the user registration page
        :return: sh512=>pbkdf2_sha512 encrypted password
        """
        return pbkdf2_sha512.encrypt(password)

    @staticmethod
    def check_hashed_password(password, hashed_password):
        """
        Checks the password sent matches the one in the database
        the database password is encrypted at this point
        :param password: sha512- hashed password
        :param hashed_password: pbkdf2_sha512 encrypted password
        :return: Trus if password matches, False otherwise
        """

        return pbkdf2_sha512.verify(password, hashed_password)
