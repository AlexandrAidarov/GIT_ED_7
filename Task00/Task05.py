# 5 За день машина проезжает n километров. Сколько дней нужно чтобы проехать m км.

distance = int(input("Сколька машина проезжает в день: "))
route = int(input("Длинна маршрута: "))

days = (distance + route -1) // distance

print(f"Машине потребуется {days} дней")