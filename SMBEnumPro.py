#!/usr/bin/env python3
import argparse
import socket
from smb.SMBConnection import SMBConnection

def obtener_info_os(conn):
    sistema_operativo = conn.remote_os
    nombre_servidor = conn.remote_name
    return nombre_servidor, sistema_operativo

def obtener_lista_usuarios(conn):
    usuarios = conn.listUsers()
    return [usuario.name for usuario in usuarios]

def obtener_lista_grupos(conn):
    grupos = conn.listGroups()
    return [grupo.name for grupo in grupos]

def obtener_lista_recursos_compartidos(conn):
    recursos = conn.listShares()
    return [recurso.name for recurso in recursos]

def enumerar_objetivo(objetivo, usuario, contrasena):
    conn = SMBConnection(usuario, contrasena, "SMBEnumPro-", objetivo, use_ntlm_v2=True)
    assert conn.connect(objetivo, 139), "Conexión fallida, tite :c"

    print(f"Esperando mientras enumero viejo{objetivo}...")

    nombre_servidor, sistema_operativo = obtener_info_os(conn)
    print(f"Nombre del servidor mi rey: {nombre_servidor}")
    print(f"Sistema operativo del principe: {sistema_operativo}")

    print("Usuarios mi apacho:")
    usuarios = obtener_lista_usuarios(conn)
    for usuario in usuarios:
        print(f"  {usuario}")

    print(" Los socios (Grupos):")
    grupos = obtener_lista_grupos(conn)
    for grupo in grupos:
        print(f"  {grupo}")
        
    print("El comunismo (Recursos Compartidos):")
    recursos = obtener_lista_recursos_compartidos(conn)
    for recurso in recursos:
        print(f"  {recurso}")

def main():
    parser = argparse.ArgumentParser(description='Enumera información de máquinas Windows utilizando SMB mi apacho.')
    parser.add_argument('objetivo', help='Dirección IP o nombre de host del objetivo papà.')
    parser.add_argument('-u', '--usuario', default='', help='Nombre de usuario para autenticación del rey')
    parser.add_argument('-p', '--contrasena', default='', help='Contraseña para autenticación mi fafa')

    args = parser.parse_args()
    enumerar_objetivo(args.objetivo, args.usuario, args.contrasena)

if __name__ == '__main__':
    main()

