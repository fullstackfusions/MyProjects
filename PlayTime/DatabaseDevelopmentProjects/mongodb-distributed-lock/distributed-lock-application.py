from pymongo._mongo_client import MongoClient
# import DistributedLock from other file

class FrontendHandler():

    def __init__(self):
        # initialize the web cient for chatbot
        self._cisco = ""# creating web client for cisco
        self.kafka = KafkaHandler()
        self._mongo_client = MongoClient('mongodb://localhost:27017/')
        self._mongodb_dlock = DistributedLock(self._mongo_client, 'netops')

    def handle_text_request(self, event):
        if self._mongodb_dlock.acquire(event.id):
            try:
                if event.roomType in ['direct']:
                    message = Message(
                        id = event.id,
                        channel = Channel(
                            room_id = event.roomId
                        ),
                        user = Person(
                            email = event.email
                        ),
                        client_type = ClientType.CISCO,
                        request_type = MessageType.TEXT,
                        message_state = MessageState.REQUEST,
                        request_payload = TextRequest(
                            text = event.text
                        )
                    )
                self._kafka.send_to_kafka(serialize_message)
                self._mongodb_dlock.release(event.id)
            except:
                print("error")
