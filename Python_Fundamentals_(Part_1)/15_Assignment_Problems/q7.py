'''
# Q7. Ask the user for a temperature in Celsius (string input). Convert it to float, 
then calculate and print temperature in Fahrenheit.

Conversion formula : FahrenheitTemp = (CelsiusTemp * (9 / 5)) + 32
'''

celsiusTemp = float (input("enter temp in celsius : "))

fahrenheitTemp = (celsiusTemp * (9 / 5)) + 32

print(f"Temperature in Fahrenheit is : {fahrenheitTemp}")