"""

Specialised configuration class. Used to process command line configuration
options.

"""

from spring_time.configuration.configuration import Configuration

class CommandLineConfiguration(Configuration):

    """

    Command line configuration parses, extends Configuration.

    Parses options passed by the user on the command line. Use to neatly
    wrap Argparse functionality in one place.

    """

    def __init__(self, name, config_id=None):

        super().__init__(name, config_id)


    def parse(self):

        """

        Parse the command line configuration

        """

        pass
