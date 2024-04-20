import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "27624303"))
    API_HASH = os.environ.get("API_HASH", "76a17501d1e952042e2385bc7223312f")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6779545727:AAEsnUUdBdcIXBC2tMzdJ6xlh0f33le41wM")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQGlg28AxCBxCjVVtpHIUzFgQqSIGWIKBXTYVntCsdJe2cLWgtI4nWMHykpIRyoUCoDE1rz7wy8UFhbJJHapY5X1kLQV-IGeI-CKJEhZ2GD6XTgxhEn347NdZc7dsGqywGfCFv6jlxFfAuf12UTx4pPAYfHj21eqMyLFf28PHcjsWLu6FdfnGdT0_A77xf-NsaOX-9MsRyrnhrD7ldSy_Def9KOyL05AlgnTPechcueMNrjqfPzKU25LhEBGj7u7B2HxLcZ0tbdEOM9GIeXD0NCUDKns77Xc6yij7DUhM86dZpUpsKeNxTpEySUF_h2QxUfPwg09m8F3XLeyjqssAKl1tRVHjAAAAABor2ReAA")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", True)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "xDarkoNetwork") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "BotzByDarkoX") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/3d8ecee0ba7dddfc6fce4.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "1756324958")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
