import logging
import os


class CommonHelpers(object):
    @staticmethod
    def get_logger(log_file_path, log_file):
        """
        Gets logger

        :param str log_file_path: log file path
        :param str log_file: log file

        :returns logger
        """
        logger = logging.getLogger()
        if not os.path.isdir(log_file_path):
            os.makedirs(log_file_path)
        file_logging_formatter = logging.Formatter('%(asctime)s %(name)s %(message)s')
        file_handler = logging.FileHandler(filename='{log_file_path}/{log_file}'.format(
            log_file_path=log_file_path, log_file=log_file
        ))
        file_handler.suffix = '%Y-%m-%d'
        file_handler.setFormatter(file_logging_formatter)
        file_handler.setLevel(logging.INFO)
        # apm_handler = LoggingHandler(client=self.apm_client)
        # apm_handler.setLevel(logging.ERROR)
        # apm_handler.setFormatter(file_logging_formatter)
        file_handler.suffix = '%Y-%m-%d'
        logger.addHandler(file_handler)
        # logger.addHandler(apm_handler)
        return logger
