import requests
import celery

city_id = 520555
appid = "dac2616d8e5455a14eb4125856dd22fb"
app = celery.Celery('Weather', broker='amqp://guest@localhost:5672//')


@app.on_after_configure.connect
def setup_periodic_tasks(sender,**kwargs):
    sender.add_periodic_task(5, current_weather.s(), name='celery')


@app.task()
def current_weather():
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                           params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()
        print("За окном:", data['weather'][0]['description'])
        print("Температура от:", data['main']['temp_min'], "до", data['main']['temp_max'], "°С")
        print("Средняя температура:", data['main']['temp'], "°С")
    except Exception as exeption_text:
        print("Exception (weather):", exeption_text)
        pass


if __name__ == '__main__':
    app.worker_main()
