import os
from wakeonlan import send_magic_packet

assert os.getenv('MAC'), "Env variable MAC should be set"

send_magic_packet(os.getenv('MAC'))
