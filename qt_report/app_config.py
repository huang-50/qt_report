import yaml
import os

class AppConfig():
    # singleton app config class
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if AppConfig.__instance == None:
            AppConfig()
        return AppConfig.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if AppConfig.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            AppConfig.__instance = self
            # load config file
            with open(os.path.join(os.path.dirname(__file__), 'config.yaml')) as yaml_file:
                self.config = yaml.load(yaml_file, Loader=yaml.FullLoader)
            self.Databases=self.config['Databases']
            self.html_header=self.config['html_header']
            self.html_footer=self.config['html_footer']
            self.section_header=self.config['section_header']
            self.section_footer=self.config['section_footer']
            

    def get(self, key, default=None):
        return self.config.get(key, default)

    def _get_config_path(self, filename='qt_app.yaml'):
        #loop through system config locations
        for path in ['/etc', '/usr/local/etc', '/usr/local/etc/qt_report', 
            os.path.abspath(os.path.join(os.path.dirname(__file__), '../../config')) ]:
            if os.path.exists(os.path.join(path, filename)):
                return os.path.join(path, filename)
        return None

