from SafoneAPI import SafoneAPI
from UsuMusic.core.bot import UsuBot
from UsuMusic.core.dir import dirr
from UsuMusic.core.git import git
from UsuMusic.core.userbot import Userbot
from UsuMusic.misc import dbb, heroku, sudo
from .logging import LOGGER

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Load Sudo Users from DB
sudo()
api = SafoneAPI()
# Bot Client
app = UsuBot()

# Assistant Client
userbot = Userbot()

from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
HELPABLE = {}
