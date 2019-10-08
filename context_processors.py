from django.conf import settings # import the settings file


def meta(request):
    return {'COMPANY_NAME': settings.COMPANY_NAME,
            'PROJECT_NAME': settings.PROJECT_NAME,
            'MALICIOUS': settings.MALICIOUS,
            'SUSPICIOUS': settings.SUSPICIOUS,
            }

