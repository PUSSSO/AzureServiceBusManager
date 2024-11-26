from azure.servicebus import ServiceBusClient, ServiceBusMessage

# Constantes de configuración
CONNECTION_STR = "Endpoint=sb://email-serviciobus.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=JZZ4DGNREDvPEsJqlroacfzoPb+iNkNJY+ASbAZ4858="
QUEUE_NAME = "email-queue"

class AzureServiceBusManager:
    """Gestor de Azure Service Bus para enviar y recibir mensajes."""
    
    def __init__(self, connection_str: str, queue_name: str):
        """Inicializa el gestor con la cadena de conexión y el nombre de la cola."""
        self.connection_str = connection_str
        self.queue_name = queue_name
        self.client = ServiceBusClient.from_connection_string(self.connection_str, logging_enable=True)

    def send_message(self, content: str):
        """Envía un mensaje a la cola."""
        with self.client.get_queue_sender(self.queue_name) as sender:
            message = ServiceBusMessage(content)
            sender.send_messages(message)
            print(f"Mensaje enviado: {content}")

    def receive_messages(self):
        """Recibe mensajes de la cola."""
        with self.client.get_queue_receiver(self.queue_name, max_wait_time=5) as receiver:
            for message in receiver:
                print(f"Mensaje recibido: {str(message)}")
                receiver.complete_message(message)

    def __del__(self):
        """Cierra el cliente cuando ya no es necesario."""
        self.client.close()

# Funcionalidad principal
if __name__ == "__main__":
    service_bus_manager = AzureServiceBusManager(CONNECTION_STR, QUEUE_NAME)

    print("Selecciona una opción:")
    print("1. Enviar mensaje")
    print("2. Recibir mensajes")
    opcion = input("Opción: ")

    if opcion == "1":
        mensaje = input("Escribe el mensaje que deseas enviar: ")
        service_bus_manager.send_message(mensaje)
    elif opcion == "2":
        print("Recibiendo mensajes...")
        service_bus_manager.receive_messages()
    else:
        print("Opción no válida")