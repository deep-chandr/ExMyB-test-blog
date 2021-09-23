from blog.models import UserToken



def check_auth(request):
    # print('here: ', request.query_params)
    #
    # query_params= dict(request.query_params)

    print('request.headers: ', request.headers)

    token = authorization = request.headers.get('Authorization')
    print('authorization: ', authorization)
    if authorization:
        # token = authorization[0]
        token = token.split(' ')

        print('token------', token[0])
        print('token------',  token[1])
        try:
            user_token = UserToken.objects.get(user__username=token[0], token=token[1] )
            request.user = user_token.user
            return user_token.user
        except UserToken.DoesNotExist:
            return None

    return None