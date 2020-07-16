from marshmallow import ValidationError


def password_validation(user_password):
    min_length = 8
    if len(user_password) < min_length:
        raise ValidationError('Password must contain at least 8 characters.')
    special_symbols = '!@#$%^&*(){}[]/\~?<>+-'
    if not [item for item in user_password if item in special_symbols]:
        raise ValidationError(f'Password must contain at least 1 special symbol: {special_symbols}')
    user_password_upper = user_password.upper()
    if not [item for item in user_password if item.isalpha() and item in user_password_upper]:
        raise ValidationError(f'Password must contain at least 1 capital letter')
