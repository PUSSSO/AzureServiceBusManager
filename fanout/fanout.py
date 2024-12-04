# fanout/fanout.py
from azure.servicebus import ServiceBusClient, ServiceBusMessage
from shared.config import CONNECTION_STR, CLIENTE_A_QUEUE, CLIENTE_B_QUEUE

def fanout_message(content):
    queues = [CLIENTE_A_QUEUE, CLIENTE_B_QUEUE]
    with ServiceBusClient.from_connection_string(CONNECTION_STR) as client:
        for queue in queues:
            sender = client.get_queue_sender(queue_name=queue)
            with sender:
                sender.send_messages(ServiceBusMessage(content))
                print(f"Mensaje enviado a {queue}")

if __name__ == "__main__":
    fanout_message("Notificación global para todos los clientes")
