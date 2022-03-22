# Base values for conversion
base16 = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')

# Main Method
def main():
    while True:
        # Get user's input for menu navigation
        choices()
        choice = input("Enter your choice: ").upper()
        while (choice != 'A' and choice != 'B' and choice != 'C'):
            choice = input("Enter your choice: ").upper()

        # A. Base R to Base 10
        if (choice == 'A'):
            print("\n- BASE R TO BASE 10 -")
            base = int(input("Enter the value of base R (Choose from 2 - 16, excl. 10): "))
            while base < 2 or base > 16 or base == 10:
                base = int(input("Enter the value of base R (Choose from 2 - 16, excl. 10): "))
            value = input(f"Enter a base {base} number: ").upper()
            val_split = value.split(".")
            if len(val_split) == 1:
                while baseR_base10(value, base) == -1:
                    value = input(f"Enter a base {base} number: ").upper()
                print(f"\nResult: {value} base {base} is equal to {baseR_base10(value, base):.4F} base 10\n")
            elif len(val_split) == 2:
                fraction = baseR_base10_frac(val_split[-1], base) + baseR_base10(val_split[0], base)
                print(f"\nResult: {value} base {base} is equal to {fraction:.4F}\n")
            continue

        # B. Base 10 to Base R
        elif (choice == 'B'):
            print("\n- BASE 10 TO BASE R -")
            value = input("Enter a base 10 number (decimal): ")
            val_split = value.split(".")

            base = int(input("Enter the value of base R (Choose from 2 - 16, excl. 10): "))
            while base < 2 or base > 16 or base == 10:
                base = int(input("Enter the value of base R (Choose from 2 - 16, excl. 10): "))

            if len(val_split) == 1:
                print(f"\nResult: {value} base 10 is equal to {base10_baseR(int(value), base)}.0000 base {base}\n")
            elif len(val_split) == 2:
                print(f"\nResult: {value} base 10 is equal to {base10_baseR(int(val_split[0]), base)}.{base10_baseR_frac(val_split[-1], base):.4} base {base}\n")
            continue

        # C. Terminate the program
        elif (choice == 'C'):
            print("\n- PROGRAM TERMINATED - ")
            break

# Display the options
def choices():
    print("NUMBER BASE CONVERSION PROGRAM\n")
    print("\tA. BASE R TO BASE 10")
    print("\tB. BASE 10 TO BASE R")
    print("\tC. QUIT THE PROGRAM\n")

# Convert the corresponding values of A to F
def equivalent(value):
    value = value.upper()
    if (value >= '0' and value <= '9'):
        return ord(value) - ord('0')
    else:
        return ord(value) - ord('A') + 10;

# Calculate for base R to base 10
def baseR_base10(value, base):
    power = 1
    decimal = 0
    for i in range(len(value) - 1, -1, -1):
        if equivalent(value[i]) >= base:
            return -1
        decimal += equivalent(value[i]) * power
        power *= base
    return decimal

# Calculate for the fractional part of base R to base 10
def baseR_base10_frac(value, base):
    val = [0] * len(value)
    decimal = 0
    for i in range(len(value) - 1, -1, -1):
        if equivalent(value[i]) >= base:
            return -1
        else:
            val[i] = equivalent(value[i])
    for i in range(-1, -len(value) - 1, -1):
        val[abs(i) - 1] = val[abs(i) - 1] * (base ** i)
    return sum(val)

# Calculate for base 10 to base R
def base10_baseR(value, base):
    count = 0
    remainder = []
    answer = ""
    if value > 0:
        while value > 0:
            remainder.append(value % base)
            value = value // base
            count += 1
        for rev in remainder[::-1]:
            answer += base16[rev]
    else:
        answer = '0'
    return answer

# Calculate for the frational part of base 10 to base R
def base10_baseR_frac(value, base):
    val = float("." + value)
    ans = [0] * len(value)
    base_converted = ""
    for i in range(len(value)):
        ans[i] = int(val * base)
        temp = str(val * base).split('.')
        val = float("." + temp[-1])
        if ans[i] > 0:
            for rev in ans[::-1]:
                base_converted += base16[rev]
        else:
            base_converted += '0'
    return ''.join(reversed(base_converted))

main()