from flask import Flask, render_template
from clbrcalc_toolbox import *

application = Flask(__name__)

@application.route("/", methods=["GET","POST"])
def index():
    form_data = read_form()
    weight = form_data["weight"]
    height = form_data["height"]
    age_minmax = age_limits()
    bmi = calculated_form_data(form_data)["bmi"]
    age = calculated_form_data(form_data)["age_years"]
    months = int(read_form()["num_months"])
    adjust_age = age + (months/3)*0.25
    bmi_validation = validate_bmi(calculated_form_data(form_data)["bmi"])
    if (bmi_validation == False or adjust_age > 43):
        if(bmi_validation == False):
            e_bmi = True
        else:
            e_bmi = False
        if(adjust_age >43):
            e_months = True
        else:
            e_months = False
        return render_template("calculator.html", form_data = form_data, age=age, bmi=bmi,
        age_limits=age_minmax,e_bmi=e_bmi,error=True,e_months=e_months,adjust_age=adjust_age)
    clbr = get_CLBR(age,bmi)
    clbr_months = get_CLBR_condition(age,bmi,months)
    loose1 = calc_target_BMI(weight,height,1)
    loose2 = calc_target_BMI(weight,height,2)
    loose3 = calc_target_BMI(weight,height,3)
    loose4 = calc_target_BMI(weight,height,4)
    output_graph(age,bmi)
    return render_template("calculator.html", form_data = form_data,
    age_limits=age_minmax, age=age, bmi=bmi, clbr=clbr, clbr_months=clbr_months,
    loose1=loose1,loose2=loose2,loose3=loose3,loose4=loose4)



if __name__ == "__main__":
    application.run(debug = False)
