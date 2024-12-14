# Author Class
class Author:
    def __init__(self, name):
        self.name = name
        self._contracts = []  # Private list to store contracts for this author
        self._books = []  # Private list to store books for this author

    def contracts(self):
        """Returns a list of contracts associated with this author."""
        return self._contracts

    def books(self):
        """Returns a list of books that this author has signed contracts for."""
        return [contract.book for contract in self._contracts]

    def sign_contract(self, book, date, royalties):
        """Creates and returns a new contract for this author."""
        contract = Contract(self, book, date, royalties)
        return contract

    def total_royalties(self):
        """Returns the total royalties the author has earned from all their contracts."""
        return sum(contract.royalties for contract in self._contracts)

    # Override __eq__ to compare Authors by their name attribute
    def __eq__(self, other):
        if isinstance(other, Author):
            return self.name == other.name
        return False

# Book Class
class Book:
    def __init__(self, title):
        self.title = title
        self._contracts = []  # Private list to store contracts for this book

    def contracts(self):
        """Returns a list of contracts associated with this book."""
        return self._contracts

    def authors(self):
        """Returns a list of authors that have signed contracts for this book."""
        return [contract.author for contract in self._contracts]

    # Override __eq__ to compare Books by their title attribute
    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title
        return False

# Contract Class
class Contract:
    contracts_list = []  # Class-level list to keep track of all Contract instances

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of the Author class.")
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of the Book class.")
        if not isinstance(date, str):
            raise Exception("Date must be a string.")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer.")
        
        self.author = author  # The author of the book
        self.book = book  # The book the contract is associated with
        self.date = date  # The date when the contract was signed
        self.royalties = royalties  # Royalties percentage
        
        author._contracts.append(self)  # Add contract to author's contract list
        book._contracts.append(self)  # Add contract to book's contract list
        Contract.contracts_list.append(self)  # Add contract to class-level contracts list

    @classmethod
    def contracts_by_date(cls, date):
        """Returns all contracts that were signed on a specific date, sorted by date."""
        filtered_contracts = [contract for contract in cls.contracts_list if contract.date == date]
        sorted_contracts = sorted(filtered_contracts, key=lambda contract: contract.date)
        return sorted_contracts

    # Override __eq__ to compare Contracts by their attributes
    def __eq__(self, other):
        if isinstance(other, Contract):
            return (self.author == other.author and
                    self.book == other.book and
                    self.date == other.date and
                    self.royalties == other.royalties)
        return False

# Testing the functionality
def test_contract_contracts_by_date():
    """Test Contract class has method contracts_by_date() that sorts all contracts by date"""
    Contract.contracts_list = []  # Reset contracts list for the test
    author1 = Author("Name 1")
    author2 = Author("Name 2")
    
    book1 = Book("Title 1")
    book2 = Book("Title 2")
    book3 = Book("Title 3")
    book4 = Book("Title 4")
    
    # Create contracts
    contract1 = Contract(author1, book1, "02/01/2001", 10)
    contract2 = Contract(author1, book2, "01/01/2001", 20)
    contract3 = Contract(author1, book3, "03/01/2001", 30)
    contract4 = Contract(author2, book4, "01/01/2001", 40)

    # Test contracts by date
    contracts_on_01_01_2001 = Contract.contracts_by_date("01/01/2001")
    
    # The order should be contract2 and contract4, sorted lexicographically by date
    assert contracts_on_01_01_2001 == [contract2, contract4]

    # Print to verify (optional)
    for contract in contracts_on_01_01_2001:
        print(f"Contract with {contract.author.name} for {contract.book.title} on {contract.date} with {contract.royalties}% royalties")

# Run the test
test_contract_contracts_by_date()
