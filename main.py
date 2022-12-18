from dispositivos import Computador, Switch, Grafo
from time import sleep

pc1 = Computador("PC1", "192.168.0.12", "77:87:01:0C:1E:A6")
pc2 = Computador("PC2", "192.168.0.10", "41:12:96:A0:E2:7E")
pc3 = Computador("PC3", "192.168.1.12", "5B:6E:F0:09:33:19")
pc4 = Computador("PC4", "192.168.1.10", "13:84:69:E4:01:59")
switch1 = Switch(12, "192.168.0.11", "38:A4:65:A6:61:5C")
switch2 = Switch(12, "192.168.1.2", "02:E7:74:AC:49:93")
conexoes = [(pc1, switch1), (pc2, switch1), (switch1, switch2), (pc3, switch2), (pc4, switch2)]
dispositivos = (Grafo(conexoes, direcionado=False))


def getArp(grafo, dispositivo_fonte):
    visitados, fila = set(), [dispositivo_fonte]
    while fila:
        vertice = fila.pop(0)
        dispositivo_fonte.arp.put(hash(vertice), vertice)
        for vizinho in grafo[vertice]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(vizinho)


def getIp


def ping(dispositivo, dispositivofinal):
    e = 0
    r = 0
    p = 0
    erro = 0
    print(f"Disparando {dispositivofinal.ip} com 32 bytes de dados:")
    for pacotes in range(4):
        if dispositivos.existe_aresta(dispositivo, dispositivofinal) is True:
            sleep(1)
            e += 1
            r += 1
            erro = p / e * 100
            print(f"Resposta de {dispositivofinal.ip}: bytes=32 tempo=16ms TTL=64")
        else:
            e += 1
            p += 1
            erro = p / e * 100
            sleep(1)
            print("Esgotado o tempo limite do pedido.")
    print(f"Estatísticas do Ping para {dispositivofinal.ip}: ")
    print(f"Pacotes: Enviados = {e}, Recebidos = {r}, Perdidos = {p} ({erro}% de perda),")
    print("Aproximar um número redondo de vezes em milissegundos: Mínimo = 2ms, Máximo = 34ms, Média = 11ms")


getArp(dispositivos, pc1)
pc1.arp.displayTable()
