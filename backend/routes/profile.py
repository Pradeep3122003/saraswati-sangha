from flask import Blueprint, request, jsonify
import json, uuid, random
from utils.validators import valid_mobile
from models import Member, Org
from extension import db
from utils.password import hash_password, verify_password
from flask_jwt_extended import create_access_token, set_access_cookies, jwt_required, get_jwt_identity

profile_bp=Blueprint('profile',__name__,url_prefix="/api/v1")

@profile_bp.route("/profile",methods=["GET"])
@jwt_required()
def profile():
 data=get_jwt_identity()
 data=json.loads(data)

 userid=data["userid"]

 if not userid or len(userid) != 32:
  return jsonify({"success":False,"message":"unauthorized access"}), 400

 profile=Member.query.get(userid)
 if not profile:
  return jsonify({"success":False,"message":"unauthorized access"}), 400

 return jsonify({"success":True,"message":"profile info", "name":profile.name, "mobile":profile.mobile, "age": profile.age, "deposit":profile.deposit, "joining":profile.joining, "exit":profile.exit, "role": profile.role}), 200
