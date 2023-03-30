import binascii

def encode_file_to_varbinary(file_path):
    with open(file_path, 'rb') as file:
        file_content = file.read()
        varbinary_content = binascii.hexlify(file_content)
        return "CAST('{}' AS VARBINARY(1024))".format(varbinary_content.decode())

file_path = 'shell.jsp'
varbinary_str = encode_file_to_varbinary(file_path)
print(varbinary_str)
