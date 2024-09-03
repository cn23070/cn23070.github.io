import sqlite3  # Import SQLite library for database operations
from hashlib import sha256  # Import SHA-256 hashing for secure password storage
from datetime import datetime  # Import datetime for recording date and time stamps
import os  # Import os for file operations
import getpass  # Import getpass for secure password input
from cryptography.fernet import Fernet  # Import Fernet for secure content encryption

class UserRole:
    """
    Define user a admin and standard user role as constants.
    """
    ADMIN = "admin"
    REGULAR_USER = "regular_user"

# Define a User class
class User:
    """
    Represents a user in the system with attributes for user ID, username, password hash, and role.
    Attributes:
    user_id (int): The unique ID of the user.
    username (str): The username of the user.
    password_hash (str): The hashed password of the user.
    role (str): The role of the user (admin or regular_user).
    """
    def __init__(self, user_id, username, password_hash, role):
        """
        Initialize user object and attributes.        
        
        Parameters:
        user_id (int): The unique ID of the user.
        username (str): The username of the user.
        password_hash (str): The hashed password of the user.
        role (str): The role of the user (admin or regular_user).   
        """ 
        self.user_id = user_id
        self.username = username
        self.password_hash = password_hash
        self.role = role
        
    def set_password(self, password):        
        """
        Set the user's password using hash.
        Parameters:
        password (str): The password to be hashed and set.
        """  
        self.password_hash = sha256(password.encode()).hexdigest()

    def check_password(self, password):  
        """
                Check if the provided password matches the stored password hash.
                Parameters:
                password (str): The password to check.
                Returns:
                bool: True if the password matches, False if it does not.
                
        """  
        return self.password_hash == sha256(password.encode()).hexdigest()

    def get_role(self):
        """
                Get the role of the user.
                Returns:
                str: The role of the user.
        """
        return self.role

    def get_user_id(self):
        """
        Get the user's unique ID.
        Returns:
        int: The user's ID.
        """
        return self.user_id

    def get_username(self):
        """
        Get the user's username.
        Returns:
        str: The username of the user.
        """
        return self.username

    def get_password_hash(self):
        """
        Get the user's password hash.
        Returns:
        str: The hashed password of the user.
        """
        return self.password_hash

# Define an Administrator with special privileges class inheriting from User
class Administrator(User):
    """
    Represents an administrator user with additional privileges to manage artefacts and view logs.
    Inherits from User and adds methods for artefact management and log viewing.
    """
    def create_artefact(self, artefact, db_manager):
        """
        Create a new artefact and store it in the database.
        Parameters:
        artefact (Artefact): The artefact to be stored.
        db_manager (DatabaseManager): The database manager to interact with the database.
        """
        db_manager.store_artefact(artefact)

    def delete_artefact(self, artefact_id, db_manager):
        """
         Delete an artefact from the database using the ID.

         Parameters:
         artefact_id (int): The ID of the artefact to be deleted.
         db_manager (DatabaseManager): The database manager to interact with the database.
         """
        db_manager.delete_artefact(artefact_id)

    def view_artefact(self, artefact_id, db_manager):
        """
        View a specific artefact from the database using artifact ID.
        Parameters:
        artefact_id (int): The ID of the artefact to view.
        db_manager (DatabaseManager): The database manager to interact with the database.
        Returns:
        Artefact: The retrieved artefact if found, or None.
        """
        return db_manager.retrieve_artefact(artefact_id)

    def view_logs(self, db_manager):
        """
        View all logs in the system.
        Parameters:
        db_manager (DatabaseManager): The database manager to interact with the database.
        """
        db_manager.view_logs()

    def view_all_artefacts(self, db_manager):
        """
        View all artefacts in the database.
        Parameters:
        db_manager (DatabaseManager): The database manager to interact with the database.
        Returns:
        list: A list of all artefacts in the database.
        """
        return db_manager.retrieve_all_artefacts()

