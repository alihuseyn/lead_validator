from typing import List, TypedDict


class Entry(TypedDict):
    url: str
    email: str


def writer(entry: Entry, *, filename: str = "invalid.txt"):
    with open(filename, "a") as fp:
        fp.write(str(entry) + "\n")


def reader(filename: str) -> List[Entry]:
    data = []
    with open(filename, "r") as fp:
        line = fp.readline()
        while line != "":
            line = line.strip("\n").strip()
            parts = line.split(",")
            data.append(Entry(url=parts[0].strip(), email=parts[1].strip()))
            line = fp.readline()

    return data
