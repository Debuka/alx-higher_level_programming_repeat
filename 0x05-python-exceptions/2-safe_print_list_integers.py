#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    i = 0  # Initialize an index variable

    while i < x:
        try:
            # Attempt to print an integer element
            print("{:d}".format(my_list[i]), end=" ")
            count += 1
        except (ValueError, TypeError):
            pass  # Skip non-integer values silently
        except IndexError:
            break  # Handle the case where x is larger than the list

        i += 1

    print()  # Print a newline after all integer values
    return count

# Example usage:
my_list = [1, 2, "3", 4, "5", 6]
x = 4
printed_count = safe_print_list_integers(my_list, x)
print(f"Number of integers printed: {printed_count}")
