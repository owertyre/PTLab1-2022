from Types import DataType
from Types import ExcellentRatingType

RatingsType = dict[str, float]


class ExcellentStudent:
    def __init__(self, data: DataType, maxAvailableRating: int = 100) -> None:
        self.data: DataType = data
        self.maxAvailableRating = maxAvailableRating
        self.excellentStudents: ExcellentRatingType = {}

    def calc(self) -> ExcellentRatingType:
        alreadyAdded = False

        for student in self.data:

            isExcellentStudent = True
            subjects = []

            for subj in self.data.get(student):
                subjects.append(subj[0])

                if subj[1] != self.maxAvailableRating:
                    isExcellentStudent = False

            if isExcellentStudent:

                if not alreadyAdded:
                    self.excellentStudents[student] = subjects
                    alreadyAdded = True

        return self.excellentStudents
