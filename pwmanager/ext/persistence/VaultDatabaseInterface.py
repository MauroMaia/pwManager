class VaultDatabaseInterface:
    def load_data(self) -> bool:
        """Load in memory the file content."""
        pass

    def save_data(self) -> bool:
        """Save memory content to file."""
        pass

    def add_new_db_user(self, username, master_password_hash):
        """Save a new user with access to this file."""
        pass

    def find_user_by_name(self, username=None):
        """Serch for a user object based on it username"""
        pass
