#LAURENTIUS MICHAEL
#TP061310

def main_menu_function():
    opt = int(input("\t\t*****WELCOME TO REAL CHAMPIONS SPORT  ACADEMY*****\nSelect User Type:\n1. Admin\n2. Registered Student\n3. Non Registered Student\nYour choice: "))
    while(opt > 3 or opt < 1):
        opt = int(input("Wrong Choice!\nKindly select user type again:\n1. Admin\n2. Registered Student\n3. Non Registered Student\nYour choice: "))
    if(opt == 1):
        admin_function()
    elif(opt == 2):
        student_function()
    else:
        nonstudent_function()

def admin_function():
    print("\t\tWelcome to Admin. Please login to access the functionalities!")
    admin_user = input("Enter your username: ")
    admin_first_login(admin_user)

def admin_first_login(check_username):
    if(check_username == "Admin"):
        admin_pass = input("Enter your password: ")
        admin_second_login(admin_pass)
    else:
        print("Username not found")

def admin_second_login(check_password):
    if(check_password == "12345"):
        admin_second_function()
    else:
        print("Your Password is Incorrect")

def admin_second_function():
    admin_option = int(input("Select one specific function:\n1. Add Record\n2. Display All Records\n3. Search Specific Record\n4. Sort and Display Record\n5. Modify Record\n6. Exit\nYour choice: "))
    while(admin_option > 6 or admin_option < 1):
        admin_option = int(input("Wrong Choice!\nSelect one specific function again:\n1. Add Record\n2. Display All Records\n3. Search Specific Record\n4. Sort and Display Record\n5. Modify Record\n6. Exit\nYour choice: "))
    if(admin_option == 1):
        add_admin_function()
    elif(admin_option == 2):
        display_admin_function()
    elif(admin_option == 3):
        search_admin_function()
    elif(admin_option == 4):
        sort_admin_function()
    elif(admin_option == 5):
        modify_admin_function()
    else:
        main_menu_function()

def add_admin_function():
    add_admin_option = int(input("Add Records of:\n1. Coach\n2. Sport\n3. Sport Schedule\nYour choice: "))
    while(add_admin_option > 3 or add_admin_option < 1):
        add_admin_option = int(input("Wrong Choice!\nAdd Records of:\n1. Coach\n2. Sport\n3. Sport Schedule\nYour choice: "))
    if(add_admin_option == 1):
        coach_add_admin_function()
    elif(add_admin_option == 2):
        sport_add_admin_function()
    else:
        schedule_add_admin_function()
   
def coach_add_admin_function():
    file = open("coach.txt","a")
    print("Enter Coach Details: ")
    coach_name = input("Enter Coach Name: ")
    coach_ID = input("Enter Coach ID: ")
    coach_join = input("Enter Coach Date Joined: ")
    coach_terminate = input("Enter Coach Date Terminated: ")
    coach_phone = input("Enter Coach Phone Number: ")
    coach_address = input("Enter Coach Address: ")
    coach_center = input("Enter Coach Center Name (Bukit Jalil, Kinrara, Cheras): ")
    coach_sport = input("Enter Coach Sport Name (Swimming/Badminton/Football/Archery/Gymnastics/Volleyball/Basketball/Cricket/Tennis/Table Tennis): ")
    file.write(coach_name+"\t"+coach_ID+"\t"+coach_join+"\t"+coach_terminate+"\t"+coach_phone+"\t"+coach_address+"\t"+coach_center+"\t"+coach_sport+"\n")
    coach_pay_admin_function(coach_name,coach_ID)
    file.close()

def coach_pay_admin_function(name_coach,ID_coach):
    nama_guru = name_coach
    ID_guru = ID_coach
    file = open("pay.txt","a")
    coach_hourlyrate = input("Enter Coach Hourly Rate (RM100/h - RM500/h): ")
    file.write(coach_hourlyrate+"\t"+nama_guru+"\t"+ID_guru+"\n")
    file.close()
    
def sport_add_admin_function():
    file= open("sport.txt","a")
    print("Enter Sport Details: ")
    sportcenter_name= input("Enter Sport Center Name (Bukit Jalil, Kinrara, Cheras): ")
    sportcenter_ID= input("Enter Sport Center ID (Bukit Jalil - BJ, Kinrara - KR, Cheras - CS): ")
    sport_name= input("Enter Sport Name (Swimming/Badminton/Football/Archery/Gymnastics/Volleyball/Basketball/Cricket/Tennis/Table Tennis): ")
    sport_ID= input("Enter Sport ID: ")
    sport_fee= input("Enter Sport Fee (RM/month): ")
    file.write(sportcenter_name+"\t"+sportcenter_ID+"\t"+sport_name+"\t"+sport_ID+"\t"+sport_fee+"\n")
    file.close()

