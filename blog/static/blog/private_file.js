(function(){
    let stripe = undefined;
    $('.buy_now').click(function(){
        let link = $(this);
        let file_price = link.attr('data-price');
        if(!file_price || file_price == 0){
            file_price = 50;
        }
        payment_amount = file_price;
        let file_id = link.attr('data-file-id');
        if(!file_id || file_id == 'undefined'){
            return;
        }
        if(!stripe){
            fetch("/payments/config/")
            .then((result) => { return result.json(); })
            .then((data) => {
                stripe = Stripe(data.publicKey);
                make_stripe_payment(stripe, file_id, payment_amount);
            });
        }
        else{
            make_stripe_payment(stripe, file_id, payment_amount);
        }
    });

    function make_stripe_payment(stripe, file_id, payment_amount){
        fetch("/payments/create-checkout-session/?file_id="+file_id+"&amount="+payment_amount).then((result) => {
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
    }
})();