class NumeroPortasException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class EnderecoMacInvalidoException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class AbsentKeyException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class Entrada:
    __slots__ = ("key", "value")

    def __init__(self, entry_key, entry_value):
        self.key = entry_key
        self.value = entry_value

    def __str__(self):
        return "(" + str(self.key) + ", " + str(self.value) + ")"


class ChainingHashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = list([] for i in range(self.size))

    def hash(self, key):
        return key % self.size

    def put(self, key, data):
        slot = self.hash(key)

        for entry in self.table[slot]:
            if key == entry.key:
                entry.value = data
                return slot

        self.table[slot].append(Entrada(key, data))
        return slot

    def getMac(self, key):
        slot = self.hash(key)
        for i in range(len(self.table[slot])):
            if key == self.table[slot][i].key:
                return self.table[slot][i].value
        else:
            raise AbsentKeyException(f'Chave {key} inexistente na tabela hash')

    def __str__(self):
        info = ""
        for items in self.table:
            if items is None:
                continue
            for entry in items:
                info += str(entry)
            return info

    def __len__(self):
        count = 0
        for i in self.table:
            count += len(i)
        return count

    def keys(self):
        result = []
        for lst in self.table:
            if lst is not None:
                for entry in lst:
                    result.append(entry.key)
        return result

    def contains(self, key):
        entry = self.__locate(key)
        return isinstance(entry, Entrada)

    def __locate(self, key):
        slot = self.hash(key)
        for i in range(len(self.table[slot])):
            if key == self.table[slot][i].key:
                return self.table[slot][i]
        else:
            return None

    def remove(self, key):
        slot = self.hash(key)
        for i in range(len(self.table[slot])):
            if key == self.table[slot][i].key:
                entry = self.table[slot][i]
                del self.table[slot][i]
                return entry
        raise AbsentKeyException(f'Chave {key} não está presente na tabela hash')

    def displayTable(self):
        for items in self.table:
            if len(items) == 0:
                print('None')
                continue
            for entry in items:
                print(f'{entry.value} ', end='')
            print()


class Dispositivo:
    def __init__(self, ip, mac):
        self.__ip = ip
        self.__mac = mac
        
    @property
    def ip(self):
        return self.__ip
    
    @ip.setter
    def ip(self, ip):
        self.__ip = ip

    @property
    def mac(self):
        return self.__mac

    @mac.setter
    def mac(self, mac):
        macsplit = mac.split(":")
        if len(macsplit) < 6:
            raise EnderecoMacInvalidoException("Endereço MAC inválido. Por favor use um endereço válido. ")
        self.__mac = mac

    def __str__(self):
        return "%s" % (self.ip)

    def __hash__(self):
        return hash(self.ip)


class Computador(Dispositivo):
    def __init__(self, nome, ip, mac):
        super().__init__(ip, mac)
        self.nome = nome
        self.arp = ChainingHashTable(6)

    def addTabelaArp(self, grafo, dispositivo_fonte):
        visitados, fila = set(), [dispositivo_fonte]
        listaipvisitados = []
        while fila:
            dispositivo = fila.pop(0)
            if dispositivo.ip not in listaipvisitados:
                listaipvisitados.append(dispositivo.ip)
                dispositivo_fonte.arp.put(hash(dispositivo), dispositivo.mac)
            for vizinho in grafo[dispositivo]:
                if vizinho not in visitados:
                    visitados.add(vizinho)
                    fila.append(vizinho)


class Switch(Dispositivo):
    def __init__(self, ip, mac):
        super().__init__(ip, mac)
        self.__nportas = 4
        self.tabela_roteamento = ChainingHashTable(self.__nportas)

    @property
    def nportas(self):
        return self.__nportas

    @nportas.setter
    def nportas(self, nportas):
        portasvalidas = [4, 8, 16, 24]
        if nportas not in portasvalidas:
            raise NumeroPortasException('Número de portas invalido. Por favor insira um número válido.')
        self.__nportas = nportas

    def addTabelaRoteamento(self, grafo, dispositivo_fonte):
        visitados, fila = set(), [dispositivo_fonte]
        listamacs = []
        while fila:
            dispositivo = fila.pop(0)
            if grafo.existe_aresta(dispositivo_fonte, dispositivo) is True and dispositivo.mac not in listamacs:
                listamacs.append(dispositivo.mac)
                dispositivo_fonte.tabelaroteamento.put(hash(dispositivo), dispositivo.mac)
            for vizinho in grafo[dispositivo]:
                if vizinho not in visitados:
                    visitados.add(vizinho)
                    fila.append(vizinho)

