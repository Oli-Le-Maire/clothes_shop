class InterfaceText():

    def home_page(self):
        return """
        <html>
        <body>

            <h1>Clothes Shop</h1>

                <p1>Welcome to Oli\'s Clothes Shop!!!
                We\'ve only just started up so our website is
                very much still in development, so please bare with us.<br><br>
                Please type what you would like to do: Browse   or
                View Basket :-)<p1>

                <form method="POST" enctype="multipart/form-data" action="/search-results">
                <input name="search" type="text" placeholder="Enter your search here">
                <input type="submit" value="Browse"></form>

                <form method="POST" enctype="multipart/form-data" action="/view-basket">
                <input type="submit" value="View Basket"></form>

        </body>
        </html>
        """

    def search_results(self, input='nothing'):
        return """
        <html>
        <body>

            <h1>Search Results</h1>

                <p1>Your search returned %s <p1>

        </body>
        </html>
        """ % input

    def view_basket(self):
        return """
        <html>
        <body>

            <h1>View Basket</h1>

                <p1>Your basket is empty<p1>

        </body>
        </html>
        """
