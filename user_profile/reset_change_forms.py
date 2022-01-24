from wtforms import PasswordField
from wtforms.validators import InputRequired, length, Regexp
from flask_security.forms import ResetPasswordForm, ChangePasswordForm



# Расширил класс ConfirmRegisterForm и переопределил валидацию пароля по современным стандартам
class ExtendedResetForm(ResetPasswordForm):
    password = PasswordField('Пароль: ', validators=[InputRequired(),
                                                     length(min=8, max=255,
                                                            message='Пароль должен быть не менее 8 символов. '),
                                                     Regexp(
                                                         '(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[_@$!%\-*#?&;:"\'])[A-Za-z\d_@$!%\-*#?&;:"\']',
                                                         message=
                                                         'Пароль должен содержать минимум один символ в нижнем регистре, '
                                                         'один в верхнем регистре, цифру, спецсимвол например: _@$!%\-*#?&;:"\' ')])


class ExtendedChangeForm(ChangePasswordForm):
    new_password = PasswordField('Пароль: ', validators=[InputRequired(),
                                                     length(min=8, max=255,
                                                            message='Пароль должен быть не менее 8 символов. '),
                                                     Regexp(
                                                         '(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[_@$!%\-*#?&;:"\'])[A-Za-z\d_@$!%\-*#?&;:"\']',
                                                         message=
                                                         'Пароль должен содержать минимум один символ в нижнем регистре, '
                                                         'один в верхнем регистре, цифру, спецсимвол например: _@$!%\-*#?&;:"\' ')])

