from abc import ABC, abstractmethod

# 1. The Product Interface (Abstract Base Class)
# This defines the "blueprint" that all concrete notifications must follow.
class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass

# 2. Concrete Products
# These are the actual implementations of the Notification interface.
class EmailNotification(Notification):
    def send(self, message):
        return f"Sending Email: {message}"

class SMSNotification(Notification):
    def send(self, message):
        return f"Sending SMS: {message}"

# 3. The Factory (The Creator)
# This class centralizes the logic of which object to create.
class NotificationFactory:
    @staticmethod
    def create_notification(notification_type):
        if notification_type == "email":
            return EmailNotification()
        elif notification_type == "sms":
            return SMSNotification()
        else:
            raise ValueError(f"Unknown notification type: {notification_type}")

# --- Usage ---
# The client code doesn't need to know about EmailNotification or SMSNotification classes.
factory = NotificationFactory()

# We don't care which specific class is instantiated; we just ask for a "type".
notif = factory.create_notification("email")

# Result: Sending Email: Hello!
print(notif.send("Hello!"))
