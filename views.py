
import random
import string
from django.shortcuts import render


def generate_password(length=12, include_numbers=True, include_special_chars=True):
    characters = string.ascii_letters
    if include_numbers:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_generator(request):
    # Default values
    password_length = 12
    include_numbers = True
    include_special_chars = True

    # Get user-defined parameters from request
    if 'length' in request.GET and request.GET['length'].isdigit():
        password_length = int(request.GET['length'])
    if 'numbers' in request.GET:
        include_numbers = True
    if 'special_chars' in request.GET:
        include_special_chars = True

    generated_password = generate_password(
        length=password_length,
        include_numbers=include_numbers,
        include_special_chars=include_special_chars
    )

    context = {
        'password': generated_password,
        'length': password_length,
        'include_numbers': include_numbers,
        'include_special_chars': include_special_chars,
    }
    return render(request, 'password_generator/password_generator.html', context)

