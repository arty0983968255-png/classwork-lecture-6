def clean_number(text):
    text=text.strip()
    text=text.replace(" ", "")
    text=text.replace("-", "")
    return text
def is_valid(number):
    if len(number)==10 and number.startswith("0"):
        return True
    else:
        return False
def digit_sum(number):
    total=0
    for digit in number:
        total=total+int(digit)
    return total
phone=input("phone: ")
number=clean_number(phone)
if is_valid(number):
    formatted=number[:3]+"-"+number[3:6]+"-"+number[6:]
    hidden=number[0:3]+"-xxx-"+number[6:]
    print("formatted: ", formatted)
    print("hidden: ", hidden)
    print("digit sum: ", digit_sum(number))
else:
    print("invalid number")