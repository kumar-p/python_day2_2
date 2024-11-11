# temprature classification for human body
def classify_temperature(temp):
    if temp < 95:
        return "Hypothermia"
    elif 95 <= temp < 97.5:
        return "Low"
    elif 97.5 <= temp < 99.5:
        return "Normal"
    elif 99.5 <= temp < 100.9:
        return "Elevated"
    else:
        return "Fever"
