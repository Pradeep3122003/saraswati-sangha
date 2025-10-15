from flask import Blueprint, request, jsonify, make_response
import json, uuid, random
from utils.validators import valid_mobile
from models import Member, Login
from extension import db
from utils.password import hash_password, verify_password
from flask_jwt_extended import create_access_token, set_access_cookies, jwt_required, get_jwt_identity

auth_bp=Blueprint('auth',__name__,url_prefix="/api/v1")


@auth_bp.route("/login",methods=["POST"])
def login():
    try:
     data = request.json
    except:
     return jsonify({"success":False,"message":"missing parameter"}), 400
    mobile = data.get("mobile")
    password = data.get("password").strip()

    if not mobile or not password:
        return jsonify({"success":False,"message":"missing parameter"}), 400

    if not valid_mobile(mobile):
        return jsonify({"success":False,"message":"invalid mobile number"}), 400

    account = Login.query.filter_by(mobile=mobile).first()
    if not account:
        return jsonify({"success":False,"message":"invalid credentials"}), 400

    if not verify_password(password, account.password.encode('utf-8')):
        return jsonify({"success":False,"message":"invalid credentials"}), 400

    profile = Member.query.filter_by(mid=account.mid).first()
    if not profile:
     return jsonify({"success":False,"message": "something went wrong"}), 400

    data=json.dumps({"userid":profile.mid, "role":profile.role})
    access_token = create_access_token(data)
    response = make_response(jsonify({"success":True,"message": "Login successful"}), 200)

    set_access_cookies(response, access_token)
    return response


@auth_bp.route("/status",methods=["GET"])
@jwt_required()
def status():
  data=get_jwt_identity()
  data=json.loads(data)
  user=Member.query.get(data["userid"])
  if not user:
    return jsonify({"success":False,"message": "unauthorized access"}), 400

  return jsonify({"success":True,"role":data["role"], "message":"user logged in"}), 200
