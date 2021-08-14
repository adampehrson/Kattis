mates = int(input())

for x in range(mates):
    data = input().split()
    day = int(data[0])
    month = data[1]


    if month == 'Dec':
        astro_sign = 'Sagittarius' if (day < 22) else 'capricorn'
    elif month == 'Jan':
        astro_sign = 'Capricorn' if (day < 21) else 'aquarius'
    elif month == 'Feb':
        astro_sign = 'Aquarius' if (day < 20) else 'pisces'
    elif month == 'Mar':
        astro_sign = 'Pisces' if (day < 21) else 'aries'
    elif month == 'Apr':
        astro_sign = 'Aries' if (day < 21) else 'taurus'
    elif month == 'May':
        astro_sign = 'Taurus' if (day < 21) else 'gemini'
    elif month == 'Jun':
        astro_sign = 'Gemini' if (day < 22) else 'cancer'
    elif month == 'Jul':
        astro_sign = 'Cancer' if (day < 23) else 'leo'
    elif month == 'Aug':
        astro_sign = 'Leo' if (day < 23) else 'virgo'
    elif month == 'Sep':
        astro_sign = 'Virgo' if (day < 22) else 'libra'
    elif month == 'Oct':
        astro_sign = 'Libra' if (day < 23) else 'scorpio'
    elif month == "Nov":
        astro_sign = 'scorpio' if (day < 23) else 'sagittarius'

    print(astro_sign[0].upper() + astro_sign[1:])
