class VideoFile:

    def __init__(self, filename):
        self.filename = filename


class OggCompressionCodec:

    def __str__(self):
        return "Ogg Codec"


class MPEG4CompressionCodec:

    def __str__(self):
        return "MP4 Codec"


class CodecFactory:

    @staticmethod
    def extract(file):
        print(f"Extracting codec from {file.filename}")
        return OggCompressionCodec()


class BitrateReader:

    @staticmethod
    def read(file, codec):
        print(f"Reading {file.filename} using {codec}")
        return "Video Buffer"

    @staticmethod
    def convert(buffer, codec):
        print(f"Converting using {codec}")
        return "Converted Buffer"


class AudioMixer:

    def fix(self, buffer):
        print("Fixing Audio")
        return "Final Video"


# ============================
# Facade
# ============================

class VideoConverter:

    def convert(self, filename, format):

        file = VideoFile(filename)

        source_codec = CodecFactory.extract(file)

        if format == "mp4":
            destination_codec = MPEG4CompressionCodec()
        else:
            destination_codec = OggCompressionCodec()

        buffer = BitrateReader.read(file, source_codec)

        result = BitrateReader.convert(buffer, destination_codec)

        result = AudioMixer().fix(result)

        return result


# ============================
# Client
# ============================

converter = VideoConverter()

video = converter.convert("youtube.ogg", "mp4")

print(video)