class Account:
    def __init__(self, id, username, password, role_id,status,is_active):
        self._id = id
        self._username = username
        self._password = password
        self._roleId = role_id
        self._status = status
        self._isActive = is_active


    def get_id(self):
        return self.get_id
    def set_id(self, id):
        self._id = id

    def get_username(self):
        return self.get_username
    def set_username(self, username):
        self._username = username

    def get_password(self):
        return self.get_password
    def set_password(self, password):
        self._password = password

    def get_roleId(self):
        return self.get_roleId
    def set_roleId(self, roleId):
        self._roleId = roleId

    def get_status(self):
        return self.get_status
    def set_status(self, status):
        self._status = status

    def get_isActive(self):
        return self.get_isActive
    def set_isActive(self, isActive):
        self._isActive = isActive
