def safe_divide(numerator, denominator):
    try:
        # Attempt to convert inputs to floats
        num = float(numerator)
        den = float(denominator)

        try:
            # Attempt the division
            result = num / den
            return f"Result: {result}"
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Both numerator and denominator must be numeric."
