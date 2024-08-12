# Function that formats a number as '0number' if the number is less than 10
def number_format(number):
    if number<10:
        return "0"+str(number)
    return str(number)    

# Function that returns the correct format of days later
def days_later_format(number_of_days_later):
    if number_of_days_later == 1:
        return "(next day)"
    elif number_of_days_later > 1:
        return f"({number_of_days_later} days later)"
    return ""    

     

# Function that returns the exact day of the week, number_of_days_later from the current day of the week 
def exact_day(current_day,number_of_days_later):
    days_of_the_week = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    current_day_lower = current_day.lower() 
    resulting_day_index = (days_of_the_week.index(current_day_lower)+number_of_days_later) % 7
    return days_of_the_week[resulting_day_index].capitalize()     



# Function that takes as parameters the start time, duration and returns a dictionary that contains the hours/minutes 
#of both times as well as the formatting AM/PM of the start time.

def get_time(start,duration):
    get_time_dict = {}
    start_hour = start.split(":")[0]
    start_min = start.split(":")[1].split()[0]
    start_am_pm = start.split(":")[1].split()[1]
    duration_hour = duration.split(":")[0]
    duration_min = duration.split(":")[1]
    get_time_dict['START'] = [start_hour,start_min,start_am_pm]
    get_time_dict['DURATION'] = [duration_hour,duration_min]
    return get_time_dict


def add_time(start, duration,starting_day_of_week=False):
    time_dict = get_time(start,duration)
    # Numerical values of hours and minutes for start   time and duration
    start_hour = int(time_dict.get("START")[0])
    start_min = int(time_dict.get("START")[1])
    duration_hour = int(time_dict.get("DURATION")[0])
    duration_min = int(time_dict.get("DURATION")[1])

    # AM/PM format
    am_pm = time_dict.get("START")[2]

    # Resulting hour/min
    resulting_min = start_min + duration_min
    if resulting_min >= 60 :
        duration_hour+=1
        resulting_min = resulting_min % 60
    resulting_hour = (start_hour + duration_hour) % 12
    if resulting_hour==0 : 
        resulting_hour=12


    # Number of Days Later
    number_of_days_later = duration_hour // 24 
    if am_pm=="PM" and (start_hour + duration_hour %12 ) >=12 :
        number_of_days_later+=1  

    # The correct time format AM/PM
    changing_am_pm_format={"AM":"PM","PM":"AM"}
    am_pm_format=am_pm 
    time_diff=12-start_hour
    if duration_hour==time_diff or (duration_hour > time_diff and ((duration_hour-time_diff)//12) %2 ==0) :
        am_pm_format=changing_am_pm_format[am_pm]  

    # Formatting the output

    output_min = number_format(resulting_min)
    output_days_later=days_later_format(number_of_days_later)

    output = str(resulting_hour) + ":" + output_min + " " + am_pm_format + " " + output_days_later

    if starting_day_of_week:
        output= str(resulting_hour) + ":" + output_min + " " + am_pm_format + "," + " " + exact_day(starting_day_of_week,number_of_days_later) + " " + output_days_later

    return output.strip()    


    

def main():
    start="9:16 AM"
    duration="466:02"
    print(add_time(start,duration,"tuesday"))

    
main()    
    
