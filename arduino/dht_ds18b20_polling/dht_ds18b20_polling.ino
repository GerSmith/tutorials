#include <OneWire.h>           // библиотека для работы с протоколом 1-Wire
#include <DallasTemperature.h> // библиотека для работы с датчиком DS18B20
#include <DHT.h>               // библиотека для работы с датчиком DHT

#define ONE_WIRE_BUS 2 // сигнальный провод датчика DS18B20
#define DHTPIN 3       // пин для подключения датчика DHT
#define DHTTYPE DHT11  // тип датчика DHT
#define LED_BUILTIN 13 // пин для светодиода "АВАРИЯ"

OneWire oneWire(ONE_WIRE_BUS);       // создаём объект для работы с библиотекой OneWire
DallasTemperature sensors(&oneWire); // создадим объект для работы с библиотекой DallasTemperature
DeviceAddress *sensorsUnique;        // создаём указатель массив для хранения адресов датчиков
DHT dht(DHTPIN, DHTTYPE);            // создание экземпляра объекта DHT

int countSensors; // количество датчиков на шине
char userInput;   // переменная хранит запрос пользователя

void setup()
{
    pinMode(LED_BUILTIN, OUTPUT); // Инициализация светодиода АВАРИЯ
    Serial.begin(9600);           // подключение последовательного порта
    while (!Serial)
        ; // ожидаем открытия Serial-порта

    sensors.begin();                                 // начинаем работу с датчиками DS18B20
    countSensors = sensors.getDeviceCount();         // выполняем поиск устройств на шине
    sensorsUnique = new DeviceAddress[countSensors]; // выделяем память в динамическом массиве под количество обнаруженных сенсоров
    for (int i = 0; i < countSensors; i++)           // делаем запрос на получение адресов датчиков
    {
        sensors.getAddress(sensorsUnique[i], i);
    }
    for (int i = 0; i < countSensors; i++) // устанавливаем разрешение всех датчиков в 12 бит
    {
        sensors.setResolution(sensorsUnique[i], 12);
    }
    dht.begin(); // запуск датчика DHT
}

void loop()
{
    float temperature[10];              // переменная для хранения температуры с датчиками DS18B20
    float dhtT = dht.readTemperature(); // получение данных температуры сенсора DHT
    float dhtH = dht.readHumidity();    // получение данных влажности сенсора DHT

    sensors.requestTemperatures(); // считываем данные из регистра каждого датчика DS18B20 по очереди
    for (int i = 0; i < countSensors; i++)
    {
        temperature[i] = sensors.getTempCByIndex(i);
    }

    if (isnan(dhtT) || isnan(dhtH)) // Проверка работоспособности сенсора DHT
    {
        //Serial.println("Error DHT sensor"); // Вывод в последовательный порт ошибки
        digitalWrite(LED_BUILTIN, HIGH); // Зажигаем встроенный светодиод
        //delay(1000);                     // ждем
    }
    else
    {
        digitalWrite(LED_BUILTIN, LOW); // Если всё хорошо светодиод не горит
    }

    userInput = Serial.read(); // опрашиваем Serial-порт
    if (userInput == 'g')      // есть запрос извне
    {
        Serial.print(dhtT); // выбрасываем в порт температуру с DHT
        Serial.print(" ");
        Serial.print(dhtH);                    // выбрасываем в порт влажность с DHT
        for (int i = 0; i < countSensors; i++) // выводим температуру в Serial-порт по каждому датчику DS18B20
        {
            Serial.print(" ");
            Serial.print(temperature[i]);
        }
        Serial.println();
    }
}
