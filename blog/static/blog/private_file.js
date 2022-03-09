(function(){
    let stripe = undefined;
    $('.buy_now').click(function(){
        let link = $(this);
        let file_price = link.attr('data-price');
        if(!file_price || file_price == 0){
            file_price = 50;
        }
        else if(file_price < 50){
            file_price *= 50;
        }
        payment_amount = file_price;
        let file_id = link.attr('data-file-id');
        if(!file_id || file_id == 'undefined'){
            return;
        }
        let page_number = link.attr('data-page');
        if(!page_number || page_number == 'undefined'){
            page_number = 1;
        }
        let payment_params = {
            page_number: page_number,
            file_id: file_id,
            payment_amount: payment_amount,
        }
        if(!stripe){
            fetch("/payments/config/")
            .then((result) => { return result.json(); })
            .then((data) => {
                stripe = Stripe(data.publicKey);
                make_stripe_payment(stripe, payment_params);
            });
        }
        else{
            make_stripe_payment(stripe, payment_params);
        }
    });

    function make_stripe_payment(stripe, payment_params){
        fetch("/payments/create-checkout-session/?page="+payment_params.page_number+"&file_id="+payment_params.file_id+"&amount="+payment_params.payment_amount).then((result) => {
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