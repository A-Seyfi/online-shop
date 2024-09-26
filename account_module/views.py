from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .models import User
from django.utils.crypto import get_random_string
from django.http import Http404, HttpRequest
from django.contrib.auth import login, logout
from utils.sms_service import send_sms

from account_module.forms import RegisterForm, LoginForm, ForgotPasswordForm, ResetPasswordForm


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        context = {
            'register_form': register_form
        }

        return render(request, 'account_module/register.html', context)

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_email = register_form.cleaned_data.get('email')
            user_password = register_form.cleaned_data.get('password')
            user_phone = register_form.cleaned_data.get('phone_number')
            user: bool = User.objects.filter(email__iexact=user_email).exists()
            if user:
                register_form.add_error('email', 'ایمیل وارد شده تکراری می باشد')
            else:
                new_user = User(
                    email=user_email,
                    email_active_code=get_random_string(72),
                    is_active=True,
                    username=user_email,
                    phone_number=user_phone,
                )
                new_user.set_password(user_password)
                new_user.save()

                # activation_code = new_user.email_active_code
                # send_sms(str(user_phone), str(activation_code), int(252794))

                return redirect(reverse('login_page'))

        context = {
            'register_form': register_form
        }
        return render(request, 'account_module/register.html', context)


class ActivateAccountView(View):
    def get(self, request):
        return render(request, 'account_module/activate_account.html')

    def post(self, request):
        activation_code = request.POST.get('activation_code')
        user: User = User.objects.filter(email_active_code__iexact=activation_code).first()
        if user is not None:
            if not user.is_active:
                user.is_active = True
                user.email_active_code = get_random_string(72)
                user.save()
                return redirect(reverse('login_page'))
            else:
                pass

        raise Http404


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        context = {
            'login_form': login_form
        }
        return render(request, 'account_module/login.html', context)

    def post(self, request: HttpRequest):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get('email')
            user_pass = login_form.cleaned_data.get('password')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                if not user.is_active:
                    login_form.add_error('email', 'حساب کاربری شما فعال نشده است')
                else:
                    is_password_correct = user.check_password(user_pass)
                    if is_password_correct:
                        login(request, user)
                        return redirect(reverse('profile_page'))
                    else:
                        login_form.add_error('email', 'کلمه عبور اشتباه است')
            else:
                login_form.add_error('email', 'کاربری با مشخصات وارد شده یافت نشد')

        context = {
            'login_form': login_form
        }
        return render(request, 'account_module/login.html', context)


class ForgetPasswordView(View):
    def get(self, request: HttpRequest):
        forget_pass_form = ForgotPasswordForm()
        context = {'forget_pass_form': forget_pass_form}
        return render(request, 'account_module/forgot_password.html', context)

    def post(self, request: HttpRequest):
        forget_pass_form = ForgotPasswordForm(request.POST)
        if forget_pass_form.is_valid():
            user_phone = forget_pass_form.cleaned_data.get('phone_number')
            user: User = User.objects.filter(phone_number__iexact=user_phone).first()
            if user is not None:
                reset_code = get_random_string(6, allowed_chars='0123456789')
                send_sms(str(user_phone), str(reset_code), int(252794))

                user.reset_code = reset_code
                user.save()

                return redirect(reverse('reset_password_page'))

        context = {'forget_pass_form': forget_pass_form}
        return render(request, 'account_module/forgot_password.html', context)


class ResetPasswordView(View):
    def get(self, request: HttpRequest):
        reset_pass_form = ResetPasswordForm()
        context = {
            'reset_pass_form': reset_pass_form,
        }
        return render(request, 'account_module/reset_password.html', context)

    def post(self, request: HttpRequest):
        reset_pass_form = ResetPasswordForm(request.POST)
        reset_code = request.POST.get('reset_code')
        user: User = User.objects.filter(reset_code__iexact=reset_code).first()

        if reset_pass_form.is_valid():
            if user is None:
                return redirect(reverse('login_page'))

            user_new_pass = reset_pass_form.cleaned_data.get('password')
            user.set_password(user_new_pass)
            user.reset_code = get_random_string(72)
            user.is_active = True
            user.save()
            return redirect(reverse('login_page'))

        context = {
            'reset_pass_form': reset_pass_form,
            'user': user
        }

        return render(request, 'account_module/reset_password.html', context)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('login_page'))