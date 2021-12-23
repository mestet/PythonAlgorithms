from mgu import SearchStringPattern


def test():
    cases = (
        ("lorem ipsum, quia dolor sit, amet, consectetur", "dolor @it,@@met", 18),
        ("qweqwe wertsaq ertsqa wertgad wertgard", "wer@ga", 22),
        ("qwerwq er bababaobaber", "ba@ba", 14),
        ("asdf tr4gtrghadfv eterfg asd asdfasd asdfasde", "@had@", 11),
        ("Hello Darkness my old friend, I come to talk with u again", "@@ain", 52),
        ("sadfqwef qwef qwef", "@", 0),
        ("qwer qwerqwer adfasd f 3r4tgrgsdfgwertqer qert", "dfasZZ", -1),
        ("qwerqwer qwer qwe rqwe rqwerqwe rqwer", "rque", -1),
        ("", "", 0),
    )
    for tc in cases:
        actual = SearchStringPattern.find_pattern(tc[0], tc[1])
        expected = tc[2]
        if actual == tc[2]:
            print(f"Test passed")
        else:
            print(f"Test failed: \n\t{tc[0]}\n\t{tc[1]}\n\t{actual=} != {expected=}")


if __name__ == "__main__":
    test()
