def get_redirect_url(params, default='work page'):
    redirect_url = params.get('return_url')
    return redirect_url if redirect_url else default
