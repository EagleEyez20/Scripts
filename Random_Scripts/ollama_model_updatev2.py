import subprocess

def update_ollama_models():
    print("Updating Ollama client...")

    # Install Ollama if not installed
    subprocess.run(["curl", "-fsSL", "https://ollama.com/install.sh", "|", "sh"])

    # Check if Ollama command is available
    if subprocess.run(["which", "ollama"], capture_output=True).returncode != 0:
        print("Ollama command could not be found. Please check the installation.")
        return 1

    # Check if Ollama serve is running
    ollama_proc = subprocess.run(["ps", "aux"], capture_output=True, text=True)
    if "ollama serve" not in ollama_proc.stdout:
        print("Ollama is not running. Starting Ollama serve...")
        subprocess.Popen(["ollama", "serve"])

    print("Fetching list of Ollama models...")
    models = subprocess.run(["ollama", "list"], capture_output=True, text=True).stdout.splitlines()[1:]
    jobs = []
    for model_name in models:
        if model_name:
            print(f"Attempting to update model: {model_name}")
            subprocess.Popen(["ollama", "pull", model_name])
            jobs.append(model_name)
            print(f"Starting update for model: {model_name}")
        else:
            print(f"No model name extracted from line: {model_name}")

    for job in jobs:
        subprocess.run(["wait", job])