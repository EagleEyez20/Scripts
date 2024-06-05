# This function updates the Ollama client by fetching a list of Ollama models and updating each one.
function update_ollama_models: any
        echo "Updating Ollama client..."
        curl  -fsSL https://ollama.com/install.sh | sh 
    
    if not type -q ollama
        echo "Ollama command could not be found. Please check the installation."
        return 1
    end
    
    set -l ollama_proc (ps aux | grep '(o)llama serve')
    if test -z "$ollama_proc"
        echo "Ollama is not running. Starting Ollama serve..."
        ollama serve &
    else
        echo "Ollama serve is already running."
    end
        
    echo "Fetching list of Ollama models..."
    set -l jobs
    ollama list | tail -n +2 | while read -l line
        set model_name (echo $line | awk '{print $1}')
        if test -n "$model_name"
            echo "Attempting to update model: $model_name"
            ollama pull $model_name &
            set -a jobs $last_pid
           echo "Starting update for model: $model_name"
        else
            echo "No model name extracted from line: $line"
        end
    end
    
    for job in $jobs
        wait $jobs
    end
    
    
    
    
    
    