from func import open_json_file, sort_dict, get_executed, result_dict


def main():
    dict_json = open_json_file()
    dict_sort = sort_dict(dict_json)
    dict_list = get_executed(dict_sort)
    print(result_dict(dict_list))


if __name__ == "__main__":
    main()
