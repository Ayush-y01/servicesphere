from enum import Enum

class UserRole(str, Enum):
    ADMIN = "admin"
    PROVIDER = "provider"
    USER = "user"