def make_upper(my_string: str) -> str:
    return my_string.upper()


def make_title(my_string: str) -> str:
    """make title for all words in string"""
    tmp_str = None
    for item in my_string.split(" "):
        if tmp_str:
            tmp_str = tmp_str + " " + item.title()
        else:
            tmp_str = item.title()
    return tmp_str


def test():
    print(make_upper("qwerty"))
    print(make_title("obey your master (c) metallica"))


if __name__ == '__main__':
    test()
