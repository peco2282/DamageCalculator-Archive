from os import getenv
from dotenv import load_dotenv

load_dotenv(dotenv_path='../.env')

log_id = int(getenv('LOG_ID', 934697584960888862))
mongo_url = getenv('MONGO_DB_URL')
guild_ids_str = getenv('GUILD_ID').split(', ')
execute_channels_str = getenv('EXECUTE_CHANNELS').split(', ')
log_msg_id = int(getenv('ID'))
guild_ids = list()
channel_ids = list()
for id in guild_ids_str:
    guild_ids.append(int(id))


for id in execute_channels_str:
    channel_ids.append(int(id))


from .definition import *
from .dictionary import *
from .embeds import *
from .custom_embeds import *
