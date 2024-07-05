import pymysql


class Pedido:
    def __init__(self, registro):
        self.id= registro.get('id')
        self.cliente= registro.get('cliente')
        self.descripcion= registro.get('descripcion')
        self.estado= registro.get('estado')

class Usuario:
    def __init__(self, registro):
        if type(registro) == tuple: 
            self.nombre = registro[1]
            self.correo = registro[2]
            self.telefono = registro[4]
            self.ciudad = registro[5]
            self.direccion = registro[6]
        else:
            self.nombre = registro.get('nombre')
            self.correo = registro.get('correo')
            self.telefono = registro.get('telefono')
            self.ciudad = registro.get('ciudad')
            self.direccion = registro.get('direccion')
        
            

class Administrador(Usuario):
    def __init__(self, registro):
        super().__init__(registro)
        self.lista_clientes = []

    def mostrar_clientes(self):
        pass

    def mostrar_pedidos_cliente_seleccionado(self, cliente_seleccionado):
        pass
    
    def marcar_pedido_en_camino(self, pedido_id):
        pass
    def to_dict(self):
        return {
            'nombre': self.nombre,
            'correo': self.correo,
            'direccion' : self.direccion,
            'telefono': self.telefono,
            'ciudad' : self.ciudad,
            'listaClientes' : self.lista_clientes,
        }

class Cliente(Usuario):
    def __init__(self, registro):
        super().__init__(registro)
        if type(registro) == tuple: 
            self.id = registro[0]
        else:
            self.id = registro.get('id')
        self.lista_pedidos =[]

    def hacer_pedido(self, datos_pedido):
        pass
    
    def mostrar_pedidos(self):
        print(f"Número de Cliente: {self.numero_cliente}")
    
    def cancelar_pedido(self):
        pass
    
    def confirmar_pedido_enviado(self, id_pedido):
        pass
    def to_dict(self):
        return {
            'nombre': self.nombre,
            'correo': self.correo,
            'direccion' : self.direccion,
            'telefono': self.telefono,
            'ciudad' : self.ciudad,
            'listaPedidos' : self.lista_pedidos,
        }

