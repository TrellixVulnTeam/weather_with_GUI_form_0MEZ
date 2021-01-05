import eel
from pyowm import OWM
from pyowm.commons.enums import SubscriptionTypeEnum

# ---------- CONFIGURATIONS ---------------------
config = {
    'subscription_type': SubscriptionTypeEnum.FREE,
    'language': 'ru',
    'connection': {
        'use_ssl': True,
        'verify_ssl_certs': True,
        'use_proxy': False,
        'timeout_secs': 5
    },
    'proxies': {
        'http': 'http://user:pass@host:port',
        'https': 'socks5://user:pass@host:port'
    }
}

# ---------- FREE API KEY ---------------------
owm = OWM('e68e5d5d92646e66428b0617f1e53cdd', config = config )

@eel.expose
def get_weather(place):
    mgr = owm.weather_manager()

    observation = mgr.weather_at_place(place)
    w = observation.weather
    temp = w.temperature('celsius')['temp']
    return "В городе " + place + " сейчас " + str(temp) + " градусов по Цельсию. " + w.detailed_status


eel.init("web")
eel.start("main.html", size=(700,700))