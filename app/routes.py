from flask import Blueprint, jsonify
from cv import personal_info, experience, education

api = Blueprint('api', __name__)


@api.route('/personal', methods=['GET'])
def get_personal():
    return personal_info


@api.route('/experience', methods=['GET'])
def get_experience():
    return experience


@api.route('/education', methods=['GET'])
def get_education():
    return education

