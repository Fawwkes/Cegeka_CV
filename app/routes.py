from flask import Blueprint, jsonify
from cv import personal_info, experience, education

api = Blueprint('api', __name__)


@api.route('/personal', methods=['GET'])
def get_personal():
    if personal_info:
        return personal_info
    else:
        return jsonify({"error": "Personal information not available"}), 404


@api.route('/experience', methods=['GET'])
def get_experience():
    if experience:
        return experience
    else:
        return jsonify({"error": "Experience not available"}), 404


@api.route('/education', methods=['GET'])
def get_education():
    if education:
        return education
    else:
        return jsonify({"error": "Education not available"}), 404
