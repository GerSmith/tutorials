
int analogPin = 3;
int data = 0;

void setup()
{
    Serial.begin(9600); // Инициализация Serial - порта
}

void loop()
{
    data = analogRead(analogPin); // читаем аналоговый вход
    Serial.println(data);         // выбрасываем данные
    delay(1000);                  // ждем
}
