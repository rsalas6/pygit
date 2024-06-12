class PygitException(Exception):
    """Base exception for pygit"""
    pass

class InitException(PygitException):
    """Exception raised during repository initialization"""
    pass
