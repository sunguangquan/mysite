from app import create_app, db
from app.models import Astype, Status

app = create_app()
app.app_context().push()


def test_asstype():
    a_type1 = Astype(astype="品牌台式机")
    # a_type2 = Astype(astype="笔记本")
    # a_type3 = Astype(astype="工作站")
    conn = db.session()
    conn.add_all([a_type1])
    conn.commit()
    # assert a_type2.id == 2
    # assert a_type1.id == 1
    # assert a_type3.id == 3
    # assert a_type1.astype == "组装机"
    # assert a_type2.astype == "笔记本"
    # assert a_type3.astype == "工作站"


# def test_assstatus():
#     status1 = Status(status="使用中")
#     status2 = Status(status="待分配")
#     status3 = Status(status="报废")
#     conn = db.session()
#     conn.add_all([status1, status2, status3])
#     conn.commit()
#     assert status1.id == 1
#     assert status2.id == 2
#     assert status3.id == 3
#
#     assert status1.status == "使用中"
#     assert status2.status == "待分配"
#     assert status3.status == "报废"
