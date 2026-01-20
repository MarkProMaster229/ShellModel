import importlib.util

class Dowlound:

    def uploadfileModel(file_path):

        spec = importlib.util.spec_from_file_location("My_Model", file_path)
        modelUser = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(modelUser)
        return modelUser
    