def schedule_add_admin_function():
    file= open("schedule.txt","a")
    print("Enter Sport Schedule Details: ")
    sportcenter_name= input("Enter Sport Center Name (Bukit Jalil, Kinrara, Cheras): ")
    sport_name= input("Enter Sport Name (Swimming/Badminton/Football/Archery/Gymnastics/Volleyball/Basketball/Cricket/Tennis/Table Tennis): ")
    sport_ID= input("Create Sport ID: ")
    sport_schedule= input("Enter Sport Schedule (Monday/Tuesday/Wednesday/Thursday/Friday/Saturday/Sunday, Time): ")
    file.write(sportcenter_name+"\t"+sport_name+"\t"+sport_ID+"\t"+sport_schedule+"\n")
    file.close()

def display_admin_function():
    display_admin_option = int(input("Display All Records of:\n1. Coach\n2. Sport\n3. Registered Student\nYour choice: "))
    while(display_admin_option > 3 or display_admin_option < 1):
        display_admin_option = int(input("Wrong Choice!\nDisplay All Records of:\n1. Coach\n2. Sport\n3. Registered Student\nYour choice: "))
    if(display_admin_option == 1):
        coach_display_admin_function()
    elif(display_admin_option == 2):
        sport_display_admin_function()
    else:
        student_display_admin_function()

def coach_display_admin_function():
    file= open("coach.txt","r")
    print(file.read())
    file.close

def sport_display_admin_function():
    file= open("sport.txt","r")
    print(file.read())
    file.close

def student_display_admin_function():
    file= open("student.txt","r")
    print(file.read())
    file.close

def search_admin_function():
    search_admin_option = int(input("Search Specific Records of:\n1. Coach by Coach ID\n2. Coach by Rating\n3. Sport by Sport ID\n4. Student by Student ID\nYour choice: "))
    while(search_admin_option > 4 or search_admin_option < 1):
        search_admin_option = int(input("Wrong Choice!\nSearch Specific Records of:\n1. Coach by Coach ID\n2. Coach by Rating\n3. Sport by Sport ID\n4. Student by Student ID\nYour choice: "))
    if(search_admin_option == 1):
        coachid_search_admin_function()
    elif(search_admin_option == 2):
        coachrating_search_admin_function()
    elif(search_admin_option == 3):
        sport_search_admin_function()
    else:
        student_search_admin_function()

def coachid_search_admin_function():
    data= input("Enter Coach ID to be searched in file: ")
    file= open("coach.txt","r")
    for line in file:
        line= line.rstrip()
        if data in line:
            print(line)

def coachrating_search_admin_function():
    data= input("Enter Rating to be searched in file (1 - 5): ")
    file= open("feedback.txt","r")
    for line in file:
        if(line.startswith(data)):
            print(line)
        
def sport_search_admin_function():
    data= input("Enter Sport ID to be searched in file: ")
    file= open("sport.txt","r")
    for line in file:
        line= line.rstrip()
        if data in line:
            print(line)

def student_search_admin_function():
    data= input("Enter Student ID to be searched in file: ")
    file= open("student.txt","r")
    for line in file:
        if(line.startswith(data)):
            print(line)   
            
def sort_admin_function():
    sort_admin_option = int(input("Sort and Display Records of:\n1. Coaches by Name\n2. Coaches by Hourly Pay Rate\n3. Coaches by Performance\nYour choice: "))
    while(sort_admin_option > 3 or sort_admin_option < 1):
        sort_admin_option = int(input("Wrong Choice!\nSort and Display Records of:\n1. Coaches by Name\n2. Coaches by Hourly Pay Rate\n3. Coaches by Performance\nYour choice: "))
    if(sort_admin_option == 1):
        name_sort_admin_function()
    elif(sort_admin_option == 2):
        rate_sort_admin_function()
    else:
        performance_sort_admin_function()

def name_sort_admin_function():
    file = open("coach.txt","r")
    words = []
    for line in file:
        words.append(line)
    file.close()
    words.sort()
    for i in words:
        print(i)

def rate_sort_admin_function():
    file = open("pay.txt","r")
    words = []
    for line in file:
        words.append(line)
    file.close()
    words.sort()
    for i in words:
        print(i)

