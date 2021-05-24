int analogPin = 3;
int data = 0;
char userInput;

void setup()
{
    Serial.begin(9600); // Инициализация Serial - порта
}

void loop()
{
    if (Serial.available() > 0) // проверяем доступен ли порт
    {
        userInput = Serial.read();
        if (userInput == 'g') // есть запрос
        {
            data = analogRead(analogPin); // читаем аналоговый вход
            Serial.println(data);         // выбрасываем данные
        }
    }
}
