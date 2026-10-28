def comp(array1, array2):
    if array1 is None or array2 is None:
        return False

    array1_squared_sorted = sorted(number * number for number in array1)
    array2_sorted = sorted(array2)

    return array2_sorted == array1_squared_sorted


if __name__ == "__main__":
    a1 = [121, 144, 19, 161, 19, 144, 19, 11]
    a2 = [
        11 * 11,
        121 * 121,
        144 * 144,
        19 * 19,
        161 * 161,
        19 * 19,
        144 * 144,
        19 * 19,
    ]
    assert comp(a1, a2)

    """    a1 = [121, 144, 19, 161, 19, 144, 19, 11]
    a2 = [11*21, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
    assert comp(a1, a2)
    a1 = [121, 144, 19, 161, 19, 144, 19, 11]
    a2 = [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]
    assert comp(a1, a2)  """
