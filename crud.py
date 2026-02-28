import json


def update_log() -> None:
    with open("log.json", "r+", encoding="utf-8") as file:
        log = json.load(file)

        new = {}
        for g, fn_dict in log.items():
            for fn, ti_dict in fn_dict.items():
                for ti, r_list in ti_dict.items():
                    pass

        file.seek(0)
        json.dump(new, file, ensure_ascii=False, indent=None, separators=(",", ":"))
        file.truncate()


def update_students() -> None:
    with open("groups.json", "r+", encoding="utf-8") as file:
        students = json.load(file)

        #

        students = dict(sorted(students.items()))

        file.seek(0)
        json.dump(students, file, ensure_ascii=False, indent=2)
        file.truncate()


if __name__ == "__main__":
    pass
