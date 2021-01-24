import datetime


class Age(object):
    '''Класс для счета возраста'''
    def __init__(self, iin: str):
        self.year = iin[0:2]
        self.month = iin[2:4]
        self.day = iin[4:6]
        self.century = iin[6]

    def getYear(self):
        full_year = ''
        if int(self.century) in range(0, 1):
            full_year = f'18{str(self.year)}'
        elif int(self.century) in range(3, 4):
            full_year = f'19{str(self.year)}'
        elif int(self.century) in range(5, 6):
            full_year = '20' + str(self.year)
        return full_year

    def getAge(self):
        year = self.getYear()
        birth_day = datetime.date(int(year), int(self.month), int(self.day))
        now = datetime.date.today()
        age = (now - birth_day).days // 365
        return age
