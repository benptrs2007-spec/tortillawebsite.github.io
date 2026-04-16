These are the changes to be made:



Create a new page with the same template as the other pages specifically for the Tallow Fried Tortilla Chips, make the more details button on the products page / tallow products page refer to this new Tallow Chip page... Then embed this Paypal add to cart object while keeping the same beautiful ui. Don't change anything else.



The paypal add to cart object:

<paypal-add-to-cart-button data-id="8B7U4DRKB9ZJG"></paypal-add-to-cart-button>

<script>

&#x20; cartPaypal.AddToCart({ id: "8B7U4DRKB9ZJG" })

</script>



Paste this code in your website's <head> (or at the top of your page’s <body> above the Part 2 code) only once per page.



<script src="https://www.paypalobjects.com/ncp/cart/cart.js" data-merchant-id="2Z48U82V2P5H2"></script>





Paste this code in your website's <body> where you want the View Cart button to show up. Make sure it's in a visible place on every page, like the navigation. You can also add it in multiple places.



<paypal-cart-button data-id="pp-view-cart"></paypal-cart-button>

<script>

&#x20; cartPaypal.Cart({ id: "pp-view-cart" })

</script>

