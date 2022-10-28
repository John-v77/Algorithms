def string_builder(string):
    final_string_list = []
    string="string to add"

    for i in range(5):
        final_string_list.append(string)
    
    response = " ".join(final_string_list)
    return response