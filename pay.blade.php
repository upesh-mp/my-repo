@extends('front.templates.app.default')

@section('head')
<title>Payment</title>
<style>
.StripeElement {
    background-color: #edefef;
    height: 45px;
    padding: 13px 12px;
    border-radius: 2px;
    border: 1px solid transparent;
    box-shadow: none;
}

.StripeElement--focus {
    box-shadow: none;
    outline: none;
    border: 2px solid #007fff;
}

.StripeElement--invalid {
    border-color: #fa755a;
}

.StripeElement--webkit-autofill {
    background-color: #fefde5 !important;
}

.payment-form {
    background-color: #fff;
    border-radius: 4px;
    padding: 20px;
    margin-top: 40px;
    margin-bottom: 10px;
    box-shadow: 2px 4px 4px 0 rgba(0,0,0,0.05);
}

.stripe {
    margin-bottom: 80px;
    text-align: center;
    font-size: 13px;
    font-weight: bold;
}
.stripe a { color: #08c }
h5 { font-size: 15px }
#card-errors {
    color: red;
    font-size: 14px;
}
</style>
@endsection


@section('body')
    <section class="container pt-80">
        <div class="row">
            <div class="col-sm-4 col-sm-offset-4">
                @include('errors.list')

                <div class="payment-form">
                    <h4 class="text-center pb-5">Total Due: <strong>AUD {{ $fees->amount }}</strong></h4>
                    <h5 class="text-center pb-20">Pay with credit or debit card</h5>

                    <form class="form" action="" method="post" id="payment-form">
                        {!! csrf_field() !!}
                        <div class="form-row">
                            <div id="card-element"></div>
                            <div id="card-errors" role="alert"></div>
                        </div>

                        <button class="btn btn-lg btn-block btn-primary mt-40 elevated">
                            Pay Now
                        </button>
                    </form>
                </div>

                <div class="stripe">
                    Secure payments with <a href="https://stripe.com" target="_blank">Stripe</a>
                </div>
            </div>
        </div>
    </section>
@endsection



@section('js')
<script src="https://js.stripe.com/v3/"></script>
<script>
$(document).ready(function () {
    var stripe = Stripe('pk_live_5fwhiqKFqInr9A783ebI3Hzq')
    var elements = stripe.elements()

    var style = {
        base: {
            color: '#32325d',
            lineHeight: '18px',
            fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
            fontSmoothing: 'antialiased',
            fontSize: '16px',
            '::placeholder': {
                color: '#aab7c4'
            }
        },
        invalid: {
            color: '#fa755a',
            iconColor: '#fa755a'
        }
    }

    var card = elements.create('card', { style })
    card.mount('#card-element')

    card.addEventListener('change', function(event) {
        var displayError = document.getElementById('card-errors');
        if (event.error) {
            displayError.textContent = event.error.message;
        } else {
            displayError.textContent = '';
        }
    })

    var form = document.getElementById('payment-form');
    form.addEventListener('submit', function(event) {
        event.preventDefault();

        stripe.createToken(card)
        .then(function(result) {
            if (result.error) {
                var errorElement = document.getElementById('card-errors');
                errorElement.textContent = result.error.message;
            } else {
                stripeTokenHandler(result.token);
            }
        })
    })


    function stripeTokenHandler(token) {
        var form = document.getElementById('payment-form')
        var hiddenInput = document.createElement('input')
        hiddenInput.setAttribute('type', 'hidden')
        hiddenInput.setAttribute('name', 'stripeToken')
        hiddenInput.setAttribute('value', token.id)
        form.appendChild(hiddenInput)
        form.submit()
    }
})
</script>
@endsection