# Define a RegularUser class representing a regular user with limited priveledges, inheriting from User
class RegularUser(User):
    """
    Represents a regular user with limited privileges for managing and viewing artefacts.
    Inherits from User and adds methods for artefact management based on ownership.
    """
    def upload_artefact(self, artefact, db_manager):
        """
        Upload an artefact to the database if the user is the owner.
        Parameters:
        artefact (Artefact): The artefact to be uploaded.
        db_manager (DatabaseManager): The database manager to interact with the database.
        """
        if artefact.owner_id == self.user_id:
            db_manager.store_artefact(artefact)

    def modify_artefact(self, artefact, db_manager):
        """
        Modify an existing artefact if the user is the owner.
        Parameters:
        artefact (Artefact): The artefact with updated details.
        db_manager (DatabaseManager): The database manager to interact with the database.
        """
        existing_artefact = db_manager.retrieve_artefact(artefact.artefact_id)
        if existing_artefact and existing_artefact.owner_id == self.user_id:
            db_manager.update_artefact(artefact)

    def view_artefact(self, artefact_id, db_manager):
        """
        View an artefact if the user is the owner or if the user is an admin.
        Parameters:
        artefact_id (int): The ID of the artefact to view.
        db_manager (DatabaseManager): The database manager to interact with the database.
        Returns:
        Artefact: The retrieved artefact if found, or None.
         """
        artefact = db_manager.retrieve_artefact(artefact_id)
        if artefact and (artefact.owner_id == self.user_id or self.get_role() == UserRole.ADMIN):
            return artefact
        return None

    def view_my_artefacts(self, db_manager):
        """
        View all artefacts owned by the user.
        Parameters:
        db_manager (DatabaseManager): The database manager to interact with the database.
        Returns:
        list: A list of artefacts owned by the user.
        """
        return db_manager.retrieve_artefacts_by_user(self.user_id)

# Define an Artefact class to represent artifacts in the system
class Artefact:
    """
    Represents an artefact with attributes for ID, title, content, checksum, encrypted content, timestamps, and owner.
    Attributes:
    artefact_id (int): The unique ID of the artefact.
    title (str): The title of the artefact.
    content (bytes): The content of the artefact.
    checksum (str): The checksum of the content.
    encrypted_content (bytes): The encrypted content of the artefact.
    timestamps (str): The timestamp of the artefact creation or update.
    owner_id (int): The ID of the owner of the artefact.
    """
    def __init__(self, artefact_id, title, content, owner_id):
        """
        Initialize an Artefact object.
        Parameters:
        artefact_id (int): The unique ID of the artefact.
        title (str): The title of the artefact.
        content (bytes): The content of the artefact.
        owner_id (int): The ID of the owner of the artefact.
        """
        self.artefact_id = artefact_id
        self.title = title
        self.content = content
        self.checksum = self.generate_checksum(content)
        self.encrypted_content = None
        self.timestamps = self.create_timestamp()
        self.owner_id = owner_id

    def generate_checksum(self, data):
        """
        Generate a checksum for the given data for data integrity check.
        Parameters:
        data (bytes): The data to generate a checksum for.
        Returns:
        str: The generated checksum.
        """
        return sha256(data).hexdigest()

    def encrypt_content(self, encryption_manager):
        """
        Encrypt the content of the artefact.
        Parameters:
        encryption_manager (EncryptionManager): The encryption manager to use for encryption.
        """
        self.encrypted_content = encryption_manager.encrypt(self.content)

    def decrypt_content(self, encryption_manager):
        """
        Decrypt the content of the artefact.
        Parameters:
        encryption_manager (EncryptionManager): The encryption manager to use for decryption.
        Returns:
        bytes: The decrypted content.
        """
        return encryption_manager.decrypt(self.encrypted_content)

    def create_timestamp(self):
        """
        Create a timestamp for the artefact.
        Returns:
        str: The current timestamp.
        """
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Define an EncryptionManager class for handling encryption
class EncryptionManager:
    """
    Manages encryption and decryption of data using a generated key.
    Attributes:
    key (bytes): The encryption key.
    cipher (Fernet): The Fernet cipher object for encryption and decryption.
    """
    def __init__(self):
        """
        Initialize an EncryptionManager with a generated encryption key.
        """
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt(self, data):
        """
        Encrypt the given data using cipher.
        Parameters:
        data (bytes): The data to encrypt.
        Returns:
        bytes: The encrypted data.
        """
        return self.cipher.encrypt(data)

    def decrypt(self, data):
        """
        Decrypt the given data using cipher.
        Parameters:
        data (bytes): The data to decrypt.
        Returns:
        bytes: The decrypted data.
        """
        return self.cipher.decrypt(data)

# Define a ChecksumManager class for checksum operations
class ChecksumManager:
    """
    Manages integrity of artifact data using checksum. Generate a checksum for the given data using SHA-256.
    Attributes:
    None
    """
    @staticmethod
    def generate_checksum(data):
        """
        Generate a checksum for the given data.
        Parameters:
        data (bytes): The data to generate a checksum for.
        Returns:
        str: The generated checksum.
        """
        return sha256(data).hexdigest()

    @staticmethod
    def verify_checksum(data, checksum):
        """
        Verify if the data matches the provided checksum.
        Parameters:
        data (bytes): The data to verify.
        checksum (str): The checksum to compare against.
        Returns:
        bool: True if the data matches the checksum, False otherwise.
        """
        return sha256(data).hexdigest() == checksum

