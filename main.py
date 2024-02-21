from steamchecker import *


try:
    print(check_steam())
except Exception as e:
    print(f'Unable to connect steam servers, exception: {e}')
