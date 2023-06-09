class Operation:

    def __init__(self, id_, date_, state, operation_amount, description, to, from_=None):
        self.id_ = id_
        self.date_ = date_
        self.state = state
        self.operation_amount = operation_amount
        self.description = description
        self.to = to
        if from_:
            self.from_ = from_
        else:
            self.from_ = None

    def __repr__(self):
        return f'Operation(id = {self.id_}, date_ = {self.date_}, state = {self.state}, \
operation_amount = {self.operation_amount}, description = {self.description}, \
from_ = {self.from_}, to = {self.to}'

    def __eq__(self, other):
        if isinstance(other, Operation):
            return (self.id_ == other.id_ and
                    self.date_ == other.date_ and
                    self.state == other.state and
                    self.operation_amount == other.operation_amount and
                    self.description == other.description and
                    self.to == other.to and
                    self.from_ == other.from_)
        return NotImplemented
