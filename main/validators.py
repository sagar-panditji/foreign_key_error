from django.core.exceptions import ValidationError


def validate_even_number(value):
    if value % 2:
        raise ValidationError("Not Eligible")
