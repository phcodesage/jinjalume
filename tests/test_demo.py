from demo.app import app


def test_component_gallery_renders_every_issue_component():
    response = app.test_client().get("/")

    assert response.status_code == 200
    assert b"Jinjalume component gallery" in response.data
    assert b"<select" in response.data
    assert b"data-theme=\"light\"" in response.data
    assert b"Use dark mode" in response.data


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
