def current_user(user):
    # Access the current user object
    user = request.user

    if user.is_authenticated:
        # User is logged in
        return HttpResponse(f"Hello, {user.username}!")
    else:
        # User is not logged in
        return HttpResponse("Hello, anonymous user!")