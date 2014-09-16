from django.conf import settings


def get_indicator_details(indicator_code):
    for count, i in enumerate(settings.INDICATORS):
        if indicator_code == i.code:
            return count, i.name

    raise ValueError('Indicator with code {} does not exist'.format(
        indicator_code))
