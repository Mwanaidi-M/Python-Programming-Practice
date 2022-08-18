def bmi(weight, height):
    """
    Function that calculates body mass index (bmi = weight / height^2).

    if bmi <= 18.5 return "Underweight"

    if bmi <= 25.0 return "Normal"

    if bmi <= 30.0 return "Overweight"

    if bmi > 30 return "Obese"
    Args:
        weight: <int>
        height: <int>

    Returns:
        stature: <str>
    """

    stature = ""
    bmi_calc = weight / pow(height, 2)

    if bmi_calc <= 18.5:
        stature = "Underweight"
    elif bmi_calc <= 25.0:
        stature = "Normal"
    elif bmi_calc <= 30.0:
        stature = "Overweight"
    elif bmi_calc > 30:
        stature = "Obese"

    return stature
