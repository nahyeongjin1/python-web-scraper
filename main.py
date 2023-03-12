from requests import get

websites = [
  "google.com", "twitter.com", "naver.com", "youtube.com", "instagram.com",
  "nomadcoders.co"
]
results = {}

for website in websites:
  if not website.startswith("https://"):
    website = f"https://{website}"
  response = get(website)
  if response.status_code == 200:
    results[website] = "OK"
  else:
    results[website] = "FAILED"

print(results)