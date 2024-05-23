import subprocess

def separate_with_demucs(audio_path, model_name='mdx_extra_q'):
    command = [
        'python', '-m', 'demucs.separate',
        '-n', model_name,
        audio_path
    ]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode == 0:
        print("Separation completed successfully.")
        print(result.stdout)
    else:
        print("Error in separation process:")
        print(result.stderr)

# Example usage
audio_path = 'C:/path/to/audio/file.mp3'
separate_with_demucs(audio_path)
