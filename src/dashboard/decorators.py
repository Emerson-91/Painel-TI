from django.contrib.auth.decorators import user_passes_test


def admin_required(function):
    return user_passes_test(lambda u: u.is_active and u.is_staff, login_url='/login/')(function)
