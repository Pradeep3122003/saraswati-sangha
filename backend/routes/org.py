from flask import Blueprint, request, jsonify, make_response
import json, uuid, random
from utils.validators import valid_mobile
from models import Member, Login
from extension import db
from utils.password import hash_password, verify_password
from flask_jwt_extended import create_access_token, set_access_cookies, jwt_required, get_jwt_identity

org_bp=Blueprint('org',__name__,url_prefix="/api/v1")
