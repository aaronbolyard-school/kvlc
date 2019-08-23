from flask import (
	Blueprint, flash, g, redirect, render_template,
	request, session, url_for
)

import kvlc.model.calculator as calculator

bp = Blueprint('home', __name__, url_prefix='/')

ACTIONS = {
	'add': calculator.add,
	'sub': calculator.sub,
	'mul': calculator.mul,
	'div': calculator.div
}

@bp.route('/', methods=('POST', 'GET'))
def index():
	errors = []
	result = ""

	if request.method == 'POST':
		leftHandSide = request.form.get('lhs', False)
		rightHandSide = request.form.get('rhs', False)

		if not leftHandSide:
			errors.append('Left hand side not provided.')
		else:
			try:
				leftHandSide = int(leftHandSide)
			except ValueError:
				errors.append('Left hand side is not valid integer.')
				leftHandSide = False

		if not rightHandSide:
			errors.append('Right hand side not provided.')
		else:
			try:
				rightHandSide = int(rightHandSide)
			except ValueError:
				errors.append('Right hand side is not valid integer.')
				rightHandSide = False

		if (leftHandSide or leftHandSide == 0) and (rightHandSide or rightHandSide == 0):
			action = ACTIONS.get(request.form.get('action', ''))
			if not action:
				errors.append('Action not valid.')
			else:
				actionResult = action(leftHandSide, rightHandSide)

				if not actionResult and actionResult != 0:
					errors.append('Input bad. Did you try and divide by zero?')
				else:
					result = str(actionResult)

	return render_template("index.html", errors=errors, result=result)