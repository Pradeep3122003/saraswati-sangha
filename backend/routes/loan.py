from flask import Blueprint, request, jsonify
import json, uuid, random
from utils.validators import valid_mobile
from models import Member, Org, Loan
from extension import db
from utils.password import hash_password, verify_password
from flask_jwt_extended import create_access_token, set_access_cookies, jwt_required, get_jwt_identity

loan_bp=Blueprint('loan',__name__,url_prefix="/api/v1")

@loan_bp.route("/loans/all",methods=["GET"])
@jwt_required()
def loans():
 data=get_jwt_identity()
 data=json.loads(data)

 userid=data["userid"]

 if not userid or len(userid) != 32:
  return jsonify({"success":False,"message":"unauthorized access"}), 400

 profile=Member.query.get(userid)
 if not profile:
  return jsonify({"success":False,"message":"unauthorized access"}), 400

 loans=Loan.query.filter_by(mid=userid).all()
 if not loans:
  return jsonify({"success":True,"message":"no loan history"}), 200

 loan=[]
 for all in loans:
  entry={"lid":all.lid,"amount":all.amount,"balance":all.balance,"loan_date":str(all.loan_date),"principal":all.principal,"interest":all.interest,"clear_date":str(all.clear_date)}
  loan.append(entry)
 return jsonify({"success":True,"message":"loan info", "loans":loan}), 200
