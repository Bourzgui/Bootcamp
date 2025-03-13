class Pagination:
    def __init__(self, items=None, pageSize=10):
        self.items = items if items else []
        self.pageSize = int(pageSize) 
        self.totalPages = max(1, (len(self.items) + self.pageSize - 1) // self.pageSize)
        self.currentPage = 1   

    def getVisibleItems(self):
        """Retourne les éléments visibles sur la page actuelle."""
        start = (self.currentPage - 1) * self.pageSize
        end = start + self.pageSize
        return self.items[start:end]

    def nextPage(self):
        """Passe à la page suivante si possible."""
        if self.currentPage < self.totalPages:
            self.currentPage += 1
        return self   

    def prevPage(self):
        """Revient à la page précédente si possible."""
        if self.currentPage > 1:
            self.currentPage -= 1
        return self  

    def firstPage(self):
        """Va à la première page."""
        self.currentPage = 1
        return self   

    def lastPage(self):
        """Va à la dernière page."""
        self.currentPage = self.totalPages
        return self   

    def goToPage(self, pageNum):
        """Va à la page spécifiée (corrige si elle est hors limites)."""
        pageNum = int(pageNum)   
        if pageNum < 1:
            self.currentPage = 1
        elif pageNum > self.totalPages:
            self.currentPage = self.totalPages
        else:
            self.currentPage = pageNum
        return self   


# Test 
alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.getVisibleItems())  # ["a", "b", "c", "d"]

p.nextPage()
print(p.getVisibleItems())  # ["e", "f", "g", "h"]

p.lastPage()
print(p.getVisibleItems())  # ["y", "z"]

p.firstPage().nextPage().nextPage()
print(p.getVisibleItems())  # ["i", "j", "k", "l"]

p.goToPage(10)
print(p.getVisibleItems())  # ["y", "z"]

p.goToPage(-5)
print(p.getVisibleItems())  # ["a", "b", "c", "d"]
