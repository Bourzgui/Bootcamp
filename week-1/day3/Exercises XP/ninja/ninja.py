class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []   
        self.messages = []       
    
    def call(self, other_phone):
    
        call_info = f"{self.phone_number} a appelé {other_phone.phone_number}"
        print(call_info)
        self.call_history.append(call_info)
    
    def show_call_history(self):
        print("\nHistorique des appels:")
        for call in self.call_history:
            print(call)
    
    def send_message(self, other_phone, content):
        
        message = {
            "to": other_phone.phone_number,
            "from": self.phone_number,
            "content": content
        }     
        self.messages.append(message)
        other_phone.messages.append(message)
    
    def show_outgoing_messages(self):
        print("\nMessages envoyés:")
        for message in self.messages:
            if message["from"] == self.phone_number:
                print(f"À: {message['to']} | Message: {message['content']}")
    
    def show_incoming_messages(self):
        print("\nMessages reçus:")
        for message in self.messages:
            if message["to"] == self.phone_number:
                print(f"De: {message['from']} | Message: {message['content']}")
    
    def show_messages_from(self, phone_number):
        print(f"\nMessages de {phone_number}:")
        for message in self.messages:
            if message["from"] == phone_number and message["to"] == self.phone_number:
                print(f"Message: {message['content']}")

if __name__ == "__main__":
    phone1 = Phone("123-456-789")
    phone2 = Phone("987-654-321")
    
    phone1.call(phone2)
    phone2.call(phone1)
    phone1.call(phone2)
     
    phone1.show_call_history()
   
    phone1.send_message(phone2, "Bonjour! Comment vas-tu?")
    phone2.send_message(phone1, "Très bien, merci! Et toi?")
    phone1.send_message(phone2, "Tout va bien!")
    print("\nTest des messages pour phone1:")
    phone1.show_outgoing_messages()
    phone1.show_incoming_messages()
    phone1.show_messages_from("987-654-321")
    
    print("\nTest des messages pour phone2:")
    phone2.show_outgoing_messages()
    phone2.show_incoming_messages()
    phone2.show_messages_from("123-456-789")