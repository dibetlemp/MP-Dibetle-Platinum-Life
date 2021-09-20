def clean_phone_number(p):
    '''Cleaning the cellphone number'''
    num = filter(str.isdigit,p)
    num_str = "".join(num)
    '''Add an initial zero if it is missing'''
    if num_str[0] != "0":
        num_str = "0"+num_str
    '''An Error for incorrect lenghth of the number'''
    if len(num_str)!= 10:
        print("Invalid Number")
        return

    return num_str

    '''Return cleaned number'''
p = input("Enter a phone number: ")
#p = "02fteue5353525f@#!+&63"

print(clean_phone_number.__doc__)
print(clean_phone_number(p))
