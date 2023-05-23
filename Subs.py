import pathlib, os, time
from subprocess import Popen
import datetime

from APS import scheduler

def runbatch():
    
    runfile = ""
    newfile = ""
    closest = 10
    
    #Get the current day and time 
    day = datetime.datetime.today().weekday()
    now = datetime.datetime.now()
    hr = int(now.strftime("%H:%M").split(":")[0])
    minute = int(now.strftime("%H:%M").split(":")[1])
    
    #Make array of all of the present batch files' names
    batchfiles = []
    workingbatchfiles = []
    dir_path = os.path.dirname(os.path.realpath("__file__"))
    
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith('.bat'):
                batchfiles.append(str(file))
                                
    for file in batchfiles:
        if int(file[3:5]) == day:
            workingbatchfiles.append(file)
                        
    if len(workingbatchfiles) == 1:
        runfile = workingbatchfiles[0]
    else:
        #Look for closest time
        for file in workingbatchfiles:
            filehr = int(file[6:8])
            fileminute = int(file[9:11])
            difference = abs((filehr - hr) * 60)
            difference += abs((fileminute - minute))
            
            if difference < closest:
                closest = difference
                runfile = file
   
    path = pathlib.Path("__file__").parent.resolve()
    
    os.chmod(path, 0o777)
    
    #Running the appropriate batch file
    pathfile = str(path) + "\ 33897"
    newfile = pathfile.replace(" 33897", runfile)
    
    os.chmod(newfile, 0o777)
    
    p = Popen([newfile])
    p.wait()
    stdout, stderr = p.communicate()

def addjob(date, link, browser):

    global scheduler
    
    newdate = ""
    
    for char in date:
        if char == '/':
            char = '-'
        newdate += char
    
    batchfile = "Job" + newdate + ".bat"
        
    #Create and edit batch file
    b = open(batchfile, mode='w')
    
    line1 = "set url=" + link + "\n"
    line2 = ""
    
    if browser == "1":
        line2 = "start chrome %url%\n"
    elif browser == "2":
        line2 = "start microsoft-edge:%url%\n"
    elif browser == "3":
        line2 = "start firefox.exe %url%\n"
    elif browser == "4":
        line2 = "start iexplore.exe %url%\n"
    
    b.write(line1)
    b.write(line2)
    
    b.close()
    
    #Extracting data from input datentime
    day = newdate[0:2]
    hr = newdate[3:5]
    m = newdate[6:]
    
    dayint = int(day)
    hrint = int(hr)
    mint = int(m)
    
    time.sleep(1)
    
    jobid = batchfile[:-4]
    
    #Create job    
    scheduler.add_job(runbatch, 'cron', id=jobid, day_of_week=dayint, hour=hrint, minute=mint)

def deletejob(date):

    global scheduler
    
    newdate = ""
    
    for char in date:
        if char == '/':
            char = '-'
        newdate += char
    
    filename = "Job" + newdate + ".bat"
    
    jobid = filename[:-4]
    
    if os.path.exists(filename):
        os.remove(filename)
        scheduler.remove_job(jobid)
