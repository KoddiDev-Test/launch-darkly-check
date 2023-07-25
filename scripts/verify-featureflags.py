import os
import requests

def main():
    # Fetch necessary environment variables
    project_key = os.getenv("PROJECT_KEY")
    env1 = os.getenv("ENV1")
    env2 = os.getenv("ENV2")
    api_key = os.getenv("API_KEY")
    url = os.getenv("URL")

    headers = {"Authorization": api_key}

    try:
        response = requests.get(url + project_key, headers=headers)
        response.raise_for_status()
        data = response.json()

        # Iterate through data to find the flag
        failed_items = []
        for item in data["items"]:
            env1_flag = item["environments"][env1]["on"]
            env2_flag = item["environments"][env2]["on"]
            is_match = (env1_flag == env2_flag)
            if not is_match:
                print(f"Flag failed to match: {item['name']} ({env1}: {env1_flag} | {env2}: {env2_flag})")
                failed_items.append(item["name"])

        # Check if anything failed
        if failed_items:
            print("Some flags failed to match!")
            exit(1)
        else:
            print(f"{env1} and {env2} flags match!")

    except requests.exceptions.RequestException as e:
        print("Error occurred during the API request:", e)
        exit(1)

if __name__ == "__main__":
    main()
