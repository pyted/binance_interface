import traceback
from copy import deepcopy
from pprint import pprint


def get_asset(symbol, base_asset):
    symbol = symbol.strip()
    base_asset = base_asset.strip()
    if base_asset and symbol.endswith(base_asset):
        asset = symbol[0:-len(base_asset)]
        return asset
    else:
        return symbol


def eprint_old(data, length=2):
    """
    Formats and prints the given data in a structured way, compatible with both list and dict types in 'data' field.
    Includes "... ..." to indicate more items in the list.

    Args:
    data (dict): The data to be formatted and printed.
    """
    try:
        texts = []
        texts.append("{")
        for key, value in data.items():
            if key == "data":
                if type(value) == [str, int, float, bool]:
                    texts.append(f" '{key}': {value},\n")
                elif type(value) == list:
                    texts.append(f" '{key}': [")
                    # Check if the first item in data is a list or a dict to determine the format
                    if len(value) == 0:
                        texts[-1] += '],\n'
                    else:
                        texts[-1] += '\n'
                        if isinstance(value[0], dict):
                            # Handling dict format
                            for i, item in enumerate(value):
                                if i == length:  # For the second entry, add ...
                                    texts.append("          ... ...\n")
                                    break
                                texts.append("          {\n")
                                for sub_key, sub_value in item.items():
                                    texts.append(f"           '{sub_key}': {repr(sub_value)},\n")

                                texts.append("          },\n")
                        else:
                            # Handling list format
                            for i, item in enumerate(value):
                                if i == length:  # For the second entry, add ...
                                    texts.append("          ... ...\n")
                                    break
                                texts.append("          [\n")
                                for j, elem in enumerate(item):
                                    end_char = "," if j < len(item) - 1 else ""
                                    texts.append(f"           {repr(elem)}{end_char}\n")
                                texts.append("          ],\n")
                        texts.append("         ]\n")
                elif type(value) == dict:
                    texts.append(" '{key}': {".format(key=key))
                    # Check if the first item in data is a list or a dict to determine the format
                    if len(value) == 0:
                        texts[-1] += '},\n'
                    else:
                        texts[-1] += '\n'
                        if isinstance(value[0], dict):
                            # Handling dict format
                            for i, item in enumerate(value):
                                if i == length:  # For the second entry, add ...
                                    texts.append("          ... ...\n")
                                    break
                                texts.append("          {\n")
                                for sub_key, sub_value in item.items():
                                    texts.append(f"           '{sub_key}': {repr(sub_value)},\n")

                                texts.append("          },\n")
                        else:
                            # Handling list format
                            for i, item in enumerate(value):
                                if i == length:  # For the second entry, add ...
                                    texts.append("          ... ...\n")
                                    break
                                texts.append("          [\n")
                                for j, elem in enumerate(item):
                                    end_char = "," if j < len(item) - 1 else ""
                                    texts.append(f"           {repr(elem)}{end_char}\n")
                                texts.append("          ],\n")
                        texts.append("         ]\n")

                    pass
                else:
                    raise Exception('使用pprint')

            else:
                if key == 'code':
                    texts.append(f"'{key}': {repr(value)},\n")
                elif key == 'msg':
                    texts.append(f" '{key}': {repr(value)},")
                else:
                    texts.append(f" '{key}': {repr(value)},\n")

        texts.append("}")
        print(''.join(texts))
    except:
        print(traceback.format_exc())
        pprint(data)


def get_short_data(data, length, value_omit='......', key_omit='...', ):
    result_data = data
    if type(data) == list:
        if len(data) > length:
            for i in range(length):
                data[i] = get_short_data(data[i], length)
            result_data = data[0:length] + [value_omit, ]
    elif type(data) == dict:
        if len(data) > length:
            result_data = {}
            for i, (sub_key, sub_value) in enumerate(data.items()):
                if i >= length:
                    break
                sub_value = get_short_data(sub_value, length)
                result_data[sub_key] = sub_value
            result_data[key_omit] = value_omit
    return result_data


def eprint(result, length=5, data_length=30, value_omit='......', key_omit='...', width=120):
    result_copy = deepcopy(result)
    if 'data' in result_copy.keys():
        if type(result_copy['data']) == list:
            short_datas = []
            for data in result['data'][0:data_length]:
                short_data = get_short_data(data, length)
                short_datas.append(short_data)
            if len(result['data']) > data_length:
                short_datas.append(value_omit)

        elif type(result_copy['data']) == dict:
            short_datas = {}
            for i, (key, data) in enumerate(result_copy['data'].items()):
                if i > data_length:
                    break
                short_data = get_short_data(data, length)
                short_datas[key] = short_data

            if len(result['data']) > data_length:
                short_datas[key_omit] = value_omit
        else:
            short_datas = result_copy['data']
        result_copy['data'] = short_datas
    pprint(result_copy, sort_dicts=False, width=width)
