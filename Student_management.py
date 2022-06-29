import math
import Info_student

class StudentManagement:
    # List, Dict
    listStudent = []

    # Xây dựng một hàm tự động sinh ra mã học sinh
    def autogenous_Id(self): # Tìm giá trị lớn nhất trong một mảng
        id = 1
        if (self.count_Student() > 0):
            id = self.listStudent[0]._id
            for st in self.listStudent:
                if (id < st._id):
                    id = st._id
            id = id + 1
        return id

    def count_Student(self):
        return self.listStudent.__len__()

    def input_Student(self): # Viết hàm nhập thông tin của từng học sinh
        id_st = self.autogenous_Id()
        full_name_st = input("Nhập họ tên của học sinh: " )
        birthday_st = input("Nhập ngày tháng năm sinh của học sinhL: ")
        sex_st = input("Nhập giới tính của học sinh: ")
        score_math_st = float(input("Nhập điểm môn toán của học sinh: "))
        score_english_st = float(input("Nhập điểm môn tiếng anh của học sinh: "))
        score_literature_st = float(input("Nhập điểm môn ngữ văn của học sinh: "))
        st = Info_student.Student(id_st, full_name_st, birthday_st, sex_st, score_math_st, score_english_st, score_literature_st)
        self.score_Avg(st)
        self.rank_Score(st)
        self.listStudent.append(st)

    def score_Avg(self, st:Info_student.Student):
        score_avg = (st._score_math + st._score_english + st._score_literature) / 3

    def rank_Score(self, st:Info_student.Student):
        




