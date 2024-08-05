import test_color_mapping
import print_manual

if __name__ == '__main__':
    test_color_mapping.test_number_to_pair(4, 'White', 'Brown')
    test_color_mapping.test_number_to_pair(5, 'White', 'Slate')
    test_color_mapping.test_pair_to_number('Black', 'Orange', 12)
    test_color_mapping.test_pair_to_number('Violet', 'Slate', 25)
    test_color_mapping.test_pair_to_number('Red', 'Orange', 7)
    
    print('All tests passed!')

    # Print the color code manual
    print_manual.print_color_code_manual()
