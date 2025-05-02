def get_num_words(string_array):
    count = len(string_array)
    return count


def count_characters(strings):
    data = {}
    for c in strings:
        c = c.lower()
        if c in data:
            data[c] += 1
        else:
            data[c] = 1
    sorted_data = sort_result(data)
    return sorted_data


def sort_result(data):
    def sort_on(dict):
        return dict["num"]

    data_array = []
    for d in data:
        if d.isalpha():
            data_array.append({"char": d, "num": data[d]})
    data_array.sort(reverse=True, key=sort_on)
    return data_array
