import os
import environ

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env = environ.Env()
env.read_env()  # 現在のディレクトリか上位にある.envを読み込み、環境変数に設定する

# env.bool() は'true', 'on', 'y', 'yes', 'ok', '1' を真として扱う
DEBUG = env.bool('DEBUG')

# env.list() は環境変数から取得した文字列をカンマ区切りでリストに変換
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')
if DEBUG:
    INTERNAL_IPS = env.list('INTERNAL_IPS')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    ...
    'myapp'
]
# MIDDLEWARE = [...]

if env.bool('USE_SILK', default=False):
    INSTALLED_APPS.append('silk')
    MIDDLEWARE.append('silk.middleware.SilkyMiddleware')

DATABASE = {
    'default': env.db_url('DATABASE_URL')
}