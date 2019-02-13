# Write a function called polysum that takes 2 arguments, n and s. This function should sum the area and square of
# the perimeter of the regular polygon. The function returns the sum, rounded to 4 decimal places.

from math import pi, tan


def polysum(n, s):
    """
    :param n: Number of sides of the polygon
    :param s: The length of the sides
    :return: The sum of the area and sqaure of the perimeter of the polygon, rounded to 4 decimal places.
    """

    # Checking for input errors
    if isinstance(n, int) != True or n <= 2:
        return 'A polygon needs more than 2 sides and be a whole number.'
    if isinstance(s, (int, float)) != True or s <= 0:
        return 'Length of the sides must be a number greater than 0.'

    # Calculating polysum
    area = ((.25*n*s**2)/(tan(pi/n)))
    perimeter = (n*s)

    return round((area + perimeter**2), 4)


print(polysum(5, 3))
