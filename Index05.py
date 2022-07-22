def num(i):
    k="12345678"
    if i in k:return 1
    return 0

def main(s):
    """
    Given a variable s string of length five. Determine the number of digits involved in this variable.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    return num(s[0])+num(s[1])+num(s[2])+num(s[3])+num(s[4])
