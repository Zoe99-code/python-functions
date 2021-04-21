def hotel_cost(nights):
    return nights*140


def plane_ride_cost(city):
    if "Cape_Town" == city:
        return 2500

    elif "Durban" == city:
        return 2300

    elif "Johannesburg" == city:
        return 2000

    else:
        return "The location is not on our database"


def rental_car_cost(days):
    car_cost = 40 * days

    if days >= 7:
        car_cost = car_cost - 50
    elif days >3 and days < 7:
        car_cost = car_cost - 20


def trip_cost(city, days):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city)

location = input("Where did you go:")
days = input("How long were you there:")
cost = input("How much did you spend:")


print(trip_cost(location, days, cost))


