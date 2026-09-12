from demo.app import app


def test_component_gallery_renders_every_issue_component():
    response = app.test_client().get("/")

    assert response.status_code == 200
    assert b"Jinjalume component gallery" in response.data
    assert b"<select" in response.data
    assert b"data-theme=\"light\"" in response.data
    assert b"Use dark mode" in response.data


def test_ui_block_routes_render_realistic_screens():
    client = app.test_client()

    blocks = client.get("/blocks")
    login = client.get("/login")
    signup = client.get("/signup")
    admin = client.get("/admin")

    assert blocks.status_code == 200
    assert b"Realistic UI blocks" in blocks.data
    assert login.status_code == 200
    assert b' action="/login"' in login.data
    assert b'name="remember"' in login.data
    assert b'autocomplete="current-password"' in login.data
    assert signup.status_code == 200
    assert b' action="/signup"' in signup.data
    assert b'name="password_confirmation"' in signup.data
    assert b'autocomplete="new-password"' in signup.data
    assert admin.status_code == 200
    assert b"Recent orders" in admin.data
    assert b"Recent activity" in admin.data
    assert b'aria-current="page"' in admin.data


def test_login_block_renders_validation_and_success_states():
    client = app.test_client()

    invalid = client.post("/login", data={"email": "", "password": ""})
    valid = client.post(
        "/login",
        data={"email": "alex@example.com", "password": "secret", "remember": "1"},
    )

    assert invalid.status_code == 200
    assert b"Review the fields below" in invalid.data
    assert b'aria-invalid="true"' in invalid.data
    assert valid.status_code == 200
    assert b"Demo sign-in accepted" in valid.data


def test_signup_block_renders_validation_and_success_states():
    client = app.test_client()

    invalid = client.post(
        "/signup",
        data={
            "name": "Alex",
            "email": "alex@example.com",
            "password": "short",
            "password_confirmation": "different",
        },
    )
    valid = client.post(
        "/signup",
        data={
            "name": "Alex Morgan",
            "email": "alex@example.com",
            "password": "correct-horse",
            "password_confirmation": "correct-horse",
            "terms": "1",
        },
    )

    assert invalid.status_code == 200
    assert b"Passwords must match" in invalid.data
    assert b"Accept the terms" in invalid.data
    assert b'aria-describedby="terms-error"' in invalid.data
    assert valid.status_code == 200
    assert b"Demo account created" in valid.data


def test_htmx_route_has_a_plain_form_fallback():
    response = app.test_client().post("/htmx", data={"message": "Hello"})

    assert response.status_code == 200
    assert b"Progressive enhancement with HTMX" in response.data
    assert b"Received: Hello" in response.data
    assert b"hx-post=" in response.data


def test_htmx_request_returns_only_the_target_fragment():
    response = app.test_client().post(
        "/htmx",
        data={"message": "Hello"},
        headers={"HX-Request": "true"},
    )

    assert response.status_code == 200
    assert b"<html" not in response.data
    assert b'role="alert"' in response.data
    assert b"Received: Hello" in response.data


def test_htmx_request_reports_empty_messages():
    response = app.test_client().post(
        "/htmx",
        data={"message": ""},
        headers={"HX-Request": "true"},
    )

    assert response.status_code == 200
    assert b"Message required" in response.data
