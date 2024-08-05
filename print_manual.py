from color_mapping import get_color_from_pair_number

def print_color_code_manual():
    for i in range(1, 26):
        major_color, minor_color = get_color_from_pair_number(i)
        print(f"{i}: {major_color} - {minor_color}")

if __name__ == '__main__':
    print_color_code_manual()
