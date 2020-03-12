__author__ = "Zelin Cai, Patrick Silvestre"
__license__ = "MIT"


def ticketing_module(gender, age):
    if age < 6:
        return "rhyming"
    elif 7 < age < 10:
        if gender == "girl":
            return "drawing"
        else:
            return "storytelling"
    elif 10 < age < 15:
        if gender == "girl":
            return "essay writing"
    elif 11 < age < 15:
        if gender == "boy":
            return "quiz"
    elif 20 < age:
        return "poetry"
    else:
        return ""
