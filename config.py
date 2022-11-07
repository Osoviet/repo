import os
import ProxyCloud

BOT_TOKEN =  os.environ.get('bot_token','5694666378:AAHxhtZ92GvZ199OdICwoAOdDQHhbjnK5yM')
API_ID =  os.environ.get('api_id','17345593')
API_HASH = os.environ.get('api_hash','80ae053901c049b519ea5bf0f50e1675')
SPLIT_FILE = 1024 * 1024 * int(os.environ.get('split_file','99'))
ROOT_PATH = 'root/'
ACCES_USERS = os.environ.get('tl_admin_user','STANISLASKI').split(';')
PROXY = ProxyCloud.parse(os.environ.get('proxy_enc','http://KIDDKDYJJKJJGDYDJKGJGJYGIHIERKDGLGDELI'))

if PROXY:
  print(f'Proxy {PROXY.as_dict_proxy()}')
