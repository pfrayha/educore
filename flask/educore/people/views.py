from flask import flash, redirect, render_template, url_for, request
from flask_login import login_required, login_user, logout_user, current_user
from . import people
from ..manager_hub import ManagerHub

@people.route('/people/new_<string:model>', methods=['GET', 'POST'])
@login_required
def new_person(model):
	if request.method == 'GET':
		return ManagerHub.get_hub_instance().people_manager.get_registration_form(model)
	else:
		return ManagerHub.get_hub_instance().people_manager.submit_registration_form(model)

@people.route('/people/edit_<string:model>/<int:id>', methods=['GET','POST'])
@login_required
def edit_person(model, id):
	if request.method == 'GET':
		return ManagerHub.get_hub_instance().people_manager.get_registration_form(model, id)
	else:
		return ManagerHub.get_hub_instance().people_manager.submit_registration_form(model, id)

@people.route('/people/list_<string:model>', methods=['GET'])
@login_required
def list_people(model):
	filters = request.args
	return ManagerHub.get_hub_instance().people_manager.list_people(model, **filters)

@people.route('/people/delete_<string:model>/<int:id>', methods=['GET'])
@login_required
def delete_person(model, id):
	return ManagerHub.get_hub_instance().people_manager.delete_person(model, id)