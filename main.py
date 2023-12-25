#import librari and modules
import pandas as pd
import os
#check is there file
if os.path.exists('Roma_best_brother.csv'):
    print("Well done, file found ")#file found
else:
    print("Fail ,file not found")#error
# Download CSV file in DataFrame
df = pd.read_csv('Roma_best_brother.csv', encoding='utf-16')

sum_numb = df['числа_и_цифры'].sum()

#print sum
print("Сумма чисел в колонке 'Числа и цифры':", sum_numb)
