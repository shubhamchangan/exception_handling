
class NoFrontLine(Exception):
    pass

class NoOldAge(Exception):
    pass

ip_1 = input('Are you Front-line worker?-')
ip_2 = input('Age>60?-')
if ip_1!='yes':
    raise NoFrontLine('Sorry U r not Frontline worker so not eligible for booster dose')

elif ip_2!='yes':
    raise NoOldAge('Sorry U r is not >60 so not eligible for booster dose')