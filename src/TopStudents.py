from Types import DataType

RatingType = dict[str, float]


class TopStudents:

    def __init__(self, data: DataType) -> None:
        self.data: DataType = data
        self.rating: RatingType = {}
        self.nameStudent: str = ""

    def calc(self) -> RatingType:
        studentName = "Такие студенты отсутствуют"
        for key in self.data:
            x = 0
            for subject in self.data[key]:
                if subject[1] == 100:
                    x += 1
            if x == len(self.data[key]):
                studentName = key

            self.nameStudent = studentName
        return self.nameStudent