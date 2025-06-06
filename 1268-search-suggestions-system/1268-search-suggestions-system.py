class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        res = []
        products.sort() # then we can use two pointers and ans should be in lexicographical order

        l, r = 0, len(products) - 1

        for i in range(len(searchWord)):
            c = searchWord[i] # check the value at index

            # looking for the product which match with char c as the result will be from left to right index
            while l <= r and (len(products[l]) <= i or products[l][i] != c):
                l += 1
            # if dont match then move to next or prev value using pointers
            # len(products[r]) <= i : imp check otherwise products[r][i] can lead to index not found

            while l <= r and (len(products[r]) <= i or products[r][i] != c):
                r -= 1

            res.append([])
            remain = r - l + 1 # all words within l to r satisfy the c matching cond

            for j in range(min(3, remain)): # max only 3 can be taken 
                res[-1].append(products[l + j]) # found matching products in the range

        return res