# 다중예외처리

try:
    client_obj.get_url(url)

except (URLError, ValueError):
    client_obj.remove_url(url)



    
import errno
import logging
try:
    f = open(filename)
except OSError as e:
    if e.errno == errno.ENOENT:
        logger.error('File not Found')

    elif e.errno == errno.EACCES:
        logger.error('Permission denied')
    else:
        logger.error('Unexpected error')
