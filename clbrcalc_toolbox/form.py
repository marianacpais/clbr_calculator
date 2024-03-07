"""Functions to read forms
"""

from flask import request
from datetime import datetime

from .calc import calc_BMI, round_to_quarters, years_from, years_ago

def read_form():
    weight = request.form.get("weight",50,int)
    height = request.form.get("height",150,int)
    defaultDate = age_limits()["date_default"]
    dateOfBirth_req = request.form.get("dateOfBirth",defaultDate)
    dateOfBirth = datetime.strptime(dateOfBirth_req, '%Y-%m-%d').date()
    num_months = request.form.get("num_months",3)
    return {"weight":weight, "height": height,"dateOfBirth":dateOfBirth,"defaultDate":defaultDate,"num_months":num_months}

def calculated_form_data(form_data):
    bmi = round(calc_BMI(form_data["weight"],form_data["height"]))
    age_years = round_to_quarters(years_from(form_data["dateOfBirth"]))
    return {"bmi": bmi, "age_years": age_years}

def validate_bmi(bmi):
    # 18 a 35
    if (bmi < 18 or bmi > 35):
        return False
    else:
        return True

def age_limits():
    # 30.00 a 43.00
    date_min = years_ago(43.24)
    date_max = years_ago(30.25)
    date_default = years_ago(35)
    return {"date_min": date_min, "date_max":date_max, "date_default":date_default}
