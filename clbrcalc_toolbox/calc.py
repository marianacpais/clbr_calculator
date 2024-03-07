from datetime import date, timedelta
from math import floor

def calc_BMI (weight_kg,height_cm):
    """Calculates the BMI given weight and height and rounds to the nearest unit

    Args:
        weight_kg (float): the weight of the individual in Kg
        height_m (float): the height of the individual in centimeters
    """
    bmi = round(weight_kg/(height_cm/100)**2)
    return(bmi)

def calc_target_BMI (weight_kg,height_cm,units):
    """Calculates target weight for loss of a certain number of units of bmi

    Args:
        weight_kg (float): the weight of the individual in Kg
        height_m (float): the height of the individual in centimeters
    """
    bmi = round(weight_kg/(height_cm/100)**2)
    bmi = bmi - units
    l_w_max = (bmi+.49) * (height_cm/100)**2
    loss_w_max = weight_kg - l_w_max
    l_w_min = (bmi-.5) * (height_cm/100)**2
    loss_w_min = weight_kg - l_w_min
    return({"w_max":round(l_w_max,1),
            "w_min":round(l_w_min,1),
            "loss_2max":round(loss_w_max,1),
            "loss_2min":round(loss_w_min,1)})

def years_from (date):
    """Calculate the APROXIMATE number of years from a given date
    """
    today = date.today()
    delta = today - date
    days = delta.days
    years = days/365.2425
    return years

def years_ago (num_years):
    """Calculate the date a given number of years ago 
    in the desired format to include in the bounds of the form"""

    days = num_years * 365.2425
    delta = timedelta(days = days)
    today = date.today()
    req_date = today - delta
    return req_date.strftime('%Y-%m-%d')


def round_to_quarters(num):
    """Rounds to fraction - quarters (x.00, x.25, x.50 ou x.75)"""
    num = num*4
    num = floor(num)
    num = num/4
    return num