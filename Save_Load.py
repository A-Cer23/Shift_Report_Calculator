import json


from Shift_Report import ShiftReport
from datetime import date,timedelta



def save(data):
    with open("Data/Shift_Reports.json", "w") as file:
        sr_json = convert_to_json(data)
        json.dump(sr_json, file, indent=2, separators=(",",":"))

def convert_to_json(data):
    jsonData = []
    for sr in data:
        jsonData.append(sr.as_dict())
    return jsonData

def load():
    shiftReports = []
    with open("Data/Shift_Reports.json", "r") as file:
        json_list = json.load(file)
        for jsonObj in json_list:
            sr = convert_to_ShiftReport(jsonObj)
            shiftReports.append(sr)
        return shiftReports

def convert_to_ShiftReport(jsonObj):
    year, month, day = split_json(jsonObj["Date"],"date")
    startHour, startMinute, startSecond = split_json(jsonObj["Start Time"], "time")
    endHour, endMinute, endSecond = split_json(jsonObj["End Time"], "time")

    sr_date = date(year,month,day)
    sr_startTime = timedelta(hours=startHour, minutes=startMinute, seconds=startSecond)
    sr_endTime = timedelta(hours=endHour, minutes=endMinute, seconds=endSecond)

    return ShiftReport(sr_date,sr_startTime,sr_endTime)

def split_json(values, type):
    if type == "date":
        split = values.split("-")
        return int(split[0]), int(split[1]), int(split[2])
    elif type == "time":
        split = values.split(":")
        return int(split[0]), int(split[1]), int(split[2])
