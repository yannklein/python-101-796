# def even_or_odd(number):
#     """Returns even or odd according to the number passed to it"""
#     if number % 2 == 0:
#         return 'even'
#     else:
#         return 'odd'

def even_or_odd(number):
    """Returns even or odd according to the number passed to it"""
    return 'even' if number % 2 == 0 else 'odd'

print(even_or_odd(32))
print(even_or_odd(33))