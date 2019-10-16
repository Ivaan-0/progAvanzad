iva=0.16
propina=0.15

Platillo = input('inserte el nombre del platillo')
total = input('inserte el total del platillo')
Platillo1 = input('inserte el nombre del platillo')
total1 = input('inserte el total del platillo')
Platillo2 = input('inserte el nombre del platillo')
total2 = input('inserte el total del platillo')
Platillo3 = input('inserte el nombre del platillo')
total3 = input('inserte el total del platillo')
Platillo4 = input('inserte el nombre del platillo')
total4 = input('inserte el total del platillo')
print('Pizza y vino', total)

subtotal = total+total1+total2+total3+total4
print('Subtotal', subtotal)

subtotal1 = subtotal*iva
print('IVA',subtotal1)

Subtotal2 = propina*subtotal
print('Propina', subtotal2)

total=subtotal+subtotal1+subtotal2

print('Subtotal' , subtotal)
print('IVA     ' , subtotal1)
print('propina ' , subtotal2)
Print('Total',total)


