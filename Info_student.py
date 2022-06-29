class Student:
    def __init__(self, id, full_name, birthday, sex, score_math, score_english, score_literature):
        self._id = id
        self._full_name = full_name
        self._birthday = birthday
        self._sex = sex
        self._score_math = score_math
        self._score_english = score_english
        self._score_literature = score_literature
        self._score_avg = 0
        self._rank_score = ""