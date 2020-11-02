import csv
def write_into_csv(info_list):
    with open("student_info.csv",'a',newline='') as csv_file:

        writer = csv.writer(csv_file)
        writer.writerow("name", "age", "contact_number", "email")
        writer.writerow(info_list)
if __name__ == '__main__':
    condition = True
    while(condition):
        student_info = input("enter  student information in the following format{name,age,contact_number,email_id}")
        print("entered information:" +student_info)

        student_info_list = student_info.split(' ')
        print("the enterered information is -\nname: {}\nage:{}\ncontact_number:{}\n email:{}".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
        choice_check = input("is the information is correct?{yes/no}:")
        if choice_check == "yes":
            write_into_csv(student_info_list)
            condition_check = input("enter {yes/no} if you want to enter the details of another student information:")
            if condition_check == "yes":
                condition = True
            elif condition_check == "no":
                condtion = False
        elif choice_check == "no":
                print("please re-enter the values ")
