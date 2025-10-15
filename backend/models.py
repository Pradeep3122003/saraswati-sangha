from extension import db
from sqlalchemy.dialects.postgresql import JSONB
from datetime import datetime
class Org(db.Model):
  __tablename__='org'
  gid=db.Column(db.String(32), primary_key=True)
  year=db.Column(db.Date)
  members=db.Column(db.Integer)
  turnover=db.Column(db.Integer)
  profit=db.Column(db.Integer)
  meeting=db.Column(db.Date)
  loanq=db.Column(db.String(32))
  def __repr__(self):
        return f'<Org {self.gid}>'


class Member(db.Model):
  __tablename__='member'
  gid=db.Column(db.String(32))
  mid=db.Column(db.String(32), primary_key=True)
  role=db.Column(db.String(10))
  name=db.Column(db.String(60))
  mobile=db.Column(db.String(10))
  age=db.Column(db.Integer)
  joining=db.Column(db.Date)
  exit=db.Column(db.Date)
  deposit=db.Column(db.Integer)
  def __repr__(self):
        return f'<Member {self.mid}>'


class Loan(db.Model):
  __tablename__='loan'
  mid=db.Column(db.String(32))
  lid=db.Column(db.String(40), primary_key=True)
  amount=db.Column(db.Integer)
  balance=db.Column(db.Integer)
  loan_date=db.Column(db.Date)
  principal=db.Column(db.Integer)
  interest=db.Column(db.Integer)
  clear_date=db.Column(db.Date)
  def __repr__(self):
        return f'<Loan {self.lid}>'

class Transaction(db.Model):
  __tablename__='transaction'
  mid=db.Column(db.String(32))
  tid=db.Column(db.String(64), primary_key=True)
  date=db.Column(db.Date)
  amount=db.Column(JSONB)
  def __repr__(self):
        return f'<Loan {self.lid}>'

class Login(db.Model):
  __tablename__='login'
  no=db.Column(db.Integer, primary_key=True)
  mid=db.Column(db.String(32))
  mobile=db.Column(db.String(10))
  password=db.Column(db.String(200))
  def __repr__(self):
        return f'<Loan {self.lid}>'
