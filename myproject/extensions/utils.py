from . import jalali
from django.utils import timezone


def jalali_convertor(time):

    time = timezone.localtime(time)
    month = {
        1: 'فروردین',
        2: 'اردیبهشت',
        3: 'خرداد',
        4: 'تیر',
        5: 'مرداد',
        6: 'شهریور',
        7: 'مهر',
        8: 'آبان',
        9: 'آذر',
        10: 'دی',
        11: 'بهمن',
        12: 'اسفند',
    }

    time_to_str = "{},{},{}".format(time.year, time.month, time.day)
    time_to_list = list(jalali.Gregorian(time_to_str).persian_tuple())

    for m in range(1, 13):
        if time_to_list[1] == m:
            time_to_list[1] = month[m]
            break

    output = '{} {} {} , ساعت{}:{}'.format(time_to_list[2], time_to_list[1], time_to_list[0], time.hour, time.minute)

    return output
