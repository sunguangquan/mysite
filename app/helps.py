from app.models import User, Computer


def userInDatabase(user):
    if User.query.filter_by(name=user.name):
        return True
    else:
        return False


def computerInDatabase(computer):
    if Computer.query.filter_by(code=computer.code):
        return True
    else:
        return False
