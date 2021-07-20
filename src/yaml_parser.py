from yaml import FullLoader, load


def yaml_load(path: str):
    try:
        with open(r"{}".format(path)) as file:
            data = load(file, Loader=FullLoader)
            return data
    except Exception as error:
        print(error)
        return None