# Define a TimestampManager class for timestamp operations
class TimestampManager:
    """
    Manages creation of timestamps.
    Methods:
    create_timestamp: Create a formatted current timestamp.
    """
    @staticmethod
    def create_timestamp():
        """
        Create a timestamp.
        Returns:
        str: The current timestamp.
        """
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def update_timestamp():
        """
        Update a timestamp.
        Returns:
        str: The current timestamp.
        """
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Define a DatabaseManager class for handling database operations
class DatabaseManager:
    """
    Manages interaction with the SQLite database including storing, retrieving, and updating artefacts,
    and logging user actions.
    Attributes:
    conn (sqlite3.Connection): The database connection object.
    """
    def __init__(self, db_name="secure_enclave.db"):
        """
        Initialize a DatabaseManager to interact with the database.
        Parameters:
        db_name (str): The name of the database file.
        """
        self.db_name = db_name
        self.connect_to_db()

    def connect_to_db(self):
        # Connect to the SQLite database
        self.db_connection = sqlite3.connect(self.db_name, timeout=10)
        self.db_cursor = self.db_connection.cursor()
        self.create_tables()

    def create_tables(self):
        """
        Create the necessary tables in the database if they do not exist.
        """
        self.db_cursor.execute('''CREATE TABLE IF NOT EXISTS Users (
                                    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    username TEXT UNIQUE NOT NULL,
                                    password_hash TEXT NOT NULL,
                                    role TEXT NOT NULL)''')

        self.db_cursor.execute('''CREATE TABLE IF NOT EXISTS Artefacts (
                                    artefact_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    title TEXT NOT NULL,
                                    content BLOB NOT NULL,
                                    checksum TEXT NOT NULL,
                                    encrypted_content BLOB NOT NULL,
                                    timestamps TEXT NOT NULL,
                                    owner_id INTEGER NOT NULL,
                                    FOREIGN KEY(owner_id) REFERENCES Users(user_id))''')

        self.db_cursor.execute('''CREATE TABLE IF NOT EXISTS Logs (
                                    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    action TEXT NOT NULL,
                                    user_id INTEGER,
                                    artefact_id INTEGER,
                                    timestamp TEXT NOT NULL,
                                    FOREIGN KEY(user_id) REFERENCES Users(user_id),
                                    FOREIGN KEY(artefact_id) REFERENCES Artefacts(artefact_id))''')

        self.db_connection.commit()

    def store_user(self, user):
        """
        Store a user in the database.
        Parameters:
        user (User): The user to store.
        """
        self.db_cursor.execute('''INSERT INTO Users (username, password_hash, role)
                                  VALUES (?, ?, ?)''',
                               (user.username, user.password_hash, user.role))
        self.db_connection.commit()

    def store_artefact(self, artefact):
        """
        Store an artefact in the database.
        Parameters:
        artefact (Artefact): The artefact to store.
        """
        self.db_cursor.execute('''INSERT INTO Artefacts (title, content, checksum, encrypted_content, timestamps, owner_id)
                                  VALUES (?, ?, ?, ?, ?, ?)''',
                               (artefact.title, artefact.content, artefact.checksum,
                                artefact.encrypted_content, artefact.timestamps, artefact.owner_id))
        self.db_connection.commit()

    def retrieve_artefact(self, artefact_id):
        """
        Retrieve an artefact from the database by its ID.
        Parameters:
        artefact_id (int): The ID of the artefact to retrieve.
        Returns:
        Artefact: The retrieved artefact if found, or None if not found.
        """
        self.db_cursor.execute('SELECT * FROM Artefacts WHERE artefact_id = ?', (artefact_id,))
        row = self.db_cursor.fetchone()
        if row:
            return Artefact(row[0], row[1], row[2], row[6])
        return None

    def update_artefact(self, artefact):
        """
        Update an artefact from the database by its ID.
        Parameters:
        artefact_id (int): The ID of the artefact to retrieve.
        Returns:
        Artefact: Retrieves and updates artefact if found, or None if not found.
        """
        self.db_cursor.execute('''UPDATE Artefacts
                                  SET title = ?, content = ?, checksum = ?, encrypted_content = ?, timestamps = ?
                                  WHERE artefact_id = ?''',
                               (artefact.title, artefact.content, artefact.checksum,
                                artefact.encrypted_content, artefact.timestamps, artefact.artefact_id))
        self.db_connection.commit()

    def delete_artefact(self, artefact_id):
        """
        Delete an artefact from the database by its ID.
        Parameters:
        artefact_id (int): The ID of the artefact to delete.
        Returns:
        Artefact: Retrieves and deletes artefact if found, or None if not found.
         """
        self.db_cursor.execute('DELETE FROM Artefacts WHERE artefact_id = ?', (artefact_id,))
        self.db_connection.commit()

    def retrieve_all_artefacts(self):
        """
        Retrieve all artefacts from the database.
        Returns:
        list: A list of all artefacts in the database.
        """    
        self.db_cursor.execute('SELECT * FROM Artefacts')
        rows = self.db_cursor.fetchall()
        return [Artefact(row[0], row[1], row[2], row[6]) for row in rows]

    def retrieve_artefacts_by_user(self, user_id):
        """
        Retrieve all artefacts owned by a specific user.
        Parameters:
        user_id (int): The ID of the user whose artefacts to retrieve.
        Returns:
        list: A list of artefacts owned by the user.
        """
        self.db_cursor.execute('SELECT * FROM Artefacts WHERE owner_id = ?', (user_id,))
        rows = self.db_cursor.fetchall()
        return [Artefact(row[0], row[1], row[2], row[6]) for row in rows]

    def view_logs(self):
        """
        View all logs in the database.
        """
        self.db_cursor.execute('SELECT * FROM Logs')
        rows = self.db_cursor.fetchall()
        for row in rows:
            print(f"Log ID: {row[0]}, Action: {row[1]}, User ID: {row[2]}, Artefact ID: {row[3]}, Timestamp: {row[4]}")

    def close(self):
        # Close the database connection
        self.db_connection.close()

