import logging

logging.basicConfig(filename='NameCheck.log',level = logging.DEBUG)

def nameCheck(name):
    if len(name) < 2:
        logging.debug('Checking for name length...')
        return 'Invalid name!'
    elif name.isspace():
        logging.debug('Checking if name is a space...')
        return 'Invalid name!'
    elif name.isalpha():
        logging.debug('Checking if name is a alphabet...')
        return 'Name is valid'
    elif name.replace(' ','').isalpha():
        logging.debug('Checking for full name...')
        return 'Name is valid'
    else:
        logging.debug('Failed all checks...')
        return 'Invalid name!'

print(nameCheck('Avinash'))
