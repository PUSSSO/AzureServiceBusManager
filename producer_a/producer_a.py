# producer_a/producer_a.py
from azure.servicebus import ServiceBusClient, ServiceBusMessage
from shared.config import CONNECTION_STR, GENERAL_QUEUE

def send_message_to_general():
    with ServiceBusClient.from_connection_string(CONNECTION_STR) as client:
        sender = client.get_queue_sender(queue_name=GENERAL_QUEUE)
        with sender:
            message = ServiceBusMessage(
                "Mensaje para cliente A",
                application_properties={"routing_key": "clienteA"}
            )
            sender.send_messages(message)
            print("Mensaje enviado al queue-general con routing_key=clienteA")

if __name__ == "__main__":
    send_message_to_general()
