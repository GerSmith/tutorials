#!python
# -*- coding: utf-8 -*-

# Пример анимированной визуализации данных с помощью Python и библиотеки moviepy
# на примере распространения COVID-19 в США
# Источник: https://proglib.io/p/animaciya-grafikov-v-python-za-4-shaga-2020-04-27
           
# Секция 1. Импорт библиотек
import pandas as pd
import matplotlib.pyplot as plt
import glob
import moviepy.editor as mpy

# Секция 2. Преобразование данных в датафреймы
# us-states.csv – статистика по случаям заражения
# Источник: репозиторий NY Times GitHub: https://github.com/nytimes/covid-19-data
df = pd.read_csv('us-states.csv', parse_dates=['date'])
# nst-est2019-alldata.csv – данные переписи населения США в 2019
# Источник: сайт переписи населения census.gov: https://www.census.gov/data/tables/time-series/demo/popest/2010s-state-total.html
populations = pd.read_csv('nst-est2019-alldata.csv', usecols=['NAME', 'POPESTIMATE2019'])

# Секция 3. Объединение данных по населению; пересчет на 100 тысяч
df = pd.merge(df, populations, how = 'left', left_on = 'state', right_on = 'NAME')
# вычисляем коэффициент встречаемости COVID-19 на 100 тысяч человек населения
# разделив количество случаев на население штата и умножив на 100 000
df['rate'] = df['cases'] / df['POPESTIMATE2019'] * 100000

# Секция 4. Отбор штатов
# Ограничим наш анализ и отберем штаты с самым высоким коэффициентом заболевших по состоянию на 1 мая 2020
df_0501 = df[df['date'] == '2020-05-01']
topfivestates_rate = list(df_0501.sort_values(by='rate', ascending=False).head()['state'])
# Добавим к ним также Вашингтон и Калифорнию, поскольку у них рано было зарегистрировано большое число случаев заболевания
topfivestates_rate.append('California')
topfivestates_rate.append('Washington')

# Секция 5. Фильтрация датасета
df = df[df['state'].isin(topfivestates_rate)]
# Ограничиваем начало диапазона 1 марта 2020, так как до этой даты случаев заболевания было мало или информация о них неполная
df = df[df['date'] >= '2020-03-01']
df = df.pivot(index = 'date', columns = 'state', values = 'rate')

# Секция 6. Подготовка данных к отображению
# Сбрасываем индекс многоиндексного датафрейма, чтобы обеспечить возможность построения графиков
df = df.reset_index()
# Удаляем столбец даты, т.к. проще отображать динамику относительно количества дней, прошедших с 1 марта 2020 года
df = df.reset_index(drop=True)
df = df.drop(columns = 'date')

# Секция 7. Построение графиков
# Создаем множество png-изображений для разных временных точек. Затем мы просто сошьем их вместе, чтобы получить gif-изображение
plt.style.use('fivethirtyeight')
length = len(df.index)
for i in range(10,length+10):
    ax = df.iloc[:i].plot(figsize=(12,8), linewidth=5, color = ['#173F5F', '#20639B', '#2CAEA3', '#F6D55C', '#ED553B', '#B88BAC', '#827498'])
    ax.set_ylim(0, 2000)
    ax.set_xlabel('Количество дней после 1-го марта 2020 года')
    ax.set_ylabel('Количество случаев на 100,000 человек')
    ax.set_title("Случаи заражения COVID-19 в США на 100,000 человек", fontsize = 18)
    ax.legend(loc='upper left', frameon=False)
    ax.grid(axis='x')
    fig = ax.get_figure()
    fig.savefig(f'.\pngs\{i}.png')

# Секция 8. Генерация GIF
# Превращаем папку с png-картинками в единый анимированный gif
gif_name = 'COVID-19-in-USA.gif'
fps = 5
# Используем пакет glob для создания списка всех png-файлов
file_list = glob.glob('.\pngs\*')
# Создаем gif-файл с помощью moviepy и сохраняем его в текущий каталог
clip = mpy.ImageSequenceClip(file_list, fps=fps)
clip.write_gif('{}.gif'.format(gif_name), fps=fps)
