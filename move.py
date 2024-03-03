class Move:
    """
    move class containing a start row and start column as well as an end row and end column
    """
    def __init__(self, from_row, from_col, to_row, to_col):
        """
        Initialize the start and end locations
        :param from_row: starting row
        :param from_col: starting col
        :param to_row: end row
        :param to_col: end col
        """
        self.from_row = from_row
        self.from_col = from_col
        self.to_row = to_row
        self.to_col = to_col

    def __str__(self):
        """
        Output string of the move with start and end row/col
        :return: output
        """
        output = f'Move [from_row={self.from_row}, from_col={self.from_col}'
        output += f', to_row={self.to_row}, to_col={self.to_col}]'
        return output	
