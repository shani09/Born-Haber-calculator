#Shows introduction message:
print '''Hello! Welcome to the Born-Haber calculator!

The calculator allows you to find one of the following values given all the other values:
-lattice enthalpy
-enthalpy of formation
-enthalpy of atomisation of first element
-enthalpy of atomisation of second element
-first electron affinity
-second electron affinity
-first ionisation energy
-second ionisation energy

Please note that you must type the name of the value exactly the way it is written above.

Remember to alter the value of the atomisation according to the number of moles of the element.

If there is only one electron affinity or one ionisation energy, set the values of the second electron affinity and second ionisation energy to 0.

This program was created by Shani Bendor, a high school student, 22/4/2015.
_________________________________________
'''

#Defines all value names to variables
a1 = 'lattice enthalpy'
b1 = 'enthalpy of formation'
c1 = 'enthalpy of atomisation of first element'
d1 = 'enthalpy of atomisation of second element'
e1 = 'first electron affinity'
f1 = 'second electron affinity'
g1 = 'first ionisation energy'
h1 = 'second ionisation energy'

#Gets all raw inputs                
def raw_inp(var_name):
        #var_value = var_name.replace(' ', '_')
        y = raw_input('Enter value for ' + var_name + ': ' )
        if (var_name == b1 or var_name == f1 or var_name == e1) and float(y) <= 0:
          return float(y)
        elif (var_name == b1 or var_name == f1 or var_name == e1) and float(y) >= 0:
          print var_name + ' must be a negative value'
          return raw_inp(var_name)           
        elif (var_name == a1 or var_name == c1 or var_name == d1 or var_name == g1 or var_name == h1) and float(y) >= 0:
          return float(y)
        elif var_name == (a1 or c1 or d1 or g1 or h1) and float(y) <= 0:
          print var_name + ' must be a positive value'
          return float(raw_inp(var_name))     
        else:
          print 'Please make sure you are typing in a number' 
          return float(raw_inp(var_name))  

#runs raw_inp function then prints the value
def run_value(var_name):
    x = raw_inp(var_name)
    #print 'Value for ' + var_name + ': ' + str(x)
    if var_name == g1 or var_name == h1 or var_name == e1 or var_name == f1 or \
    var_name == c1 or var_name == d1:
        x = x * -1
    return x

#Asks user which value they would like to find
unknown_value = raw_input('Enter the name of the value you would like to find here: ')

#Asks user to input all of the missing values and calculates unknown value
vars_list = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8']
value_names = [a1, b1, c1, d1, e1, f1, g1, h1]
sum_values = 0
for value_name in value_names:
  if value_name == unknown_value:
    y = 0
  else:
    y = run_value(value_name)
  sum_values = sum_values + y
     
#Modifies the value of the sum
if unknown_value == a1 or unknown_value == b1:
  sum_values = sum_values * -1
print ' '
print 'The value for ' + unknown_value + ' is ' + str(sum_values) + ' kJ/mol'
print 'To calculate another value, re-run the program'