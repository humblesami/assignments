console.log("Sanity check!");

fetch("/payments/config/")
.then((result) => { return result.json(); })
.then((data) => {
  // Initialize Stripe.js
  const stripe = Stripe(data.publicKey);
  console.log(stripe);
  document.querySelector("#submitBtn").addEventListener("click", () => {
    // Get Checkout Session ID
    fetch("/payments/create-checkout-session/")
    .then((result) => {
     console.log(result);
     result = result.json();
     console.log(result);
     return result;
     })
    .then((data) => {
      console.log(data);
      // Redirect to Stripe Checkout
      if(data){
        data = {sessionId: data.sessionId};
        data = stripe.redirectToCheckout(data);
        return data;
      }
    })
    .then((res) => {
      console.log(res);
    }).catch(function(er){
        console.log('error ', er);
    });
  });
});