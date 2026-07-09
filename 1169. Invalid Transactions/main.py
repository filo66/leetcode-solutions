class Solution:
    def invalidTransactions(self, transactions: list) -> list:
        invalid = set()

        lists = []

        for i in range(len(transactions)):
            arr = transactions[i].split(",")

            arr[1] = int(arr[1])
            arr[2] = int(arr[2])
            lists.append(arr)

            if arr[2] > 1000 :
                invalid.add(i)

        for i in range(len(transactions)):
            for j in range(i+1 , len(transactions)):
                if lists[i][0] == lists[j][0]:
                    try:
                        assert lists[i][3] != lists[j][3]
                        assert abs(lists[i][1] - lists[j][1]) <= 60
                        invalid.add(i) 
                        invalid.add(j) 
                    except:
                        pass
        
        return [transactions[i] for i in sorted(invalid)]
