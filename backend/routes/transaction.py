from flask import Blueprint, request, jsonify
import json, uuid, random
from utils.validators import valid_mobile
from models import Member, Transaction
from extension import db
from utils.password import hash_password, verify_password
from flask_jwt_extended import create_access_token, set_access_cookies, jwt_required, get_jwt_identity

tra_bp=Blueprint('tra',__name__,url_prefix="/api/v1")

@tra_bp.route("/transactions",methods=["GET"])
@jwt_required()
def transactions():
 data=get_jwt_identity()
 data=json.loads(data)

 userid=data["userid"]

 if not userid or len(userid) != 32:
  return jsonify({"success":False,"message":"unauthorized access"}), 400

 profile=Member.query.get(userid)
 if not profile:
  return jsonify({"success":False,"message":"unauthorized access"}), 400

 tras=Transaction.query.filter_by(mid=userid).all()
 if not tras:
  return jsonify({"success":True,"message":"no transaction history"}), 200

 tra=[]
 for all in tras:
  entry={"tid":all.tid,"date":str(all.date), "details": all.amount}
  tra.append(entry)
 return jsonify({"success":True,"message":"loan info", "transactions":tra}), 200
