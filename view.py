class View():

    def home_page(self):
        return F"""
        <html>
        <head>
            <link rel="stylesheet" href="style.css"/>
            <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
        </head>
        <body>

            <h1>Clothes Shop</h1>
                <p1>Welcome to Oli\'s Clothes Shop!!!
                We\'ve only just started up so our website is
                very much still in development, so please bare with us.
                    <br>
                    <br>
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

    def search_results(self, is_stock_there_conditional='Nothing at all'):
        return F"""
        <html>
        <head>
            <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
        </head>
        <body>

            <h1>Search Results</h1>

                <p1>We have the following...<br><p1>
                <p2><br> {is_stock_there_conditional} </p2>

                <form method="POST" enctype="multipart/form-data" action="/">
                <input type="submit" value="Back to Home Page"

        </body>
        </html>
        """

    def view_basket(self):
        return F"""
        <html>
        <head>
            <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
        </head>
        <body>

            <h1>View Basket</h1>

                <p1>Your basket is empty<p1>

                <form method="POST" enctype="multipart/form-data" action="/">
                <input type="submit" value="Back to Home Page"

        </body>
        </html>
        """

# {search_input[1]}: £{search_input[2]}
