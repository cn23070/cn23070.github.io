"""
This basic application simulates communication between IoT devices and a central controller 
to measure the impact of encryption in transit. 
"""

import time  # measure the time taken for message transmission
import random  # generate random encryption keys
import string  # work with ASCII characters for key generation
import pandas as pd  # generating and displaying the results summary table in a human friendly readable format


class IoTDevice:
    """
    Represents an IoT device that can send encrypted and unencrypted messages to a controller.
    """

    def __init__(self, device_id):
        """
        Initializes an IoT Device instance with a unique device ID and generates an encryption key.

        :param device_id: Unique identifier for the IoT device.
        """
        self.device_id = device_id  # Store the unique device ID
        self.key = self.generate_key()  # Generate a random encryption key for the device

    def generate_key(self):
        """
        Generates an 8-character encryption key composed of random letters and digits.

        :return: A string representing the encryption key.
        """
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))

    def encrypt_message(self, message):
        """
        Encrypts the given message using a simple XOR encryption technique with the device's key.

        :param message: The plain text message to encrypt.
        :return: The encrypted message as a string.
        """
        encrypted_message = ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(message, self.key))
        return encrypted_message  # Return the encrypted message

    def decrypt_message(self, encrypted_message):
        """
        Decrypts the given encrypted message using the device's key.

        :param encrypted_message: The message to decrypt.
        :return: The decrypted message as plain text.
        """
        decrypted_message = ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(encrypted_message, self.key))
        return decrypted_message  # Return the decrypted message

    def send_message(self, message, controller, encrypted=True):
        """
        Sends a message from the IoT device to the central controller, optionally encrypting it.

        :param message: The message to send.
        :param controller: The controller to receive the message.
        :param encrypted: A boolean flag indicating whether to encrypt the message (default is True).
        """
        if encrypted:
            encrypted_message = self.encrypt_message(message)
            print(f"Device {self.device_id} sending encrypted message...")

            intercepted = controller.intercept_message(encrypted_message, encrypted=True)

            start_time = time.time()
            controller.receive_message(encrypted_message, self, encrypted=True)
            end_time = time.time()
        else:
            print(f"Device {self.device_id} sending plain message...")

            intercepted = controller.intercept_message(message, encrypted=False)

            start_time = time.time()
            controller.receive_message(message, self, encrypted=False)
            end_time = time.time()

        time_taken = end_time - start_time

        controller.log_message(
            device_id=self.device_id,
            message=message if not encrypted else encrypted_message,
            encrypted=encrypted,
            intercepted=intercepted,
            time_taken=time_taken
        )


class Controller:
    """
    Manages communication with IoT devices and logs message transmissions.
    """

    def __init__(self):
        """
        Initializes a Controller instance, which will manage communication with IoT devices.
        """
        self.message_log = []  # Initialize an empty list to log details of each transmitted message

    def receive_message(self, message, device, encrypted=True):
        """
        Receives a message from an IoT device and optionally decrypts it.

        :param message: The message received (either plain or encrypted).
        :param device: The IoT device that sent the message.
        :param encrypted: A boolean flag indicating whether the message is encrypted.
        """
        if encrypted:
            decrypted_message = device.decrypt_message(message)
            print(f"Controller received encrypted message: {message} (decrypted: {decrypted_message})")
        else:
            print(f"Controller received plain text message: {message}")

    def intercept_message(self, message, encrypted=True):
        """
        Simulates interception of a message by an attacker.

        :param message: The message to intercept (either plain or encrypted).
        :param encrypted: A boolean flag indicating whether the message is encrypted.
        :return: True, indicating the message was intercepted.
        """
        if encrypted:
            print(f"\n[ATTACKER] Intercepted encrypted message: {message}")
            print("[ATTACKER] Attacker failed to decrypt the message without the key.\n")
        else:
            print(f"\n[ATTACKER] Intercepted plain text message: {message}")
            print("[ATTACKER] Attacker successfully read the message.\n")
        return True  # Indicate that the message was intercepted

    def log_message(self, device_id, message, encrypted, intercepted, time_taken):
        """
        Logs details of each transmitted message, including device ID, message content, and transmission statistics.

        :param device_id: ID of the device that sent the message.
        :param message: The content of the message (plain text or encrypted).
        :param encrypted: Whether the message was encrypted.
        :param intercepted: Whether the message was intercepted.
        :param time_taken: The time taken to transmit the message.
        """
        self.message_log.append({
            'Device ID': device_id,
            'Message': message,
            'Encrypted': encrypted,
            'Intercepted': intercepted,
            'Time Taken (s)': time_taken
        })

    def print_summary(self):
        """
        Prints a summary table of all messages logged during the simulation, including encryption and interception status.
        """
        df = pd.DataFrame(self.message_log)
        print("\n--- Summary Table ---")
        print(df)  # Display the summary table


def simulate_devices(device_count, controller, encrypted=True):
    """
    Simulates multiple IoT devices sending messages to the controller, with optional encryption.

    :param device_count: The number of IoT devices to simulate.
    :param controller: The controller that receives the messages.
    :param encrypted: A boolean flag to indicate whether to encrypt the messages.
    """
    devices = [IoTDevice(device_id=i) for i in range(1, device_count + 1)]

    for device in devices:
        message = f"Hi Controller! This is device {device.device_id}"
        device.send_message(message, controller, encrypted=encrypted)


if __name__ == "__main__":
    # Initialize the controller
    controller = Controller()

    # Specify the number of IoT devices to simulate. Default is 10 but this can be changed.
    DEVICE_COUNT = 20

    # Simulate devices sending plain messages
    print("Simulation with plain messages:")
    simulate_devices(DEVICE_COUNT, controller, encrypted=False)

    # Simulate devices sending encrypted messages
    print("\nSimulation with encrypted messages:")
    simulate_devices(DEVICE_COUNT, controller, encrypted=True)

    # Print the summary of all messages transmitted
    controller.print_summary()

