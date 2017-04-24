# Returns the second column y[1] in a sorted arr bound to enumerated values
# which increments a counter from 1++ and multiplies it by the value in the arr
def sort_by_value_and_index(arr):
    return [y[1] for y in sorted(enumerate(arr),key=lambda x:(x[0] + 1) * x[1])]
