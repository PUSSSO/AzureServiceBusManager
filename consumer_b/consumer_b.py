# consumer_b/consumer_b.py
from azure.servicebus import ServiceBusClient
from shared.config import CONNECTION_STR, CLIENTE_B_QUEUE

def process_cliente_b_messages():
    with ServiceBusClient.from_connection_string(CONNECTION_STR) as client:
        receiver = client.get_queue_receiver(queue_name=CLIENTE_B_QUEUE, max_wait_time=10)
        with receiver:
            for message in receiver:
                print(f"Procesando mensaje: {str(message)}")
                receiver.complete_message(message)

if __name__ == "__main__":
    process_cliente_b_messages()