# Define a Logger class for logging actions
class Logger:
    """
    Handles logging of events to the database.
    Attributes:
    db_manager (DatabaseManager): The database manager to interact with the database.
    """
    def __init__(self, db_manager):
        """
        Initialize Logger with a reference to the database manager.
        Parameters:
        db_manager (DatabaseManager): The database manager to interact with the database.
        """
        self.db_manager = db_manager

    def log_event(self, action, user_id=None, artefact_id=None):
        """
        Log an event to the database.
        Parameters:
        action (str): The action performed.
        user_id (int, optional): The ID of the user who performed the action. Defaults to None.
        artefact_id (int, optional): The ID of the artefact related to the action. Defaults to None.
        """
        timestamp = TimestampManager.create_timestamp()
        self.db_manager.db_cursor.execute('''INSERT INTO Logs (action, user_id, artefact_id, timestamp)
                                            VALUES (?, ?, ?, ?)''',
                                         (action, user_id, artefact_id, timestamp))
        self.db_manager.db_connection.commit()

    def view_logs(self):
        """
        Display all logs.
        """
        self.db_manager.view_logs()

# Define a function for user login
def login_user(db_manager):
    """
    Prompt the user for their credentials and validate them against the database.
    Parameters:
    db_manager (DatabaseManager): The database manager to interact with the database.
    Returns:
    User: The authenticated User object if credentials are valid, or None.
    """
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")

    # Retrieve user from the database
    db_manager.db_cursor.execute('SELECT * FROM Users WHERE username = ?', (username,))
    row = db_manager.db_cursor.fetchone()

    if row and sha256(password.encode()).hexdigest() == row[2]:
        # Create and return a User object if credentials are valid
        return User(row[0], row[1], row[2], row[3])
    return None

