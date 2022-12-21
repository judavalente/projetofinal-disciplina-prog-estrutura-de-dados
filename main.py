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


pc1.addTabelaArp(dispositivos, pc1)
pc1.arp.displayTable()
print("--------------------")
switch1.addTabelaRoteamento(dispositivos, switch2)
switch.tabela_roteamento.displayTable()
