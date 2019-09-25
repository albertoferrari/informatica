'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 richiedere i valori delle variabili alfa e beta poi
 scambiare il valore delle due variabili e visualizzarle
'''

alfa = input('alfa: ')
beta = input('beta: ')
#temp = alfa
#alfa = beta
#beta = temp
alfa , beta = beta , alfa
print('alfa=',alfa,'beta=',beta)
