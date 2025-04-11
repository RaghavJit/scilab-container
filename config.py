DB_NAME_DEFAULT = 'djangoDB'
DB_USER_DEFAULT = 'dbsiteuser'
DB_PASS_DEFAULT = 'password!'
DB_HOST_DEFAULT = '172.18.0.1'
DB_PORT_DEFAULT = '3306'

DB_NAME_SCILAB = 'scilab_c'
DB_USER_SCILAB = 'dbsiteuser'
DB_PASS_SCILAB = 'password!'
DB_HOST_SCILAB = '172.18.0.1'
DB_PORT_SCILAB = '3306'

BIN = '/Temp/Scilab.Bin'
# SCILAB_FLAGS = '-noatomsautoload'
SCILAB_FLAGS = '-noatomsautoload -nogui -nb '
SCIMAX_LOADER = '/Sites/CLOUD/scilab/scilab-scimax-2.1.4/loader.sce'
UPLOADS_PATH = '/Sites/scilab-on-cloud/uploads'
SCILAB_3 = 'scilab-5.3.3'
SCILAB_4 = 'scilab-5.4.1'
SCILAB_5 = 'scilab-5.5.2'
SCILAB_6 = 'scilab-5.5.2'
# Host for sending e-mail.
EMAIL_HOST_SERVER = 'localhost'

# Port for sending e-mail.
EMAIL_PORT_SERVER = 25
#EMAIL_TIMEOUT_SERVER = 4

# Optional SMTP authentication information for EMAIL_HOST.
#EMAIL_HOST_USER_SERVER = 'user'
#EMAIL_HOST_PASSWORD_SERVER = 'password'
#EMAIL_USE_TLS_SERVER = False

FROM_EMAIL = 'textbook@scilab.in'
TO_EMAIL = 'scilab-cloud@fossee.in'
CC_EMAIL = ''
BCC_EMAIL = 'prashantsinalkar@gmail.com'

# github
#GITHUB_ACCESS_TOKEN = '6b8b51fdba799db7c9e1bffd0bc4001967efa26e'
GITHUB_ACCESS_TOKEN_SOCBOT = '3c0201b0efb748381de6166109dc51caea04edf0'

#GITHUB_ACCESS_TOKEN = '2706c4bad278c031f98e1b43e42244dc22ad73ab'
GITHUB_ACCESS_TOKEN = 'c512fb4c9019dc6238a06d498852306d31cf050d'
SITE = 'https://testcloud.scilab.in'
GARUDA_SERVER = 0
MAIN_REPO='/Sites/scilab-on-cloud/uploads/'
TEMP_USER='psinalkar1988'
MAIN_USER='fosseeuser'

DEFAULT_TORNADO_WORKERS=1
DEFAULT_REQUEST_COUNT=1
MAX_SCILAB_INSTANCE=1
MIN_SCILAB_INSTANCE=1

