myInput = str(input("Enter your string: "))

def isPalindrome(str):
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-1-i]:
            return False
    return True

prepareInput =  myInput.casefold().replace(" ","")
print(f"After ignores spaces and capitalication: {prepareInput}")
answer = isPalindrome(prepareInput)
print(answer)

#1 รับค่า string 
#2 ตัดช่องว่างและทำเป็นพิมเล็กทั้งหมด
#3 ลูปตั้งแต่ตัว 0 ถึง ตัวสุดท้ายของ string ที่งส่งเข้ามา
    #3.1 ถ้าตัวอักษรแรก + n != ตัวอักษรสุดท้าย - n
        #3.1.1 เป็นเท็จ
#4 ที่เหลือเป็นจริง