def performance_sort_admin_function():
    file = open("feedback.txt","r")
    words = []
    for line in file:
        words.append(line)
    file.close()
    words.sort()
    for i in words:
        print(i)

def modify_admin_function():
    modify_admin_option = int(input("Modify Record of:\n1. Coach\n2. Sport\n3. Sport Schedule\nYour choice: "))
    while(modify_admin_option > 3 or modify_admin_option < 1):
        modify_admin_option = int(input("Wrong Choice!\nModify Record of:\n1. Coach\n2. Sport\n3. Sport Schedule\nYour choice: "))
    if(modify_admin_option == 1):
        coach_modify_admin_function()
    elif(modify_admin_option == 2):
        sport_modify_admin_function()
    else:
        schedule_modify_admin_function()

def coach_modify_admin_function():
    name_coach = input("Enter Coach's Name to be modified: ")
    no = 0
    words = []
    with open('coach.txt', 'r') as file:
        # read a list of lines into data
        data = file.readlines()
    file = open("coach.txt","r")
    for line in file:
        words.append(line)
    file.close()
    for cnt in words:
        if name_coach in cnt:
            hao = no
            coach_modify_admin_second_function(hao,data)
        else:
            no = no + 1
            
def coach_modify_admin_second_function(angka,daftar):
    nomor = angka
    jawaban = daftar
    file = open("coach.txt","w")
    print("Enter Coach Details: ")
    coach_name = input("Enter Coach Name: ")
    coach_ID = input("Enter Coach ID: ")
    coach_join = input("Enter Coach Date Joined: ")
    coach_terminate = input("Enter Coach Date Terminated: ")
    coach_phone = input("Enter Coach Phone Number: ")
    coach_address = input("Enter Coach Address: ")
    coach_center = input("Enter Coach Center Name (Bukit Jalil, Kinrara, Cheras): ")
    coach_sport = input("Enter Coach Sport Name (Swimming/Badminton/Football/Archery/Gymnastics/Volleyball/Basketball/Cricket/Tennis/Table Tennis): ")
    jawaban[nomor] = (coach_name+"\t"+coach_ID+"\t"+coach_join+"\t"+coach_terminate+"\t"+coach_phone+"\t"+coach_address+"\t"+coach_center+"\t"+coach_sport+"\n")
    file.writelines(jawaban)
    coach_pay_modify_admin_function(coach_name,coach_ID,nomor)
    file.close()
    print("You have modified "+coach_name+"'s record")
    
def coach_pay_modify_admin_function(name_coach,ID_coach,numbres):
    nama_guru = name_coach
    ID_guru = ID_coach
    urutan = numbres
    with open('pay.txt', 'r') as file:
        # read a list of lines into data
        dataku = file.readlines()
    file = open("pay.txt","w")
    coach_hourlyrate = input("Enter Coach Hourly Rate (RM100/h - RM500/h): ")
    dataku[urutan] = (coach_hourlyrate+"\t"+nama_guru+"\t"+ID_guru+"\n")
    file.writelines(dataku)
    file.close()

def sport_modify_admin_function():
    id_sport = input("Enter Sport's ID to be modified: ")
    no = 0
    words = []
    with open('sport.txt', 'r') as file:
        # read a list of lines into data
        data = file.readlines()
    file = open("sport.txt","r")
    for line in file:
        words.append(line)
    file.close()
    for cnt in words:
        if id_sport in cnt:
            hao = no
            sport_modify_admin_second_function(hao,data)
        else:
            no = no + 1
            
def sport_modify_admin_second_function(angka,daftar):
    nomor = angka
    jawaban = daftar
    file = open("sport.txt","w")
    print("Enter Sport Details: ")
    sportcenter_name= input("Enter Sport Center Name (Bukit Jalil, Kinrara, Cheras): ")
    sportcenter_ID= input("Enter Sport Center ID (Bukit Jalil - BJ, Kinrara - KR, Cheras - CS): ")
    sport_name= input("Enter Sport Name (Swimming/Badminton/Football/Archery/Gymnastics/Volleyball/Basketball/Cricket/Tennis/Table Tennis): ")
    sport_ID= input("Enter Sport ID: ")
    sport_fee= input("Enter Sport Fee (RM/month): ")
    jawaban[nomor] = (sportcenter_name+"\t"+sportcenter_ID+"\t"+sport_name+"\t"+sport_ID+"\t"+sport_fee+"\n")
    file.writelines(jawaban)
    file.close()
    print("You have modified "+sport_ID+" record")

