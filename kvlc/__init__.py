import os

from flask import Flask

from flask_bootstrap import Bootstrap

def create_app(test_config=None):
	app = Flask(__name__, instance_relative_config=True)
	
	Bootstrap(app)

	import kvlc.views.index
	app.register_blueprint(kvlc.views.index.bp)

	return app
