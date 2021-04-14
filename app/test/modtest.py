from app import create_app, db
from app.models import User, Computer
import unittest


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


class TestUserCase(unittest.TestCase):

    def setUp(self):
        app = create_app()
        app.app_context().push()
        conn = db.session()
        u1 = User(name="李靖", dep="技术支持")
        u2 = User(name="孙广全", dep="技术支持")
        if not userInDatabase(u1):
            conn.add(u1)
        if not userInDatabase(u2):
            conn.add(u2)
        conn.commit()

    def test_user(self):
        u1 = User.query.filter_by(name="李靖").first()
        self.assertEqual("李靖", u1.name)
        self.assertEqual("技术支持", u1.dep)
        u2 = User.query.filter_by(name="孙广全").first()
        self.assertEqual("孙广全", u2.name)
        self.assertEqual("技术支持", u2.dep)


class TestComputerCase(unittest.TestCase):
    def setUp(self) -> None:
        app = create_app()
        app.app_context().push()
        db.create_all()
        conn = db.session()
        c1 = Computer(code="h1", cpu="I7", ram=8, ram_sp=1600, monitor="21 apple",
                      user_id=User.query.filter_by(name="孙广全").first().id)
        c2 = Computer(code="h2", cpu="I9", ram=32, ram_sp=3200, monitor="16 apple",
                      user_id=User.query.filter_by(name="李靖").first().id)
        if not computerInDatabase(c1):
            conn.add(c1)
        if not computerInDatabase(c2):
            conn.add(c2)
        conn.commit()

    def test_computer(self):
        c1 = Computer.query.filter_by(code='h1').first()
        self.assertEqual("I7", c1.cpu)

    def test_user(self):
        c1 = Computer.query.filter_by(code='h1').first()
        self.assertEqual(1, c1.id)


if __name__ == '__main__':
    unittest.main()
