function make_stripe_payment(payment_amount){
    fetch("/payments/config/")
    .then((result) => { return result.json(); })
    .then((data) => {
        const stripe = Stripe(data.publicKey);
        fetch("/payments/create-checkout-session/?amount="+payment_amount).then((result) => {
            console.log(result);
            result = result.json();
            return result;
        }).then((data) => {
            if(data.error){
                throw data.error;
            }
            data = { sessionId: data.sessionId };
            data = stripe.redirectToCheckout(data);
            return data;

        }).then((res) => {
            console.log(res);
        }).catch(function (er) {
            console.log('error ', er);
        });
    });
}
alert('file opened, now closing');
window.close();
