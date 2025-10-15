from flask import Blueprint, request, jsonify
import json, uuid, random
from utils.validators import valid_mobile
from models import Member, Org
from extension import db
from utils.password import hash_password, verify_password
from flask_jwt_extended import create_access_token, set_access_cookies, jwt_required, get_jwt_identity

org_bp=Blueprint('org',__name__,url_prefix="/api/v1")

@org_bp.route("/group",methods=["GET"])
@jwt_required()
def group():
 data=get_jwt_identity
 data=json.loads(data)

 userid=data["mid"]

 if not userid or len(userid) != 32:
  return jsonify({"success":False,"message":"unauthorized access"}), 400

 profile=Member.query.get(userid)
 if not profile:
  return jsonify({"success":False,"message":"unauthorized access"}), 400

 group=Org.query.get(profile.gid)
 if not group:
  return jsonify({"success":False,"message":"something went wrong"}), 503

 return jsonify({"success":True,"message":"group info", "year":group.year, "members":group.members, "turnover": group.turnover, "profit":group.profit, "loanq":group.loanq, "meeting":group.meeting}), 200