# Define the main function
def main():
    """
    Main function to initialize the system and manage user interactions.
    """
    # Initialize DatabaseManager and Logger
    db_manager = DatabaseManager()
    logger = Logger(db_manager)

    while True:
        # Prompt the user to choose between creating an admin or a regular user
        choice = input("Choose an option: [create_admin, create_regular, login, exit]: ")

        if choice == 'create_admin':
            # Prompt for admin details and create an admin user
            admin_username = input("Enter admin user username: ")
            admin_password = getpass.getpass("Enter a password to be used by the admin user: ")

            # Check if the admin username already exists
            db_manager.db_cursor.execute('SELECT * FROM Users WHERE username = ?', (admin_username,))
            if db_manager.db_cursor.fetchone():
                print("Admin username already exists. Please choose a different username.")
                db_manager.close()
                return

            admin_user = Administrator(None, admin_username, '', UserRole.ADMIN)
            admin_user.set_password(admin_password)

            try:
                # Store the admin user in the database
                db_manager.store_user(admin_user)
            except sqlite3.IntegrityError:
                print("Username for this admin user already exists. Please choose a different username.")
                db_manager.close()
                return

        elif choice == 'create_regular':
            # Prompt for regular user details and create a regular user
            regular_username = input("Enter standard user username: ")
            regular_password = getpass.getpass("Enter a password to be used for the standard user: ")

            # Check if the regular user username already exists
            db_manager.db_cursor.execute('SELECT * FROM Users WHERE username = ?', (regular_username,))
            if db_manager.db_cursor.fetchone():
                print("Username for this standard user already exists. Choose a different username.")
                db_manager.close()
                return

            regular_user = RegularUser(None, regular_username, '', UserRole.REGULAR_USER)
            regular_user.set_password(regular_password)

            try:
                # Store the regular user in the database
                db_manager.store_user(regular_user)
            except sqlite3.IntegrityError:
                print("Username for this standard user already exists. Choose a different username.")
                db_manager.close()
                return

        while True:
            # Prompt the user to log in
            user = login_user(db_manager)
            if not user:
                print("Login failed.")
                continue

            # Create user-specific instances
            if user.get_role() == UserRole.ADMIN:
                user = Administrator(user.get_user_id(), user.get_username(), user.get_password_hash(), user.get_role())
            elif user.get_role() == UserRole.REGULAR_USER:
                user = RegularUser(user.get_user_id(), user.get_username(), user.get_password_hash(), user.get_role())

            while True:
                # Display user-specific actions
                print(f"Welcome {user.get_username()}, you have the role {user.get_role()}")
                if user.get_role() == UserRole.ADMIN:
                    action = input("Choose action: [upload, delete, view_all, view_logs, logout, exit]: ")
                    if action == 'upload':
                        # Handle artefact upload for admin
                        file_path = input("Please enter the full path to file including file name to upload: ")
                        if os.path.exists(file_path):
                            try:
                                with open(file_path, 'rb') as file:
                                    content = file.read()
                                    artefact = Artefact(None, os.path.basename(file_path), content, user.get_user_id())
                                    encryption_manager = EncryptionManager()
                                    artefact.encrypt_content(encryption_manager)
                                    db_manager.store_artefact(artefact)
                                    logger.log_event("Uploaded artefact", user_id=user.get_user_id(), artefact_id=artefact.artefact_id)
                                    print(f"Successfully uploaded artefact {artefact.title}")

                                    # Display artefact details
                                    print("Artifact Details:")
                                    print(f"ID: {artefact.artefact_id}")
                                    print(f"Title: {artefact.title}")
                                    print(f"Checksum: {artefact.checksum}")
                                    print(f"Timestamp: {artefact.timestamps}")
                            except Exception as e:
                                print(f"Error reading file: {e}")
                        else:
                            print("File does not exist or cannot be located.")

                    elif action == 'delete':
                        # Handle artefact deletion for admin
                        try:
                            artefact_id = int(input("Enter artefact ID to delete: "))
                            db_manager.delete_artefact(artefact_id)
                            logger.log_event("Deleted artefact", user_id=user.get_user_id(), artefact_id=artefact_id)
                            print("Artefact deleted.")
                        except ValueError:
                            print("Invalid artefact ID. Please enter a numeric value.")

                    elif action == 'view_all':
                        # View all artefacts for admin
                        artefacts = user.view_all_artefacts(db_manager)
                        for artefact in artefacts:
                            print(f"ID: {artefact.artefact_id}, Title: {artefact.title}, Timestamp: {artefact.timestamps}")

                    elif action == 'view_logs':
                        # View all logs for admin
                        logger.view_logs()

                    elif action == 'logout':
                        # Handle logout
                        print("Logged out.")
                        break

                    elif action == 'exit':
                        # Exit the application
                        print("Exiting application.")
                        db_manager.close()
                        return

                    else:
                        print("Invalid action.")

                elif user.get_role() == UserRole.REGULAR_USER:
                    action = input("Choose action: [upload, modify, view_my, logout, exit]: ")
                    if action == 'upload':
                        # Handle artefact upload for regular user
                        file_path = input("Please enter the full path to file including file name to upload: ")
                        if os.path.exists(file_path):
                            try:
                                with open(file_path, 'rb') as file:
                                    content = file.read()
                                    artefact = Artefact(None, os.path.basename(file_path), content, user.get_user_id())
                                    artefact.encrypt_content(EncryptionManager())
                                    user.upload_artefact(artefact, db_manager)
                                    logger.log_event("Uploaded artefact", user_id=user.get_user_id(), artefact_id=artefact.artefact_id)
                                    print(f"Successfully uploaded artefact {artefact.title}")

                                    # Display artefact details
                                    print("Artifact Details:")
                                    print(f"ID: {artefact.artefact_id}")
                                    print(f"Title: {artefact.title}")
                                    print(f"Checksum: {artefact.checksum}")
                                    print(f"Timestamp: {artefact.timestamps}")
                            except Exception as e:
                                print(f"Error reading file: {e}")
                        else:
                            print("File does not exist or cannot be found.")

                    elif action == 'modify':
                        # Handle artefact modification for regular user
                        try:
                            artefact_id = int(input("Enter your artefact ID that you wish to modify: "))
                            existing_artefact = db_manager.retrieve_artefact(artefact_id)
                            if existing_artefact and existing_artefact.owner_id == user.get_user_id():
                                file_path = input("Enter full path to file to modify: ")
                                if os.path.exists(file_path):
                                    try:
                                        with open(file_path, 'rb') as file:
                                            content = file.read()
                                            artefact = Artefact(artefact_id, os.path.basename(file_path), content, user.get_user_id())
                                            artefact.encrypt_content(EncryptionManager())
                                            user.modify_artefact(artefact, db_manager)
                                            logger.log_event("Modified artefact", user_id=user.get_user_id(), artefact_id=artefact_id)
                                            print(f"Successfully modified artefact {artefact.title}")

                                            # Display updated artefact details
                                            print("Updated Artifact Details:")
                                            print(f"ID: {artefact.artefact_id}")
                                            print(f"Title: {artefact.title}")
                                            print(f"Checksum: {artefact.checksum}")
                                            print(f"Timestamp: {artefact.timestamps}")
                                    except Exception as e:
                                        print(f"Error reading file: {e}")
                                else:
                                    print("File does not exist or cannot be located.")
                            else:
                                print("Artefact does not belong to you or does not exist.")
                        except ValueError:
                            print("Invalid artefact ID. Please enter a numeric value.")

                    elif action == 'view_my':
                        # View artefacts owned by the regular user
                        artefacts = user.view_my_artefacts(db_manager)
                        for artefact in artefacts:
                            print(f"ID: {artefact.artefact_id}, Title: {artefact.title}, Timestamp: {artefact.timestamps}")

                    elif action == 'logout':
                        # Handle logout
                        print("Logged out.")
                        break

                    elif action == 'exit':
                        # Exit the application
                        print("Exiting application.")
                        db_manager.close()
                        return

                    else:
                        print("Invalid action.")

