import requests

# Constant variables
OUTPUT_DIR = "output/"
SRC_LINK = "video-links.txt"

success_count = 0
count = 0

# Read vid src and download line by line
with open(SRC_LINK, 'r') as file:

    for line in file:

        line = line.strip().replace("https://vt.tiktok.com/", "").replace("/", "")

        download_link = f"https://tikwm.com/api/?url=https%3A%2F%2Fvt.tiktok.com%2F" + line
        print(f'[DEBUG] Downloading file {count} from: {download_link}')

        response = requests.get(download_link).json()
        file_path = OUTPUT_DIR + f'{count}-tiktok.mp4'

        if response.get("code") == 0:
            with open(file_path, 'wb') as file:
                file.write(requests.get(response["data"]["play"]).content)
            print(
                f'File {count} downloaded successfully | Duration: {response["data"]["duration"]} seconds')
            success_count += 1
        else:
            print(f'\n[DEBUG] Response: {response}\n')
            print(f'Failed to download file {count}')

        count += 1


print(f"{success_count}/{count} file(s) downloaded successfully")
