import ipaddress

bloques = [    ("10.0.0.0/8", "RFC1918 - Bloque privado A"),    ("172.16.0.0/12", "RFC1918 - Bloque privado B"),    ("192.168.0.0/16", "RFC1918 - Bloque privado C")]

for bloque in bloques:
    print("Bloque de red: {}".format(bloque[1]))
    print("Dirección IP y máscara: {}".format(bloque[0]))
    direccion = ipaddress.ip_interface(bloque[0])
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
    print("\n")