def schedule_modify_admin_function():
    id_sport2 = input("Enter Sport's ID to be modified: ")
    no = 0
    words = []
    with open('schedule.txt', 'r') as file:
        # read a list of lines into data
        data = file.readlines()
    file = open("schedule.txt","r")
    for line in file:
        words.append(line)
    file.close()
    for cnt in words:
        if id_sport2 in cnt:
            hao = no
            schedule_modify_admin_second_function(hao,data)
        else:
            no = no + 1
            
def schedule_modify_admin_second_function(angka,daftar):
    nomor = angka
    jawaban = daftar
    file = open("schedule.txt","w")
    print("Enter Sport Schedule Details: ")
    sportcenter_name= input("Enter Sport Center Name (Bukit Jalil, Kinrara, Cheras): ")
    sport_name= input("Enter Sport Name (Swimming/Badminton/Football/Archery/Gymnastics/Volleyball/Basketball/Cricket/Tennis/Table Tennis): ")
    sport_ID= input("Create Sport ID: ")
    sport_schedule= input("Enter Sport Schedule (Monday/Tuesday/Wednesday/Thursday/Friday/Saturday/Sunday, Time): ")
    jawaban[nomor] = (sportcenter_name+"\t"+sport_name+"\t"+sport_ID+"\t"+sport_schedule+"\n")
    file.writelines(jawaban)
    file.close()
    print("You have modified "+sport_ID+" record")

def student_function():
    print("\t\tWelcome to Our Student Platform. Please login to access the functionalities!")
    login_user = input("Enter your username: ")
    student_first_login(login_user)

def student_first_login(student_username):
    file= open("student.txt","r")
    for line in file:
        line= line.rstrip()
        if student_username in line:
            login_pass = input("Enter your password: ")
            student_second_login(line,login_pass,student_username)
    file.close()

def student_second_login(baris,student_password,siswa_username):
    siswa_user = siswa_username
    if student_password in baris:
        student_second_function(siswa_user)
    else:
        print("Your Password or Username is Incorrect")

def student_second_function(username_siswa):
    user_siswa = username_siswa
    student_option = int(input("Select one specific function:\n1. View Detail of Coach\n2. View Detail of Self-Record\n3. View Detail of Sport Schedule\n4. Modify Self-Record\n5. Provide Feedback & Rating\n6. Exit\nYour choice: "))
    while(student_option > 6 or student_option < 1):
        student_option = int(input("Wrong Choice!\nSelect one specific function:\n1. View Detail of Coach\n2. View Detail of Self-Record\n3. View Detail of Sport Schedule\n4. Modify Self-Record\n5. Provide Feedback & Rating\n6. Exit\nYour choice: "))
    if(student_option == 1):
        coach_student_function()
    elif(student_option == 2):
        selfrecord_student_function(user_siswa)
    elif(student_option == 3):
        schedule_student_function(user_siswa)
    elif(student_option == 4):
        modify_student_function(user_siswa)
    elif(student_option == 5):
        feedback_student_function()
    else:
        main_menu_function()

def coach_student_function():
    file= open("coach.txt","r")
    print(file.read())
    file.close

def selfrecord_student_function(username_murid):
    file= open("student.txt","r")
    for line in file:
        line= line.rstrip()
        if username_murid in line:
            print(line)
            
