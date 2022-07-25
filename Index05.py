def num(s):
    if s == "1" or s == "2" or s == "3" or s == "4" or s == "5" or s == "6" or s == "7" or s == "8" or s == "9":return 1
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
