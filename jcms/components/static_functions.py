import warnings


class StaticFunctions:
    """
    Static functions that are used often in the jcms module
    """

    @staticmethod
    def warn(warning: str):
        """
        A central function to warn the user

        :param warning: The warning message for the user
        :type warning: str
        """
        warnings.warn(warning, Warning)


    @staticmethod
    def app_has_attr(app_name, app_data, variable_name: str, variable_type) -> bool:
        """
        Checks if a jcms app has a attribute. If not it warns the user with a nice message

        :param app_name: Name of the jcms app
        :param app_data: data of the specified app
        :param variable_name: Name of the variable that is searched
        :param variable_type: Type of the variable that is searched
        :return: Bool
        """

        has_attribute = hasattr(app_data, variable_name) and isinstance(getattr(app_data, variable_name), variable_type)

        if not has_attribute: StaticFunctions.warn('In app ' + app_name + ': no ' + variable_name + ' in jcms.py found or '
                                                  + variable_name + ' is not instance of ' + variable_type.__name__)

        return has_attribute
