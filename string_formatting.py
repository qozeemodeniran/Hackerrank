def str_format(n):
    for i in range(1, n+1):
        i_decimal = i
        i_octal = oct(i).replace("0o", "")
        i_hexa = hex(i).upper().replace("0X", "")
        i_binary = bin(i).replace("0b", "")

        print(i_decimal, i_octal, i_hexa, i_binary)
n = int(input("Enter an integer: "))
str_format(n)