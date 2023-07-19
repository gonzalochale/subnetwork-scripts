import ipaddress

valid_input = False

while not valid_input:
    cidr = input("Introduce una dirección IP y máscara en formato CIDR: ")
    try:
        direccion = ipaddress.ip_interface(cidr)
        valid_input = True
    except ValueError as e:
        print("Formato incorrecto: {}".format(e))
else:
    red = direccion.network
    broadcast = red.broadcast_address
    ip_disponible_inicial = int(ipaddress.IPv4Address(red.network_address) + 1)
    ip_disponible_final = int(ipaddress.IPv4Address(red.broadcast_address) - 1)
    tamaño = ip_disponible_final - ip_disponible_inicial + 1


    print("Tipo: {}{}".format("IPv6 " if direccion.version == 6 else "", "privada" if direccion.is_private else "pública"))
    print("ID de red: {}".format(red))
    print("Máscara: {}".format(direccion.netmask))
    print("Broadcast: {}".format(broadcast))
    print("1a IP disponible: {}".format(ipaddress.IPv4Address(ip_disponible_inicial)))
    print("Última IP disponible: {}".format(ipaddress.IPv4Address(ip_disponible_final)))
    print("Tamaño: {}".format(tamaño))





