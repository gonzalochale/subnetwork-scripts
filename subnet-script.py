import ipaddress

# Pedir al usuario que ingrese la dirección de red CIDR y el número de bits para las subredes
cidr = input("Ingresa la dirección de red CIDR (p.ej. 192.168.0.0/24): ")
num_bits = int(input("Ingresa el número de bits para las subredes: "))

# Convertir la dirección de red CIDR a un objeto de la clase ipaddress.IPv4Network
red = ipaddress.IPv4Network(cidr)

# Hacer el subneteo
subredes = list(red.subnets(new_prefix=num_bits))

# Imprimir las subredes creadas
print("Las subredes creadas son: ")
for subred in subredes:
    print(subred)
