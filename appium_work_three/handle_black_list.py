import yaml


def handle_black(fun):
    def run(*args, **kwargs):
        with open('../data/black_list.yaml', 'r') as f:
            black_lists = yaml.safe_load(f)
            try:
                return fun(*args, **kwargs)
            except Exception as msg:
                for black in black_lists:
                    black_count = args[0].driver.find_elements(*black)
                    if len(black_count) > 0:
                        black_count[0].click()
                        return fun(*args, **kwargs)
                raise msg

    return run
