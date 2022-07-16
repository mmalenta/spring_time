"""

This module provides a Configuration base class to be used to derive
specialised configuration classes.

"""

from time import gmtime, strftime, time

class Configuration():

    """

    Configuration base class.

    Instances of this class should not be created directly in the code. This
    class should be used only to derive more specialised configuration
    classes.

    """

    def __init__(self, name, config_id=None):
        self._name = name
        if config_id is not None:
            self._id = config_id
        else:
            # Generate configuration ID
            tmp_id = strftime("%Y-%m-%d_%H:%M:%S", gmtime(time()))
            self._id = tmp_id

    def set(self):
        """

        Set the raw configuration passed by the user.

        """
        pass

