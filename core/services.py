import imghdr
import mimetypes
import os
import uuid


def generate_unique_file_path(instance, filename):
    # Save original filename
    instance.filename = filename
    __, ext = os.path.splitext(filename)

    if not ext:
        guessed_ext = imghdr.what(instance.imagefile.file)

        if guessed_ext:
            ext = ".{}".format(guessed_ext)

    # Generate a random UUID
    uuid_str = str(uuid.uuid4())
    instance.uuid = uuid_str

    # Save in a folder/file structure to avoid
    #  too many files in the same directory:
    # - folder name are the 1st and 2n chars
    # - filename the rest
    folder, filename = uuid_str[:2], uuid_str[2:]
    filename = "{}{}".format(filename, ext)

    # Guess and store MIME type and encoding
    content_type, encoding = mimetypes.guess_type(filename)
    instance.content_type = content_type
    instance.encoding = encoding

    return os.path.join(folder, filename)
