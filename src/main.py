from device_factory import DispositivoFactory
from light import Light
from observer import ConcreteObserver
from security_system import SecuritySystem
from smart_home import Home
from thermostat import Thermostat

def mostrar_menu():
    print("\nMenu de Opções:")
    print("1. Listar dispositivos")
    print("2. Adicionar dispositivo")
    print("3. Remover dispositivo")
    print("4. Controlar dispositivo")
    print("5. Dispositivos On")
    print("6. Desligar todas as luzes")
    print("7. Sair")

def listar_dispositivos(home):
    if len(home.devices) == 0:
        print('Não existem dispositivos.')
    else:
        print("\nDispositivos:")
    for i, device in enumerate(home.devices):
        print(f"{i}. {device.status()}")

def adicionar_dispositivo(home, max_devices):
    if len(home.devices) >= max_devices:
        print("Limite de dispositivos atingido!")
        return

    print("\nTipos de dispositivos disponíveis:")
    print("1. Luz")
    print("2. Termostato")
    print("3. Sistema de Segurança")
    print()
    tipo = input("Escolha o tipo de dispositivo (1/2/3): ")
    print()

    if tipo == '1':
        device = DispositivoFactory.create_device('Luz')
    elif tipo == '2':
        device = DispositivoFactory.create_device('Termostato')
    elif tipo == '3':
        device = DispositivoFactory.create_device('SistemaSeguranca')
    else:
        print("Tipo inválido!")
        return

    home.add_device(device)
    print("Dispositivo adicionado com sucesso!")

    observer = ConcreteObserver()
    device.add_observer(observer)

def remover_dispositivo(home):
    listar_dispositivos(home)
    index = int(input("Digite o índice do dispositivo a ser removido: "))

    try:
        home.devices.pop(index)
        print("Dispositivo removido com sucesso.")
    except IndexError:
        print("Índice inválido!")

def controlar_dispositivo(home):
    listar_dispositivos(home)
    index = int(input("Digite o índice do dispositivo a ser controlado: "))

    try:
        device = home.devices[index]
        print(f"Ações disponíveis para {device.__class__.__name__}:")
        if isinstance(device, Light):
            print("1. Ligar")
            print("2. Desligar")
            action = input("Escolha a ação (1/2): ")
            if action == '1':
                device.ligar()
            elif action == '2':
                device.desligar()
            else:
                print("Ação inválida!")
        elif isinstance(device, Thermostat):
            print("1. Aquecer")
            print("2. Esfriar")
            print("3. Desligar")
            action = input("Escolha a ação (1/2/3): ")
            if action == '1':
                device.aquecer()
            elif action == '2':
                device.esfriar()
            elif action == '3':
                device.desligar()
            else:
                print("Ação inválida!")
        elif isinstance(device, SecuritySystem):
            print("1. Armar com gente em casa")
            print("2. Armar sem ninguém em casa")
            print("3. Desarmar")
            action = input("Escolha a ação (1/2/3): ")
            if action == '1':
                device.armar_com_gente_em_casa()
            elif action == '2':
                device.armar_sem_gente_em_casa()
            elif action == '3':
                device.desarmar()
            else:
                print("Ação inválida!")
        print("Ação realizada com sucesso.")
    except IndexError:
        print("Índice inválido!")

def mostrar_total_dispositivos_on(home):
    total_on = home.total_dispositivos_on()
    print(f"Número total de dispositivos ligados: {total_on}")


def main():
    max_devices = int(input("Digite o limite de dispositivos que a casa inteligente pode receber: "))
    home = Home()

    observer = ConcreteObserver()
    for device in home.devices:
        device.add_observer(observer)

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            listar_dispositivos(home)
        elif opcao == '2':
            adicionar_dispositivo(home, max_devices)
        elif opcao == '3':
            remover_dispositivo(home)
        elif opcao == '4':
            controlar_dispositivo(home)
        elif opcao == '5':
            mostrar_total_dispositivos_on(home)
        elif opcao == '6':
            home.desligar_todas_as_luzes()
        elif opcao == '7':
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
