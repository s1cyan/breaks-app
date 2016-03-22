from django.shortcuts import render
from models import ScheduleBlock


def greeting_page(request):
    """
    Renders the initial page users will see, a register or login page will be
    accessible.

    :param request: None
    :return: greetings.html
    """
    context_dict = {
            'page_title': 'Cacti',
            'slogan': 'We need a slogan.',
            'show_image': True,
            'register_url': '/cacti_app/register',
            'login_url': '/cacti_app/login'
            }
    return render(request, 'greetings.html', context_dict)


def login_page(request):
    """
    Renders the login page for users to sign in.

    :param request: POST
    :return: login.html
    """
    # TODO: Check for GET request and check the database.
    # TODO: Return the render template and route this function to a url.
    # TODO: Authenticate the user and log them in using Django's User model.
    context_dict = {
        'page_title': 'Login',
        'slogan': 'Let\'s get you signed up with this service.',
        'post_registration_url': '/cacti_app/post_registration_url'
    }
    return render(request, 'login-page.html', context_dict)


def register_page(request):
    """
    Renders the registration page and allows the user to create an account.

    :param request: POST
    :return: registration.html
    """
    # TODO: Check for POST request and add the user to the database.
    # TODO: Check if the Username and Email address exists.
    context_dict = {
        'page_title': 'Registration',
        'show_image': False,
        # 'form': form_class,
    }
    return render(request, 'registration.html', context_dict)


def user_email(request, email_id):
    # TODO: What is this for?
    email = 0


def search_page(request):
    context_dict = {'page_title': 'Cacti: Search for friends'}
    return render(request, 'search-page.html', context_dict)


def register_schedule_information(request):
    """
    Renders the form allowing users to register their schedule information.
    This function is mapped with process_sched_info(request).
    :param request: None
    :return: post-registration.html
    """
    # TODO: Check if the user is logged in.
    context_dict = {
            'page_title': 'Update your schedule',
            'schedule_url': '/cacti_app/set-your-schedule',
            'schedule_process': '/cacti_app/process-schedule'
            }

    return render(request, 'post-registration.html', context_dict)


def process_sched_info(request):
    """
    Processes and attempts to validate the form. If the form is correct,
        returns the correct page, otherwise a warning is spit out to the user.
    """
    # TODO: Convert the string to a datetime timefield.
    # TODO: Check if the start time is less than the end time.
    # TODO: Add a schedule description.
    # TODO: Do logic processing, if the form is correct return the user to the
    # right page, if not, spit out error
    post_dict = request.POST
    try:
        schedule_obj = ScheduleBlock.objects.get(
            schedule_name=post_dict['sched_name'],
            start_time=post_dict['start_time'],
            end_time=post_dict['end_time'],
            )
    except:
        print post_dict
