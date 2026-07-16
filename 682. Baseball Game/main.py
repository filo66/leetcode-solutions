class Solution:
    def calPoints(self, operations: list[str]) -> int:
        record = []
        for i , operation in enumerate(operations):
            try:
                operation = int(operation)
                record.append(operation)
            except:
                if operation == "+" and len(record) >= 2:
                    record.append(record[-1]+record[-2])
                elif operation == "D":
                    record.append(record[-1]*2)
                elif operation == "C":
                    record.pop(-1)
        
        return sum(record)
