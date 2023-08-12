def stringsplit(stringsplit):
    parts = stringsplit.split('_')
   
    if len(parts) < 3:
        raise ValueError("The input string should contain at least three parts separated by underscores and not spaces or any other symbol")
   
    ans = {
        "name": parts[0].strip(),
        "Domain_name": parts[1].strip(),
        "Regno": "_".join(parts[2:]).strip()
    }
    return ans

a = input("Enter the string with only 3 values with '_' and without the spaces: ")

try:
    b = stringsplit(a)
    print(b)
except ValueError as c:
    print(c)