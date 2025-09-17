min = int(input('Минуты: '))
hh = min // 60
mm = min - 60 * hh
if mm < 10:
    mm = '0' + str(mm)
print(f'{hh}:{mm}')