from flask import Blueprint, render_template, jsonify
from app.models import User, Computer
from app import db
from flask import request

bp = Blueprint('comput', __name__)


@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/get/computers')
def get_computers():
    computers = Computer.query.all()
    com_list = []
    for c in computers:
        com_list.append(c.to_dict())
    return jsonify(com_list)


@bp.route('/get/computer')
def get_computer():
    pass


@bp.route('/get/users')
def get_users():
    us = User.query.all()
    u_list = []
    for u in us:
        u_list.append(u.to_dict())
    return jsonify(u_list)


@bp.route('/get/user')
def get_user():
    pass


@bp.route('/get/query')
def query():
    if request.args.get('u_id'):
        u_id = request.args.get('u_id')
        if u_id.isdigit():
            u = User.query.get(int(request.args.get('u_id')))
            if u.computers:
                ul = []
                for i in u.computers:
                    ul.append(i.to_dict())
                return jsonify(ul)
            else:
                return '您查找的用户不存在'
        else:
            return "您查找的用户不存在"
    if request.args.get('code'):
        code = request.args.get('code')
        if code:
            c = Computer.query.filter_by(code=code).first()
            if c:
                return jsonify(c.to_dict())
            else:
                return '您查找的计算机不存在'
        else:
            return "没有您要查找的计算机"
