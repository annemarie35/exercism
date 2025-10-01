def is_valid(isbn):
    digits = isbn.replace("-", "")

    if len(digits) == 0 or len(digits) != 10:
        return False

    if (digits[9] not in ('10', '9', '8', '7', '6', '5', '4', '3', '2', '1', '0') or 'X' in digits) and digits[9] != 'X':
        return False

    sum = 0
    for index in (10, 9, 8, 7, 6, 5, 4, 3, 2, 1):
        if digits[index-1] not in ('10', '9', '8', '7', '6', '5', '4', '3', '2', '1', '0') and digits[index-1] != 'X':
            return False
        value = 10 if digits[index-1] == 'X' else int(digits[index-1])
        sum += index * value
    return sum % 11 == 0

# nums = list(isbn.replace("-", ""))
#  if nums[-1] == "X":
#   nums[-1] = "10"
# in ('10', '9', '8', '7', '6', '5', '4', '3', '2', '1', '0') can be replaced by built-in function isdigit()