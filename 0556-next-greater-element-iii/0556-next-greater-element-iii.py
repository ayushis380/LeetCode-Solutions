class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))  # Convert the number to a list of digits
        length = len(digits)

        # Step 1: Find the first decreasing digit from the right
        i = length - 2
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1

        if i == -1:
            return -1  # Digits are in descending order; no greater number possible

        # Step 2: Find the smallest digit on the right of i that is greater than digits[i]
        j = length - 1
        while digits[j] <= digits[i]:
            j -= 1

        # Step 3: Swap the found digits
        digits[i], digits[j] = digits[j], digits[i]

        # Step 4: Reverse the suffix (everything after position i)
        digits[i + 1:] = reversed(digits[i + 1:])

        # Step 5: Convert back to integer
        result = int(''.join(digits))

        # Step 6: Check if it fits in 32-bit signed integer
        return result if result <= 2**31 - 1 else -1