def schedule_student_function(username_murid):
    file= open("student.txt","r")
    for line in file:
        line= line.rstrip()
        if username_murid in line:
            baris = line
    myfile = open("schedule.txt","r")
    if "Bukit Jalil" in baris:
        if "Swimming" in baris:
            for line in myfile:
                line= line.rstrip()
                if "Bukit Jalil" in line:
                    if "Swimming" in line:
                        print(line)
        elif "Badminton" in baris:
            for line in myfile:
                line= line.rstrip()
                if "Bukit Jalil" in line:
                    if "Badminton" in line:
                        print(line)
        elif "Football" in baris:
            for line in myfile:
                line= line.rstrip()
                if "Bukit Jalil" in line:
                    if "Football" in line:
                        print(line)
        elif "Archery" in baris:
            for line in myfile:
                line= line.rstrip()
                if "Bukit Jalil" in line:
                    if "Archery" in line:
                        print(line)
        elif "Gymnastics" in baris:
            for line in myfile:
                line= line.rstrip()
                if "Bukit Jalil" in line:
                    if "Gymnastics" in line:
                        print(line)
        elif "Volleyball" in baris:
            for line in myfile:
                line= line.rstrip()
                if "Bukit Jalil" in line:
                    if "Volleyball" in line:
                        print(line)
        elif "Basketball" in baris:
            for line in myfile:
                line= line.rstrip()
                if "Bukit Jalil" in line:
                    if "Basketball" in line:
                        print(line)
        elif "Cricket" in baris:
            for line in myfile:
                line= line.rstrip()
                if "Bukit Jalil" in line:
                    if "Cricket" in line:
                        print(line)
        elif "Tennis" in baris:
            for line in myfile:
                line= line.rstrip()
                if "Bukit Jalil" in line:
                    if "Tennis" in line:
                        print(line)
        elif "Table Tennis" in baris:
            for line in myfile:
                line= line.rstrip()
                if "Bukit Jalil" in line:
                    if "Table Tennis" in line:
                        print(line)
        else:
            print("There is no schedule for your registered sport.")
    elif "Kinrara" in baris:
        if "Swimming" in baris:
            for line in myfile:
                line= line.rstrip()
                if "Kinrara" in line:
                    if "Swimming" in line:
                        print(line)
        elif "Badminton" in baris:
            for line in myfile:
                line= line.rstrip()
                if "Kinrara" in line:
                    if "Badminton" in line:
                        print(line)
        elif "Football" in baris:
            for line in myfile:
                line= line.rstrip()
                if "Kinrara" in line:
                    if "Football" in line:
                        print(line)
        elif "Archery" in baris:
            for line in myfile:
                line= line.rstrip()
                if "Kinrara" in line:
                    if "Archery" in line:
                        print(line)
        elif "Gymnastics" in baris:
            for line in myfile:
                line= line.rstrip()
                if "Kinrara" in line:
                    if "Gymnastics" in line:
                        print(line)
        elif "Volleyball" in baris:
            for line in myfile:
                line= line.rstrip()
                if "Kinrara" in line:
                    if "Volleyball" in line:
                        print(line)
        elif "Basketball" in baris:
            for line in myfile:
                line= line.rstrip()
                if "Kinrara" in line:
                    if "Basketball" in line:
                        print(line)
        elif "Cricket" in baris:
            for line in myfile:
                line= line.rstrip()
                if "Kinrara" in line:
                    if "Cricket" in line:
                        print(line)
        elif "Tennis" in baris:
            for line in myfile:
                line= line.rstrip()
                if "Kinrara" in line:
                    if "Tennis" in line:
                        print(line)
        elif "Table Tennis" in baris:
            for line in myfile:
                line= line.rstrip()
                if "Kinrara" in line:
                    if "Table Tennis" in line:
                        print(line)
        else:
            print("There is no schedule for your registered sport.")
    elif "Cheras" in baris:
        if "Swimming" in baris:
            for line in myfile:
                line= line.rstrip()
                if "Cheras" in line:
                    if "Swimming" in line:
                        print(line)
        elif "Badminton" in baris:
            for line in myfile:
                line= line.rstrip()
                if "Cheras" in line:
                    if "Badminton" in line:
                        print(line)
        elif "Football" in baris:
            for line in myfile:
                line= line.rstrip()
                if "Cheras" in line:
                    if "Football" in line:
                        print(line)
        elif "Archery" in baris:
            for line in myfile:
                line= line.rstrip()
                if "Cheras" in line:
                    if "Archery" in line:
                        print(line)
        elif "Gymnastics" in baris:
            for line in myfile:
                line= line.rstrip()
                if "Cheras" in line:
                    if "Gymnastics" in line:
                        print(line)
        elif "Volleyball" in baris:
            for line in myfile:
                line= line.rstrip()
                if "Cheras" in line:
                    if "Volleyball" in line:
                        print(line)
        elif "Basketball" in baris:
            for line in myfile:
                line= line.rstrip()
                if "Cheras" in line:
                    if "Basketball" in line:
                        print(line)
        elif "Cricket" in baris:
            for line in myfile:
                line= line.rstrip()
                if "Cheras" in line:
                    if "Cricket" in line:
                        print(line)
        elif "Tennis" in baris:
            for line in myfile:
                line= line.rstrip()
                if "Cheras" in line:
                    if "Tennis" in line:
                        print(line)
        elif "Table Tennis" in baris:
            for line in myfile:
                line= line.rstrip()
                if "Cheras" in line:
                    if "Table Tennis" in line:
                        print(line)
        else:
            print("There is no schedule for your registered sport.")
    else:
        print("Your registered sport center is not found.")

