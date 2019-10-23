class Weather:
    # Погода
    def weather_forecast(self):
        print('Погода хорошая? Да(y) || Нет(n)')
        resolution = input()
        if resolution == "y":
            # print('Погода хорошая')
            return True
        elif resolution == "n":
            # print('Погода плохая')
            return False
        else:
            print('Ведите N (если погода плохая) или Y(если погода хорошая)')

class Weather_service:
    # Решение метеослужбы
    def __init__(self, weather):
        self.weather = weather
    
    def weather_service_solution(self, weather):
        if self.weather.weather_forecast() == True:
            print('Погода летная')
            return True
        else:
            print('Погода не летная')
            return False

class Dispatcher:
    # Диспечер
    def __init__(self, weather_service):
        self.weather_service = weather_service
    
    def take_off_clearance(self, weather_service):
        if self.weather_service.weather_service_solution(weather_service.weather):
            # print('Разрешение получено')
            return True
        else:
            # print('Разрешение отклоненно')
            return False

class Engin:
    # Двигатель
    def start_engin(self):
        print('Запустить двигатель? Да(y) || Нет(n)')
        resolution = input()
        if resolution == "y":
            print('Двигатель запущен, удачного полета')
            return True
        elif resolution == "n":
            print('Отмена запуска двигателя')
            return False
        else:
            print('Y или N что сложного?')


class Airplane:
    # самолет
    def __init__(self,  dispatcher): #engin
        self.engin = Engin()
        self.dispatcher = dispatcher

    def dispatcher_start(self, dispatcher):
        if self.dispatcher.take_off_clearance(dispatcher.weather_service):
            print('Диспечер разрешил взлет')
            return True
        else:
            print('Диспечер запретил взлет')
            return False

    def engin_start(self, engin):
        self.engin.start_engin()

class Boing(Airplane):
# Боинг
    def flight_readiness(self):
        print('Начать процедуру запуска? Да(y) || Нет(n)')
        resolution = input()
        if resolution == 'y':
            print('Запрос необходимых данных')
            if airplane.dispatcher_start(airplane.dispatcher) and airplane.engin_start(airplane.engin) == False:
                print('Взлет отменен, не запущены двигатели')

        elif resolution == "n":
            print('Запуск отменен')
        else: 
            print('Y или N что сложного ?')


weather = Weather()
weather_service = Weather_service(weather)
dispatcher = Dispatcher(weather_service)
# engin = Engin()
airplane = Airplane(dispatcher)
boing = Boing(dispatcher)

boing.flight_readiness()
