# https://www.codewars.com/kata/5412509bd436bd33920011bc/train/python


def maskify(cc):
    length = len(cc)

    return (length - 4) * "#" + cc[-4:]