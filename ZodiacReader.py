#Welcome to the ZodiacReader
#Astrological Signs
#This program displays astrological signs depending on date of birth

#First, prepare, define, and build the Zodiac method
def zoSign(day,month):
#After defining the zodiac method, start checking months and dates
#If certain crieteria are met, then determining the zodiac sign is possible
#So now let's prep for the Driver
    if month == 'January':
        sign = 'Capricorn' if (day < 20) else 'Aquarius'
    elif month == 'February':
        sign = 'Aquarius' if (day < 19) else 'Pisces'
    elif month == 'March':
        sign = 'Pisces' if (day < 21) else 'Aries'
    elif month == 'April':
        sign = 'Aries' if (day < 20) else 'Taurus'
    elif month == 'May':
        sign = 'Taurus' if (day <21) else 'Gemini'
    elif month == 'June':
        sign = 'Gemini' if (day < 21) else 'Cancer'
    elif month == 'July':
        sign = 'Cancer' if (day < 23) else 'Leo'
    elif month == 'August':
        sign = 'Leo' if (day < 23) else 'Virgo'
    elif month == 'September':
        sign = 'Virgo' if (day < 23) else 'Libra'
    elif month == 'October':
        sign = 'Libra' if (day < 23) else 'Scorpio'
    elif month == 'November':
        sign = 'Scorpio' if (day < 22) else 'Sagittarius'
    elif month == 'December':
        sign = 'Sagittarius' if (day < 22) else 'Capricorn'
    print(sign)
#Last thing to do is make Driver code
if __name__== '__main__':
    day = 1
    month = 'May'
    zoSign(day,month)
