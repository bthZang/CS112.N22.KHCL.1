from src.checkTriangle import checkTriangle

if __name__ == "__main__":
    a = int(input("Nhập a: "))
    b = int(input("Nhập b: "))
    c = int(input("Nhập c: "))

    
    if(checkTriangle(a,b,c)):
        print(
            "La tam giac"
        )
    else:
        print(
            "Ko la tam giac"
        )