def num(i):
    if i=="*":
        return 1
    return 0
def main(s):
    """
    A string of length five is given. Return the index of the "*" character, return False if not present.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    if "*" in s:
        return num(a[0]) * 0 + num(a[1]) * 1 + num(a[2]) * 2 + num(a[3]) * 3 + num(a[4]) * 4
    return False