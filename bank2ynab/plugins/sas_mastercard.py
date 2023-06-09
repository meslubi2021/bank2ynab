from bank_handler import BankHandler
import pandas as pd


class SAS_Mastercard(BankHandler):
    def __init__(self, config_dict: dict):
        """
        :param config_object: a dictionary of conf parameters
        """
        super().__init__(config_dict)
        self.name = "SAS EuroBonus World Mastercard"

    def _preprocess_file(self, file_path: str, plugin_args: list) -> str:
        """
        This is probably the only method you really want to override.
        exists solely to be used by plugins for pre-processing a file
        that otherwise can be read normally (e.g. weird format)
        :param file_path: path to file
        """
        try:
            df = pd.read_excel(file_path, engine="xlrd")
            df.to_csv(file_path, sep=";", index=False)
        except ImportError as e:
            raise ImportError(
                "The SAS_Mastercard plugin requires the excel engine xlrd to be installed. Please run pip install xlrd."
            )

        return file_path


def build_bank(config):
    """This factory function is called from the main program,
    and expected to return a B2YBank subclass.
    Without this, the module will fail to load properly.

    :param config: dict containing all available configuration parameters
    :return: a B2YBank subclass instance
    """
    return SAS_Mastercard(config)
