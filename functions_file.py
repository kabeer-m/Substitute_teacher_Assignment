import csv
import time

def getday():           #fuction to automatically get time
    t = time.asctime()
    s = t.split()
    day = s[0]
    return day


def Absentees(L,day,H1,H2):    #function to get schedule of absetees
    with open('Teachers-timetable.csv','r') as file:    # format = [name,day,1,2,3,4,5,6,7,8]
        R = []
        reader = csv.reader(file)
        for i in reader :
            if i[0] in L and i[1]==day :        #check if day and name is same
                if i[0] in H1 :
                    S = i[:6]+['','','','']
                    R.append(S)     # first 4 periods
                elif i[0] in H2 :
                    S = i[:2] + ['','','',''] + i[6:]
                    R.append(S)
                else :
                    R.append(i)
    return(R)  ## Dont forget to retun a value
                

def check_for_repeats(Absent,T,period,checklist):  #check if a teacher is already assigned to a period
    if T in Absent:                ##To check if the teacher is absent
        return False
    for i in checklist:                     
        if i[period] == T:
            return False
    else:
        return True

def check_for_double(Total,Teacher,current):
    count = 0
    
    for i in Total:
        for j in i:
            if j == Teacher:
                count += 1
                
    for i in current:
        if i == Teacher :
            count += 1
            
    if count >= 2:
        return False
    else :
        return True

def check_for_exceptions(Teacher, E_Teachers):
    if Teacher in E_Teachers :
        return False
    else:
        return True

def check_for_most_free(Candidates,day):
    no_of_free_periods = []
    with open('Teachers-timetable.csv','r') as file :
        reader = csv.reader(file)
        for Candidate in Candidates:
            for record in reader:
                if record[0]==Candidate and record[1]==day:
                    C = record.count('')
                    no_of_free_periods.append(C)
                    break
#try:
    most_free = max(no_of_free_periods)
    index_of_most_free = no_of_free_periods.index(most_free)
    teacher_with_most_free_period = Candidates[index_of_most_free]
    return(teacher_with_most_free_period)
    
    #except:
     #   return('MONITOR')

def check_for_halfday_1(teacher,period,H1):
    if (teacher in H1) and (period > 5):
        return False
    else:
        return True

def check_for_halfday_2(teacher,period,H2):
    if (teacher in H2) and (period < 6):
        return False
    else:
        return True
 
def assignment(Absent,Teacher, day, Total, E_Teachers,H1_Teachers,H2_Teachers): #Assigning the teachers
    Assigned = []                    #blank list to which names will be assigned
    with open('Teachers-timetable.csv','r') as file:
        reader = csv.reader(file)
        for i in reader:             #for every entry in main TT   
            if i[0] == Teacher and i[1] == day:#find the entry with same name,day
                for j in range(2,10):   #2-10 because first two entries are name and day

                    if i[j] == '':      #if teacher has no class that peiod
                        Assigned.append('')     #assign blank

                    elif (Teacher in H2_Teachers) and (j<6):     ##if teacher is going on half day, j<6 cus first 2 entries be name and day
                        Assigned.append('')                     ## 6th index is 5th period
                        
                    elif (Teacher in H1_Teachers) and (j>5):     ##if teacher is going on half day, j>5 cus first 2 entries be name and day
                        Assigned.append('')                     ## 5th index is 4th period

                                
                    else:               # if there is a class
                        f = open('Teachers-timetable.csv','r') # open main TT to check for free teachers
                        inner_reader = csv.reader(f)
                        Candidates = []         ## List for the candidates
                        for k in inner_reader:          #again,every entry in main TT
                            
                            if k[1]== day and k[j] == '':   #if a teacher has no class that period

                                repeat = check_for_repeats(Absent,k[0],(j-1),Total)  #check if teacher is repeated
                                double = check_for_double(Total,k[0],Assigned)
                                excepted = check_for_exceptions(k[0],E_Teachers)
                                half_day1 = check_for_halfday_1(k[0],j,H1_Teachers)
                                half_day2 = check_for_halfday_2(k[0],j,H2_Teachers)
                                
                                if repeat and double and excepted and half_day1 and half_day2:               #fuction takes name, period no (-1 becausethe first entry in total will be the name of the absent teavher)
                                    Candidates.append(k[0]) #if there r no repeats add name to a candidate list
                                else:
                                    continue

                        else :
                            Substituted_teacher = check_for_most_free(Candidates,day)
                            Assigned.append(Substituted_teacher)    
                        f.close()  #dont forget to close !!!
                
                        
    return([Teacher]+Assigned) # first entry will be absent teachers name

def make_file(sub_teachers,schedule,day):  # function to make the new file with the substitute teachers
    line = ['---------------------------------']
    line_breaker = line*9
    print(schedule)
    f = open('Substitute_sheet.csv', 'w')
    head = ['Name_of_Teacher','1','2','3','4','5','6','7','8']      # header
    writer = csv.writer(f)
    writer.writerow([day.upper()])
    writer.writerow(head)
    for i in range(len(sub_teachers)) :
        writer.writerow(sub_teachers[i])
        for j in range(len(schedule)):
            if schedule[j][0]==sub_teachers[i][0]:
                J = ['']+schedule[j][2: : ]
                writer.writerow(J)
        writer.writerow(line_breaker)
    f.close()           ### NEVER FORGET TO CLOSE!!!!!!!
    
