def view_recursive_list(data, index):
    
    """ Recursitive created for a list reader
    
    Args:
    data [list] != 0
    index [int] == 0
    
    Returns:
    int > 0 to 'index'

    """
    
    if index != len(data):
        """ 'if' loop to 
        """
        print(data[index]) # return data (int) in console
        # print(type(data [index])) # return data type in console
        view_recursive_list(data, index + 1)

data = [1,2,3,4,5] # list
view_recursive_list(data, 0) # call to function