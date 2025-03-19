def Add(numbers):
    if not numbers:
        return 0
    # nums = (int)numbers.split(",")
    # if not nums.isdigit():
    #     raise ValueError("inputs should be integers")
    if ",\n" in numbers:
        raise ValueError("format issue")
    numbers = numbers.replace("\n",",")
    try:
        nums = [int(n) for n in numbers.split(",")]
    except ValueError:
        raise ValueError("inputs must be integers")

    return sum(nums)