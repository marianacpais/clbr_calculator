import pandas as pd

ds =  pd.read_csv("static/data/table.csv", sep=";")

def get_CLBR(age,BMI):
    """Reads table to get estimated CLBR.

    Args:
        Age (float): age in years rounded to quarter fraction (floor)
        BMI (int): BMI

    Returns:
        str: estimated CLBR for given Age and BMI
    """
    result = ds[(ds["Idade"]==age) & (ds["IMC"]==BMI)]
    result = result["CLBR"].iloc[0]
    return result

def get_CLBR_condition(age,bmi,months):
    """Reads table to get estimated CLBR after certain number of months.

    Args:
        Age (float): age in years rounded to quarter fraction (floor)
        BMI (int): BMI
        months (int): number of months after

    Returns:
        str: estimated CLBR for given Age and BMI
    """

    error_message = "Not Applicable: BMI would be < 18"
    if months != 0:
        months3 = months/3
    else:
        months3 = 0
    age = age + months3*0.25
    # Keep Weight
    keep_w = ds[(ds["Idade"]==age) & (ds["IMC"]==bmi)]
    keep_w = keep_w["CLBR"].iloc[0]
    # Loose 1 unit bmi
    bmi = bmi-1
    if bmi < 18:
        loose1 = error_message
    else:
        loose1 = ds[(ds["Idade"]==age) & (ds["IMC"]==bmi)]
        loose1 = loose1["CLBR"].iloc[0]
    # Loose 2 units bmi
    bmi = bmi-1
    if bmi < 18:
        loose2 = error_message
    else:
        loose2 = ds[(ds["Idade"]==age) & (ds["IMC"]==bmi)]
        loose2 = loose2["CLBR"].iloc[0]
    # Loose 3 units bmi
    bmi = bmi-1
    if bmi < 18:
        loose3 = error_message
    else:
        loose3 = ds[(ds["Idade"]==age) & (ds["IMC"]==bmi)]
        loose3 = loose3["CLBR"].iloc[0]
    # Loose 4 units bmi
    bmi = bmi-1
    if bmi < 18:
        loose4 = error_message
    else:
        loose4 = ds[(ds["Idade"]==age) & (ds["IMC"]==bmi)]
        loose4 = loose4["CLBR"].iloc[0]
    return {"keep_w":keep_w, "loose1":loose1, "loose2":loose2, "loose3":loose3, "loose4":loose4}
