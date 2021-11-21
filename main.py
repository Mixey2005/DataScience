import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('StudentsPerformance .csv')
print(df.info())
print('Матеша у девочек:',df[df['gender']=='female']['math score'].mean())
print('Матеша у пацанов:',df[df['gender']=='male']['math score'].mean())
print('Литра у девочек:',df[df['gender']=='female']['reading score'].mean())
print('Литра у пацанов:',df[df['gender']=='male']['reading score'].mean())
print('Письмо у девочек:',df[df['gender']=='female']['writing score'].mean())
print('Письмо у пацанов:',df[df['gender']=='male']['writing score'].mean())
print('---------------------------------------------------------------------')
print('Матеша без хавчика:',df[df['lunch']=='free/reduced']['math score'].mean())
print('Матеша c хавчиком:',df[df['lunch'] == 'standard']['math score'].mean())
print('Письмо без хавчика:',df[df['lunch']=='free/reduced']['writing score'].mean())
print('Письмо c хавчиком:',df[df['lunch'] == 'standard']['writing score'].mean())
print('Литра без хавчика',df[df['lunch']=='free/reduced']['reading score'].mean())
print('Литра с хавчиком',df[df['lunch'] == 'standard']['reading score'].mean())
print('---------------------------------------------------------------------')
df_m = df[df['gender']=='male']['lunch'].value_counts()
df_f = df[df['gender']=='female']['lunch'].value_counts()
standart_m = df_m['standard']
standart_f = df_f['standard']
free_m = df_m['free/reduced']
free_f = df_f['free/reduced']

print('Поевшие пацаны:',standart_m,',','поевшие девочки:',standart_f,',','непоевшие пацаны:',free_m,',','непоевшие девочки',free_f)
print('Отношение количества пацанов к девочкам:',(standart_m+free_m)/(standart_f+free_f))
print('Отношение поевших пацанов к девочкам:',standart_m/standart_f,',','отношение непоевших пацанов к девочкам:',free_m/free_f)
print('Следовательно, пацанов поело меньше чем девочек, поэтому и результаты тестов у пацанов меньше')
print('Исходя из изученных нами данных, можем сказать что пацаны умнее девок в точных науках, а девки в гуманитарных.Также, стоит подметить, что те кто похавали, лучше написали тесты')
df['gender'].value_counts().plot(kind='bar')
plt.show()