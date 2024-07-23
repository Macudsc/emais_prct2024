from django.urls import reverse

def user_profile_url(request):
    if not request.user.is_authenticated:
        return {}

    profile_url = ''
    if request.user.is_superuser:
        profile_url = reverse('admin:index')
    elif request.user.groups.filter(name='patient').exists():
        profile_url = reverse('patient:myinfo')
    elif request.user.groups.filter(name='doctor').exists():
        profile_url = reverse('doctor:myinfo')
    elif request.user.groups.filter(name='administrator').exists():
        profile_url = reverse('administrator:myinfo')

    return {'profile_url': profile_url}