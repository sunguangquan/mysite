from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app import db
from flask_admin.contrib.sqla import ModelView
from app import admin


class User(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(25), unique=True)
    dep = Column(String(25))
    computers = relationship('Computer', backref='user')

    def __repr__(self):
        return "姓名: {}  部门: {}".format(self.name, self.dep)

    def to_dict(self):
        comput = []
        for com in self.computers:
            comput.append({"code": com.code, "cpu": com.cpu, "ram": com.ram})
        return {
            "id": self.id,
            "name": self.name,
            "dep": self.dep,
            "computers": comput
        }


class Computer(db.Model):
    id = Column(Integer, primary_key=True)
    code = Column(String(50), unique=True, index=True)
    cpu = Column(String(125))
    ram = Column(Integer)
    ram_sp = Column(Integer)
    gpu = Column(String(100))
    disk = Column(String(125))
    monitor = Column(String(50))
    user_id = Column(Integer, ForeignKey('user.id'))
    # ass_type = Column(Integer, ForeignKey("asstype.id"))
    # ass_status = Column(Integer, ForeignKey("assstatus.id"))

    def to_dict(self):
        return {
            "id": self.id,
            "code": self.code,
            "cpu": self.cpu,
            "ram": self.ram,
            "ram_sp": self.ram_sp,
            "gpu": self.gpu,
            "disk": self.disk,
            "monitor": self.monitor,
            "user": self.user.name
        }


# class Asstype(db.Model):
#     id = Column(Integer, primary_key=True)
#     astype = Column(String(20))
#
#
# class Assstatus(db.Model):
#     id = Column(Integer, primary_key=True)
#     assstatus = Column(String(20))


admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Computer, db.session))
