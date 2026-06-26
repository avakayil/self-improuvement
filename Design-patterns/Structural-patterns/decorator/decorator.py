from abc import ABC, abstractmethod
import base64
import zlib


# ======================================
# Component
# ======================================

class DataSource(ABC):

    @abstractmethod
    def write_data(self, data):
        pass

    @abstractmethod
    def read_data(self):
        pass


# ======================================
# Concrete Component
# ======================================

class FileDataSource(DataSource):

    def __init__(self):
        self.data = ""

    def write_data(self, data):
        self.data = data

    def read_data(self):
        return self.data


# ======================================
# Base Decorator
# ======================================

class DataSourceDecorator(DataSource):

    def __init__(self, source: DataSource):
        self.wrappee = source

    def write_data(self, data):
        self.wrappee.write_data(data)

    def read_data(self):
        return self.wrappee.read_data()


# ======================================
# Encryption Decorator
# ======================================

class EncryptionDecorator(DataSourceDecorator):

    def write_data(self, data):

        encrypted = base64.b64encode(
            data.encode()
        ).decode()

        self.wrappee.write_data(encrypted)

    def read_data(self):

        encrypted = self.wrappee.read_data()

        return base64.b64decode(
            encrypted.encode()
        ).decode()


# ======================================
# Compression Decorator
# ======================================

class CompressionDecorator(DataSourceDecorator):

    def write_data(self, data):

        compressed = zlib.compress(
            data.encode()
        )

        self.wrappee.write_data(compressed)

    def read_data(self):

        compressed = self.wrappee.read_data()

        return zlib.decompress(
            compressed
        ).decode()


# ======================================
# Client
# ======================================

source = FileDataSource()

source.write_data("Hello")
print(source.read_data())

print()

source = EncryptionDecorator(source)

source.write_data("Hello")
print(source.read_data())

print()

source = CompressionDecorator(source)

source.write_data("Hello")
print(source.read_data())