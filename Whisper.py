import whisper
import os
import time

models = ["tiny", "base", "small", "medium"]
audio_file = "Operating system.wav"

output_folder = "Transcription"
os.makedirs(output_folder, exist_ok=True)

for model_name in models:
    print(f"Processing with model: {model_name}...")

    start_time = time.time()
    model = whisper.load_model(model_name)

    result = model.transcribe(audio_file)
    end_time = time.time()

    latency = end_time - start_time
    print(f"Model {model_name} completed transcription in {latency:.2f} seconds.")

    output_path = os.path.join(output_folder, f"{model_name}_transcription.txt")
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(result["text"])

    print(f"Transcription saved to {output_path}")

print("All transcriptions completed.")
