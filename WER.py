import jiwer

base_path = "//Transcription/"
transcription_files = [
    "tiny_transcription.txt",
    "base_transcription.txt",
    "small_transcription.txt",
    "medium_transcription.txt",
]
reference_file = base_path + "ref_transcription.txt"

with open(reference_file, "r", encoding="utf-8") as ref_file:
    reference_text = ref_file.read().strip()

wer_results = {}
for transcription_file in transcription_files:
    full_path = base_path + transcription_file
    with open(full_path, "r", encoding="utf-8") as model_file:
        model_text = model_file.read().strip()

    wer = jiwer.wer(reference_text, model_text)
    wer_results[transcription_file] = wer

for model, wer in wer_results.items():
    print(f"Model ({model}): WER = {wer:.2%}")
