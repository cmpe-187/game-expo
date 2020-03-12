__author__ = "Zelin Cai, Patrick Silvestre"
__license__ = "MIT"


def ticketing_module(age, gender):
    if gender == "boy":
        if age < 6:
            return "rhyming"
        elif 7 < age < 10:
            return "storytelling"
        elif 11 < age < 15:
            return "quiz"
        elif 20 < age:
            return "poetry"
        else:
            return ""
    elif gender == "girl":
        if age < 6:
            return "rhyming"
        elif 7 < age < 10:
            return "drawing"
        elif 10 < age < 15:
            return "essay writing"
        elif 20 < age:
            return "poetry"
        else:
            return ""
    else:
        return ""
