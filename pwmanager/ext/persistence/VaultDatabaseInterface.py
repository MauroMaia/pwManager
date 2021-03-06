class VaultDatabaseInterface:
    #
    #   Generic Operations
    #

    def load_data(self) -> bool:
        """Load in memory the file content."""
        pass

    def save_data(self) -> bool:
        """Save memory content to file."""
        pass

    #
    #   CREATE operations
    #

    def add_new_db_user(self, username: str, master_password_hash: str):
        """Save a new user with access to this file."""
        pass

    def add_new_entry(self, entry):
        """Save a new entry with access to this file."""
        pass

    #
    #   Search Operations
    #

    def find_user_by_name(self, username: str):
        """Search for a user object based on it username"""
        pass

    def find_entry(self, entry_description: str, entry_username: str, entry_group: str):
        """Search for a Entry object based on it entry_name"""
        pass

    def find_all_entry_by_description(self, entry_description: str):
        """Search all Entries objects based on it entry_description"""
        pass

    def find_all_entry_by_uuid(self, entry_uuid: str):
        """Search all Entries objects based on it entry_uuid"""
        pass
