from multiprocessing.sharedctypes import Value


def windchill(T,V):
    Value = 35.74 + 0.6215 * T- 35.75 * (V**0.16) + 0.4275 * T * (V**0.16)
    return Value
T = float(input('what is the temperature?: '))
Fahrenheit_Celisius = input('Fahrenheit or Celisius F/C?: ')
if Fahrenheit_Celisius.upper() == 'C':
    T = (T*9/5) + 32
for x in range(5, 65, 5):
    V = x 
    value = windchill(T, V)
    print(f'At temperature {T}, and with speed {x} mph, the windchill is {value: .2f}F ')
