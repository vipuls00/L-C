def find_element_index_in_list(input_list, search_value):
    try:
        return input_list.index(search_value)
    except ValueError:
        return -1  


def calculate_average_of_sublist(input_list, min_value, max_value):
    min_value_index = find_element_index_in_list(input_list, min_value)
    max_value_index = find_element_index_in_list(input_list, max_value)

    if min_value_index == -1 or max_value_index == -1:
        return "Error: One or both of the specified values are not found in the list."

    if min_value_index > max_value_index:
        min_value_index, max_value_index = max_value_index, min_value_index

    if min_value_index <= max_value_index:  
        sublist = input_list[min_value_index: max_value_index + 1]
        if sublist:  
            sublist_sum = sum(sublist)
            sublist_length = len(sublist)
            return sublist_sum // sublist_length
        else:
            return "Error: No elements found in the sublist."
    else:
        return "Error: Invalid range. The min_value_index should be less than or equal to the max_value_index."


def handle_multiple_queries_on_list(input_list, queries_list):
    for query_min_value, query_max_value in queries_list:
        result = calculate_average_of_sublist(input_list, query_min_value, query_max_value)
        print(f"Average for query ({query_min_value}, {query_max_value}) is: {result}")


def get_input():
    try:
        total_elements_in_list = int(input('Enter the total number of elements in the list: '))
        input_list = list(map(int, input("Enter the comma-separated list of elements: ").split(',')))

        if len(input_list) != total_elements_in_list:
            print("Error: The number of elements in the list does not match the specified total.")
            return None, None

        total_queries_to_process = int(input('Enter the total number of queries to process: '))
        queries_list = [tuple(map(int, input('Enter query (min_value, max_value): ').split(','))) for _ in range(total_queries_to_process)]

        return input_list, queries_list

    except ValueError:
        print("Error: Invalid input format. Please enter integer values only.")
        return None, None


def main():
    input_list, queries_list = get_input()

    if input_list is not None and queries_list is not None:
        handle_multiple_queries_on_list(input_list, queries_list)


if __name__ == "__main__":
    main()
