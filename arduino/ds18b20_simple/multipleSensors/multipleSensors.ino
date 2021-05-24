// библиотека для работы с протоколом 1-Wire
#include <OneWire.h>
// библиотека для работы с датчиком DS18B20
#include <DallasTemperature.h>

// сигнальный провод датчика
#define ONE_WIRE_BUS 2

// создаём объект для работы с библиотекой OneWire
OneWire oneWire(ONE_WIRE_BUS);
// создадим объект для работы с библиотекой DallasTemperature
DallasTemperature sensors(&oneWire);
// создаём указатель массив для хранения адресов датчиков
DeviceAddress *sensorsUnique;
// количество датчиков на шине
int countSensors;

// функция вывода адреса датчика
void printAddress(DeviceAddress deviceAddress)
{
    for (uint8_t i = 0; i < 8; i++)
    {
        if (deviceAddress[i] < 16)
            Serial.print("0");
        Serial.print(deviceAddress[i], HEX);
    }
}

void setup()
{
    // инициализируем работу Serial-порта
    Serial.begin(9600);
    // ожидаем открытия Serial-порта
    while (!Serial)
        ;
    // начинаем работу с датчиком
    sensors.begin();
    // выполняем поиск устройств на шине
    countSensors = sensors.getDeviceCount();
    Serial.print("Found sensors: ");
    Serial.println(countSensors);
    // выделяем память в динамическом массиве под количество обнаруженных сенсоров
    sensorsUnique = new DeviceAddress[countSensors];

    // определяем в каком режиме питания подключены сенсоры
    if (sensors.isParasitePowerMode())
    {
        Serial.println("Mode power is Parasite");
    }
    else
    {
        Serial.println("Mode power is Normal");
    }

    // делаем запрос на получение адресов датчиков
    for (int i = 0; i < countSensors; i++)
    {
        sensors.getAddress(sensorsUnique[i], i);
    }
    // выводим полученные адреса
    for (int i = 0; i < countSensors; i++)
    {
        Serial.print("Device ");
        Serial.print(i);
        Serial.print(" Address: ");
        printAddress(sensorsUnique[i]);
        Serial.println();
    }
    Serial.println();
    // устанавливаем разрешение всех датчиков в 12 бит
    for (int i = 0; i < countSensors; i++)
    {
        sensors.setResolution(sensorsUnique[i], 12);
    }
}

void loop()
{
    // переменная для хранения температуры
    float temperature[10];
    // отправляем запрос на измерение температуры всех сенсоров
    sensors.requestTemperatures();
    // считываем данные из регистра каждого датчика по очереди
    for (int i = 0; i < countSensors; i++)
    {
        temperature[i] = sensors.getTempCByIndex(i);
    }
    // выводим температуру в Serial-порт по каждому датчику
    for (int i = 0; i < countSensors; i++)
    {
        Serial.print("Device ");
        Serial.print(i);
        Serial.print(" Temp C: ");
        Serial.print(temperature[i]);
        Serial.println();
    }
    Serial.println();
    // ждём одну секунду
    delay(1000);
}
