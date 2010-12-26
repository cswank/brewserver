from zope.password.password import SSHAPasswordManager

class AuthenticatorPlugin(object):

    def get_pw(self, identity):
        try:
            pw = identity['password']
        except KeyError:
            return
        return pw

    def get_login(self, identity):
        try:
            login = identity['repoze.who.plugins.auth_tkt.userid']
            return login
        except KeyError:
            pass
        try:
            login = identity['login']
        except KeyError:
            return
        return login

class MongoAuthenticatorPlugin(AuthenticatorPlugin):

    def __init__(self, db_name, db_users='users'):
        self.db_name = db_name
        self.db_users = db_users

    def authenticate(self, environ, identity):
        login = self.get_login(identity)
        password = self.get_pw(identity)
        if login is None or password is None:
            return
        users = self.users
        doc = users.find_one({'username': login})
        if doc is None:
            return
        manager = SSHAPasswordManager()
        hashed = doc.get('password')
        result = manager.checkPassword(str(hashed), str(password))
        if result:
            return login
        return None

    @property
    def users(self):
        db = self.db
        return db[self.db_users]

    @property
    def db(self):
        from pymongo.connection import Connection
        c = Connection()
        return c[self.db_name]

