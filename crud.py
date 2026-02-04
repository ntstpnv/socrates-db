import json


def update_group():
    with open("students.json", "r+", encoding="utf-8") as file:
        students = json.load(file)

        #

        file.seek(0)
        json.dump(students, file, ensure_ascii=False, indent=2)
        file.truncate()


if __name__ == "__main__":
    update_group()
