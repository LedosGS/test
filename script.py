import csv



def calculate_average_grade(grades):
    """
    вычисляем среднюю оценку из списка 
    """
    valid_gareds = [grade for grade in grades if grade is not None]
    return round(sum(valid_gareds)/len(valid_gareds), 3) if valid_gareds else 0

def process_student_data(student_data):
    """
    обрабатывает данные студентов 

    args:
    student_data: список словарей, каждый содержит данные студента

    returns:
    обработанный список  данными студентов
    """

    grades = [student.get("grade") for student in student_data]

    avarage_grade = calculate_average_grade(grades)

    for student in student_data:
        if student ["grade"] is None:
            student["grade"] = avarage_grade

    return student_data

def save_to_csv(student_data, filename):


    with open(filename, mode="w" , newline="") as file:
        writer = csv.DictWriter(file,fieldnames=student_data[0].keys())
        writer.writeheader()
        writer.writerow(student_data)


def readCSV():
    """
    читаем csv файл
    """

    student_data = []

    with open(file_path, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            student_data.append(row)
    return student_data


def sort(student_data, key):

    """
    алгоритм сортировки вставками
    """
    for i in range(1, len(student_data)):
        currentValue = student_data[i]
        position = i

        while position > 0 and student_data(position -1)[key] > currentValue[key]:
            student_data[position] = student_data[position - 1]
            position -= 1

    return student_data[::-1]




def main():
    pass

    # for student in clear_data:


main()





