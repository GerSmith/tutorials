#include "DHT.h"

#define DHTPIN 3      // пин для подключения датчика DHT
#define DHTTYPE DHT11 // тип датчика DHT

DHT dht(DHTPIN, DHTTYPE); // создание экземпляра объекта DHT

#define LED_BUILTIN 13

char userInput;

void setup()
{
    Serial.begin(9600);           // подключение последовательного порта
    dht.begin();                  // запуск датчика DHT
    pinMode(LED_BUILTIN, OUTPUT); // Инициализация светодиода
}

void loop()
{
    float t = dht.readTemperature(); // получение данных температуры
    float h = dht.readHumidity();    // получение данных влажности

    if (isnan(h) || isnan(t)) // Проверка работоспособности сенсора
    {
        Serial.println("Error DHT sensor"); // Вывод в последовательный порт ошибки
        digitalWrite(LED_BUILTIN, HIGH);    // Зажигаем встроенный светодиод
        delay(1000);
    }
    else
    {
        digitalWrite(LED_BUILTIN, LOW); // Если всё хорошо светодиод не горит
    }

    if (Serial.available() > 0) // проверяем доступен ли порт
    {
        userInput = Serial.read();
        if (userInput == 'g') // есть запрос
        {
            Serial.print(t);   // выбрасываем данные
            Serial.print(" "); // выбрасываем данные
            Serial.println(h); // выбрасываем данные
        }
    }
}