def modify_student_function(username_murid):
    nama_pengguna = username_murid
    no = 0
    words = []
    with open('student.txt', 'r') as file:
        # read a list of lines into data
        data = file.readlines()
    file = open("student.txt","r")
    for line in file:
        words.append(line)
    file.close()
    for cnt in words:
        if nama_pengguna in cnt:
            hao = no
            modify_student_second_function(hao,data)
        else:
            no = no + 1
            
def modify_student_second_function(angka,daftar):
    nomor = angka
    jawaban = daftar
    file = open("student.txt","w")
    student_user = input("Create your username: ")
    student_pass = input("Create your password: ")
    student_id = input("Create Your Student ID (6 digits): ")
    student_name = input("Enter Your Name: ")
    student_dob = input("Enter Your Date of Birth (DD/MM/YYYY): ")
    student_address = input("Enter Your Address: ")
    student_phone = input("Enter Your Phone Number: ")
    student_sport = input("Enter Your Chosen Sport (Swimming/Badminton/Football/Archery/Gymnastics/Volleyball/Basketball/Cricket/Tennis/Table Tennis): ")
    student_center = input("Enter Your Chosen Sport Center: ")
    jawaban[nomor] = (student_id+"\t"+student_name+"\t"+student_dob+"\t"+student_address+"\t"+student_phone+"\t"+student_sport+"\t"+student_center+"\t"+student_user+"\t"+student_pass+"\n")
    file.writelines(jawaban)
    file.close()
    print("You have modified your record")
    
def feedback_student_function():
    file = open("feedback.txt","a")
    print("Kindly provide your feedback: ")
    feedback_name = input("Enter Coach Name: ")
    feedback_id = input("Enter Coach ID: ")
    feedback_star = input("Enter Rating for Coach (1-Very Poor, 5-Excellent): ")
    feedback_comment = input("Enter Feedback: ")
    file.write(feedback_star+"\t"+feedback_name+"\t"+feedback_id +"\t"+feedback_comment+"\n")
    file.close()
    print("Thank you for giving us feedback")

def nonstudent_function():
    nonstudent_option = int(input("\t\t*****REAL CHAMPIONS SPORT  ACADEMY*****\nSelect one specific function:\n1. View Detail of Sport\n2. View Detail of Sport Schedule\n3. Register\n4. Exit\nYour choice: "))
    while(nonstudent_option > 4 or nonstudent_option < 1):
        nonstudent_option = int(input("Wrong Choice!\nSelect one specific function:\n1. View Detail of Sport\n2. View Detail of Sport Schedule\n3. Register\n4. Exit\nYour choice: "))
    if(nonstudent_option == 1):
        sport_nonstudent_function()
    elif(nonstudent_option == 2):
        schedule_nonstudent_function()
    elif(nonstudent_option == 3):
        register_nonstudent_function()
    else:
        main_menu_function()

def sport_nonstudent_function():
    file= open("sport.txt","r")
    print(file.read())
    file.close
   
def schedule_nonstudent_function():
    file= open("schedule.txt","r")
    print(file.read())
    file.close

def register_nonstudent_function():
    file = open("student.txt","a")
    student_user = input("Create your username: ")
    student_pass = input("Create your password: ")
    student_id = input("Create Your Student ID (6 digits): ")
    student_name = input("Enter Your Name: ")
    student_dob = input("Enter Your Date of Birth (DD/MM/YYYY): ")
    student_address = input("Enter Your Address: ")
    student_phone = input("Enter Your Phone Number: ")
    student_sport = input("Enter Your Chosen Sport (Swimming/Badminton/Football/Archery/Gymnastics/Volleyball/Basketball/Cricket/Tennis/Table Tennis): ")
    student_center = input("Enter Your Chosen Sport Center: ")
    file.write(student_id+"\t"+student_name+"\t"+student_dob+"\t"+student_address+"\t"+student_phone+"\t"+student_sport+"\t"+student_center+"\t"+student_user+"\t"+student_pass+"\n")
    file.close()
    print("You have created your account successfully!")

option = int(input("Do you want to continue? '0' to continue or any other numbers to terminate: "))
while(option == 0):
    main_menu_function()
    option = int(input("Do you want to continue? '0' to continue or any other numbers to terminate: "))
print("GOOD BYE!")



