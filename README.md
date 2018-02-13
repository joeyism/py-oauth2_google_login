# oauth2_google_login
Gets OAuth2 access token from Google/YouTube automatically, using [requests_oauthlib](https://github.com/requests/requests-oauthlib)

## Installation

```bash
pip3 install --user oauth2_google_login
```

## Usage

### With Default Chrome Webdriver
First, setup Chrome Webdriver so that it is in PATH, which can be done in terminal

```bash
export PATH=$PATH:/home/username/Downloads/chromedriver
```

Then in Python, run

```python
from oauth2_google_login import get_access_token

auth = get_access_token(
    email = "user@email.com",
    password = "password",
    client_id="1234567",
    client_secret="a1b2c3d4e5",
    scope = ['https://www.googleapis.com/auth/yt-analytics.readonly', "https://www.googleapis.com/auth/youtube.readonly"]
    )

auth.access_token # Facebook access token
```

### With Custom Webdriver

```python
from oauth2_google_login import get_access_token
from selenium import webdriver

driver = webdriver.Chrome("/home/username/Downloads/chromedriver")

auth = get_access_token(
    email = "user@email.com",
    password = "password",
    client_id="1234567",
    client_secret="a1b2c3d4e5",
    scope = ['https://www.googleapis.com/auth/yt-analytics.readonly', "https://www.googleapis.com/auth/youtube.readonly"],
    driver = driver
    )

auth.access_token # Facebook access token
```

## Versions

**1.0.x**
* First Publish
