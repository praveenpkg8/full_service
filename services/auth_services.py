import uuid

from flask import session, request
from models.auth_datastore import User, Session


class AuthServices(object):

    @staticmethod
    def new_user(request_data):
        message = User.create_user(
            name=request_data.get('name'),
            mail=request_data.get('mail'),
            password=request_data.get('password'),
        )
        return message

    @staticmethod
    def fetch_user_by_mail(mail):
        user = User.user_by_mail(mail)
        return user

    @staticmethod
    def google_oauth_new_user(user_info):

        password = uuid.uuid4().hex
        user = User.user_by_mail(user_info.get('email'))

        if user is None:
            message = User.create_user(
                name=user_info.get('name'),
                mail=user_info.get('email'),
                password=password,
            )
            return message

    @staticmethod
    def google_oauth_authenticate_user(user, token_id):

        if user:

            session_id = str(uuid.uuid4())
            ses = Session(
                session_id=session_id,
                mail=user.get('email'),
                name=user.get('name'),
                token_id=token_id
            )
            Session.create_session(ses)

            return session_id

        return user

    @staticmethod
    def authenticate_user(user):

        if user:

            session_id = str(uuid.uuid4())
            ses = Session(
                session_id=session_id,
                mail=user.get('mail'),
                name=user.get('name')
            )
            Session.create_session(ses)

            return session_id

        return user

    @staticmethod
    def get_user_logged_out():

        if "session" in request.cookies:

            session_key = Session.get_session(request.cookies.get('session'))
            Session.delete_session(session_key)
            return "User logged out"


def get_name():

    name = session['id']
    return name
