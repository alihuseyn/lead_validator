def output(*text: str, code: str):
    print("".join([f"\033[{code}", *text, "\033[0m"]))


def danger(*text: str):
    output(*text, code="91m")


def success(*text: str):
    output(*text, code="92m")


def warning(*text: str):
    output(*text, code="93m")


def info(*text: str):
    output(*text, code="94m")
