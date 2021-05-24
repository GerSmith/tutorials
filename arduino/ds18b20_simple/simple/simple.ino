// библиотека для работы с протоколом 1-Wire
#include <OneWire.h>
// библиотека для работы с датчиком DS18B20
#include <DallasTemperature.h>

// сигнальный провод датчика
#define ONE_WIRE_BUS 2

// создаём объект для работы с библиотекой OneWire
OneWire oneWire(ONE_WIRE_BUS);

// создадим объект для работы с библиотекой DallasTemperature
DallasTemperature sensor(&oneWire);

void setup()
{
    // инициализируем работу Serial-порта
    Serial.begin(9600);
    // начинаем работу с датчиком
    sensor.begin();
    // устанавливаем разрешение датчика от 9 до 12 бит
    sensor.setResolution(12);
}

void loop()
{
    // переменная для хранения температуры
    float temperature;
    // отправляем запрос на измерение температуры
    sensor.requestTemperatures();
    // считываем данные из регистра датчика
    temperature = sensor.getTempCByIndex(0);
    // выводим температуру в Serial-порт
    Serial.print("Temp C: ");
    Serial.println(temperature);
    // ждём одну секунду
    delay(1000);
}
