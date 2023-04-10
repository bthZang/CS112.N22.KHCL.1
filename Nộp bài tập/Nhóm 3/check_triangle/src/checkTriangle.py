def checkTriangle(a: int, b: int, c: int) -> bool:
    if(a >= (b + c)):
        return False
    if(b >= (a + c)):
        return False
    if(c >= (a + b)):
        return False
    return True

