import os


class DataTrustsError(Exception):
    def __init__(self, message):
        self.message = message


class TrustContextError(DataTrustsError):
    pass


class ConfigNotFoundError(TrustContextError):
    def __init__(self, context_root_directory):
        self.message = "No configuration found in %s" % str(os.path.join(context_root_directory, "data_trust"))


class ExpectationSuiteNotFoundError(DataTrustError):
    def __init__(self, data_asset_name):
        self.data_asset_name = data_asset_name
        self.message = "No expectation suite found for resource_name %s" % resource_name


class BatchKwargsError(TrustContextError):
    def __init__(self, message, batch_kwargs):
        self.message = message
        self.batch_kwargs = batch_kwargs