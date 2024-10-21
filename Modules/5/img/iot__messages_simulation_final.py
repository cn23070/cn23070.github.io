import time  # measure the time taken for message transmission
import random  # generate random encryption keys
import string  # work with ASCII characters for key generation
import pandas as pd  # generating and displaying the results summary table in a human friendly readable format


class IoTDevice:
    def __init__(self, device_id):
        """
        Initializes an IoT Device instance with a unique device ID and generates an encryption key.
        """
        self.device_id = device_id  # Store the unique ID for this device
        self.key = self.generate_key()  # Generate a random encryption key for the device

    def generate_key(self):
        """
        Generates an 8-character encryption key composed of random letters and digits.
        """
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))  # Return a random 8-character key

    def encrypt_message(self, message):
        """
        Encrypts the given message using a simple XOR encryption technique with the device's key.
        :return: The encrypted message as a string.
        """
        # XOR each character of the message with the corresponding character of the key
        encrypted_message = ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(message, self.key))
        return encrypted_message  # Return the encrypted message

    def decrypt_message(self, encrypted_message):
        """
        Decrypts the given encrypted message using the device's key.
        :return: The decrypted message as plain text.
        """
        # XOR the encrypted message with the key to retrieve the original message
        decrypted_message = ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(encrypted_message, self.key))
        return decrypted_message  # Return the decrypted message

    def send_message(self, message, controller, encrypted=True):
        """
        Sends a message from the IoT device to the central controller, optionally encrypting it.
        """
        if encrypted:
            # If encryption is enabled, encrypt the message before sending
            encrypted_message = self.encrypt_message(message)
            print(f"Device {self.device_id} sending encrypted message...")

            # Simulate message interception by an attacker
            intercepted = controller.intercept_message(encrypted_message, encrypted=True)

            # Measure the time taken to send the message to the controller
            start_time = time.time()
            controller.receive_message(encrypted_message, self, encrypted=True)
            end_time = time.time()
        else:
            # If encryption is not enabled, send the plain message
            print(f"Device {self.device_id} sending plain message...")

            # Simulate message interception by an attacker
            intercepted = controller.intercept_message(message, encrypted=False)

            # Measure the time taken to send the plain message to the controller
            start_time = time.time()
            controller.receive_message(message, self, encrypted=False)
            end_time = time.time()

        # Calculate the time taken to transmit the message
        time_taken = end_time - start_time

        # Log the message transmission details in the controller's log
        controller.log_message(
            device_id=self.device_id,
            message=message if not encrypted else encrypted_message,
            encrypted=encrypted,
            intercepted=intercepted,
            time_taken=time_taken
        )


class Controller:
    def __init__(self):
        """
        Initializes a Controller instance, which will manage communication with IoT devices.
        """
        self.message_log = []  # Initialize an empty list to log details of each transmitted message

    def receive_message(self, message, device, encrypted=True):
        """
        Receives a message from an IoT device and optionally decrypts it.
        """
        if encrypted:
            # If the message is encrypted, decrypt it using the device's key
            decrypted_message = device.decrypt_message(message)
            print(f"Controller received encrypted message: {message} (decrypted: {decrypted_message})")
        else:
            # If the message is not encrypted, display the plain message
            print(f"Controller received plain text message: {message}")

    def intercept_message(self, message, encrypted=True):
        """
        Simulates interception of a message by a bad actor.
        :return: True, indicating the message was intercepted.
        """
        if encrypted:
            # If the message is encrypted, the attacker cannot decrypt it without the key
            print(f"\n[ATTACKER] Intercepted encrypted message: {message}")
            print("[ATTACKER] Attacker failed to decrypt the message without the key.\n")
        else:
            # If the message is not encrypted, the attacker can read it
            print(f"\n[ATTACKER] Intercepted plain text message: {message}")
            print("[ATTACKER] Attacker successfully read the message.\n")
        return True  # Indicate that the message was intercepted

    def log_message(self, device_id, message, encrypted, intercepted, time_taken):
        """
        Logs details of each transmitted message, including device ID, message content, and transmission statistics.
        """
        # Append a dictionary containing message details to the log
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
        # Convert the log of messages to a pandas DataFrame for a tabular summary
        df = pd.DataFrame(self.message_log)
        print("\n--- Summary Table ---")
        print(df)  # Display the summary table


def simulate_devices(num_devices, controller, encrypted=True):
    """
    Simulates multiple IoT devices sending messages to the controller, with optional encryption.
    """
    # Create a list of IoTDevice objects, one for each device
    devices = [IoTDevice(device_id=i) for i in range(1, num_devices + 1)]

    # Loop through each device and send a message to the controller
    for device in devices:
        message = f"Hi Controller! This is device {device.device_id}"  # Create a unique message for each device
        device.send_message(message, controller, encrypted=encrypted)  # Send the message (encrypted or plain)


if __name__ == "__main__":
    # Initialize the controller
    controller = Controller()

    # Specify the number of IoT devices to simulate. Default is 10 but this can be changed.
    num_devices = 10

    # Simulate devices sending plain messages
    print("Simulation with plain messages:")
    simulate_devices(num_devices, controller, encrypted=False)

    # Simulate devices sending encrypted messages
    print("\nSimulation with encrypted messages:")
    simulate_devices(num_devices, controller, encrypted=True)

    # Print the summary of all messages transmitted
    controller.print_summary()
