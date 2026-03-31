import os

config = {
	"api_type": "openai",
	# "api_base": "YOUR_API_BASE_URL",
	# "api_version": "2023-07-01-preview",
	"api_key": os.environ.get("OPENAI_API_KEY", ""),
}