# Run the main function if this script is executed
if __name__ == "__main__":
    main()
    
# References for Libraries Used
#sqlite3:
#Reference: SQLite Consortium. (n.d.). SQLite Documentation. Retrieved from https://www.sqlite.org/docs.html
#Usage: Used as a lightweight database engine by the application.

#hashlib:
#Reference: Python Software Foundation. (n.d.). hashlib — Secure hashes and message digests. 
#In Python 3.x Library Documentation. Retrieved from https://docs.python.org/3/library/hashlib.html
#Usage: Provides secure hash and message digest algorithms, including SHA-256, used for password hashing.

#datetime:
#Reference: Python Software Foundation. (n.d.). datetime — Basic date and time types. 
#In Python 3.x Library Documentation. Retrieved from https://docs.python.org/3/library/datetime.html
#Usage: Used for creating and managing timestamps of key events in the application.

#cryptography:
#Reference: The Cryptography Developers. (n.d.). Cryptography Library Documentation. 
#Retrieved from https://cryptography.io/en/latest/
#Usage: Provides the Fernet symmetric encryption scheme for securely encrypting and decrypting content.

#os:
#Reference: Python Software Foundation. (n.d.). os — Miscellaneous operating system interfaces. 
#In Python 3.x Library Documentation. Retrieved from https://docs.python.org/3/library/os.html
#Usage: Allows interaction with the underlying operating system, allowing local file upload by the application.   

#getpass:
#Reference: Python Software Foundation. (n.d.). getpass — Portable password input. 
#In Python 3.x Library Documentation. Retrieved from https://docs.python.org/3/library/getpass.html
#Usage: Used to securely capture password input from the user without showing charachters on screen. 
