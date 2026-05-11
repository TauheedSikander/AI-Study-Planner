from calendar import Day
import datetime as dt

def generate_schedule(exam_date_str, subjects, hours_per_day):
    today = dt.date.today()
    exam_date = dt.datetime.strptime(exam_date_str,"%Y-%m-%d").date()
    days_left = (exam_date - today).days
    
    if days_left <= 0:
        return ("Cannot generate Schedule")
    
    hours_per_subject = (hours_per_day) / len(subjects)
    
    if len(subjects) == 0:
     return "Subjects list cannot be empty"
    
    schedule = {}
    
    for i in range(1, days_left + 1):
        schedule["Day " + str(i)] = {}

        for j in range(0, len(subjects)):
            schedule["Day " + str(i)][subjects[j]] = hours_per_subject
            
    return schedule