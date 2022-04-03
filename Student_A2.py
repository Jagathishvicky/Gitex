import sys
class Student:
    def __init__(self):
        self.mark_list, self.f_sub = [], []
        self.m_flag, self.tot, self.avg = 0, 0, 0
    def get(self):
        self.s_name = input("Student Name: ").capitalize()
        try:
            self.s_roll = int(input("Student Roll No: "))
        except ValueError:
            print("No.. input is not a number. It's a string")
            sys.exit()
        if self.s_roll > 100 or self.s_roll < 0:
            print("Roll number is invalid, it must between 0 to 100")
            sys.exit()

        self.num_sub = int(input("No of subjets: "))
        for i in range(1, self.num_sub+1):
            try:
                self.s_mark = int(input(f"Subject {i} Mark: "))
                self.mark_list.append(self.s_mark)
                print(self.mark_list)
            except ValueError:
                print("No.. input is not a number. It's a string")
                sys.exit()
        for i, j in enumerate(self.mark_list, 1):
            if j > 100 or j < 0:
                print(f"Subject {i} mark is invalid")
                sys.exit()
            else:
                self.tot = sum(self.mark_list)
                self.avg = self.tot / self.num_sub
                self.m_flag+=1

    def display(self):
        if self.m_flag > 0:
            for i, j in enumerate(self.mark_list, 1):
                if j < 40:
                    self.f_sub.append(i)
            if len(self.f_sub) == 0:
                print(f"Hi {self.s_name} congratulations! you got passed in all the subjects. ")
            else:
                print(f"Sorry {self.s_name} you got failed in these subjects {self.f_sub} ")
            print("Total:", self.tot)
            print("Average:", self.avg)
            if self.avg > 89:
                print("Grade: S")
            elif self.avg > 79 or self.avg < 90:
                print("Grade: A")
            elif self.avg > 69 or self.avg < 80:
                print("Grade: B")
            else:
                print("Grade: C")


num = int(input("No of student: "))
for i in range(num):
    s = Student()
    s.get()
    s.display()