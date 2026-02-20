from pydiscourse import DiscourseClient

# Configuration
url = "https://www.isharkfly.com/"
api_username = "honeymoose"
api_key = "****"

client = DiscourseClient(
    url,
    api_username=api_username,
    api_key=api_key
)

try:
    user = client.create_user(
        name="shan",
        username="shanouyang",
        email="867611216@qq.com",
        password="AnotherSecurePassword!",
        active=True,
        approved=True
    )
    print(f"User created: {user['message']}")

except Exception as e:
    print(f"Error creating user: {e}")