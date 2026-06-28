from abc import ABC, abstractmethod


# =====================================
# Profile
# =====================================

class Profile:

    def __init__(self, name, email):
        self.name = name
        self.email = email


# =====================================
# Iterator Interface
# =====================================

class ProfileIterator(ABC):

    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def get_next(self):
        pass


# =====================================
# Collection Interface
# =====================================

class SocialNetwork(ABC):

    @abstractmethod
    def create_friends_iterator(self):
        pass


# =====================================
# Concrete Collection
# =====================================

class Facebook(SocialNetwork):

    def __init__(self):

        self.friends = [
            Profile("Alice", "alice@gmail.com"),
            Profile("Bob", "bob@gmail.com"),
            Profile("Charlie", "charlie@gmail.com"),
        ]

    def create_friends_iterator(self):
        return FacebookIterator(self)


# =====================================
# Concrete Iterator
# =====================================

class FacebookIterator(ProfileIterator):

    def __init__(self, facebook):

        self.facebook = facebook

        self.current_position = 0

    def has_next(self):

        return self.current_position < len(
            self.facebook.friends
        )

    def get_next(self):

        if self.has_next():

            profile = self.facebook.friends[
                self.current_position
            ]

            self.current_position += 1

            return profile

        return None


# =====================================
# Client
# =====================================

class SocialSpammer:

    def send(self, iterator, message):

        while iterator.has_next():

            profile = iterator.get_next()

            print(
                f"Sending '{message}' to "
                f"{profile.name}"
            )


# =====================================
# Main
# =====================================

facebook = Facebook()

iterator = facebook.create_friends_iterator()

spammer = SocialSpammer()

spammer.send(iterator, "Hello Friends!")