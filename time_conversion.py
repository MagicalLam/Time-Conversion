def timeConversion(s):
    s = s.split(":")
    if s[0] == "12" and s[2][2] == "A":
        s[0] = "00"
        s[2] = s[2][0:2]
        return ":".join(s)
    elif s[2][2] == "P":
        s[0] = str(int(s[0])+12)
        s[2] = s[2][0:2]
        return ":".join(s)
    else:
        s[2] = s[2][0:2]
        return ":".join(s)
