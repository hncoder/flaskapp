from . import db

# class Role(db.Model):
# 	"""docstring for Role"""
# 	__tablename__ = 'roles'
# 	id = db.Column(db.Integer, primary_key=True)
# 	name = db.Column(db.String(64), unique=True)
# 	users = db.relationship('User', backref='role', lazy='dynamic')

# 	def __repr__(self):
# 		return '<Role %r>' % self.name


# class User(db.Model):
# 	"""docstring for User"""
# 	__tablename__ = 'users'
# 	id = db.Column(db.Integer, primary_key=True)
# 	email = db.Column(db.String(64), unique=True, index=True)
# 	username = db.Column(db.String(64), unique=True, index=True)
# 	sex = db.Column(db.Integer, default=0)
# 	role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
# 	password_hash = db.Column(db.String(128))
# 	confirmed = db.Column(db.Boolean, default=False)

# 	def __repr__(self):
# 		return '<User %r>' % self.username
		
