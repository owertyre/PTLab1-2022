# -*- coding: utf-8 -*-
import argparse
import sys

from CalcRating import CalcRating
from XmlDataReader import XmlDataReader
from ExcellentStudent import ExcellentStudent


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])
    reader = XmlDataReader()

    students = reader.read(path)
    print("Students: ", students)

    rating = CalcRating(students).calc()
    print("Rating: ", rating)

    data = reader.read(path)
    print(data)

    excellentStudent = ExcellentStudent(students).calc()
    if len(excellentStudent) != 0:

        print("Студент имеющий 100 баллов по всем дисциплинам:"
              " ", excellentStudent)

    else:

        print("Студент имеющий 100 баллов по всем дисциплинам - отсутствует")


if __name__ == "__main__":
    main()
