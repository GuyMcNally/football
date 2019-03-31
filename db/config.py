from configparser import ConfigParser
  
def config(filename='db/database.ini', section='cats'):
    # create a parser
    configParser = ConfigParser()
    # read config file
    configParser.read(filename)
    
    # params = configParser.get(section)
    print(configParser.read(filename))
    # get section, default to postgresql
    db = {}
    if configParser.has_section(section):
        params = configParser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
 
    return db