nombre_cliente = "Melina"
producto = "Pollo a la brasa"
precio_unitario = 45.50
cantidad = 1

total = precio_unitario * cantidad

print("Buen día {}, el detalle de su compra es el siguiente:".format(nombre_cliente))
print("Producto: {}".format(producto))
print("Precio unitario: {:.2f}".format(precio_unitario))
print("Cantidad: {}".format(cantidad))
print("Total a pagar: {:.2f}".format(total))