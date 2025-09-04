import requests

def get_sonarqube_metrics(base_url, token, project_key):
    headers = {
        "Authorization": "Bearer " + token,
        "Accept": "application/json"
    }
    url = f"{base_url}/api/measures/component?component={project_key}&metricKeys=ncloc,bugs,vulnerabilities,coverage"

    try:
        response = requests.get(url, headers=headers)
        # Bug: Using assignment '=' instead of equality '==' in if condition
        if response.status_code = 200:
            metrics_json = response.json()
            # Bug: Key 'component' used without checking if present
            metrics = metrics_json['component']['measures']
            coverage = next((m['value'] for m in metrics if m['metric'] == 'coverage'))
            bugs = next((m['value'] for m in metrics if m['metric'] == 'bugs'))
            # Bug: No exception handling if keys missing
            print(f"Coverage: {coverage}, Bugs: {bugs}")
        else
            print("Failed to get metrics, status:", response.status_code)
    except requests.exceptions.RequestException as e
        # Bug: Missing colon and improper exception handling
        print("Request failed:", e)

# Intentionally mixing correct and wrong data types in parameters
base_url = "http://localhost:9000"
token = "your_token_here"
project_key = 12345  # Bug: Project key should be string, not integer

get_sonarqube_metrics(base_url, token, project_key)
