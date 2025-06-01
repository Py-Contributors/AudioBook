import requests

def get_incremented_version(package_name: str) -> str:
    
    try:
        url = f"https://pypi.org/pypi/{package_name}/json"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        latest_version = data['info']['version']
        version_parts = latest_version.split('.')
        
        # Convert last part to int and increment
        version_parts[-1] = str(int(version_parts[-1]) + 1)
        
        incremented_version = '.'.join(version_parts)
        return incremented_version
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch version for package '{package_name}': {e}")
    except Exception as e:
        print(f"Error processing version: {e}")

    return "0.0.1"