# Whisper Transcription Project

This project implements the **Whisper** speech recognition models (`tiny`, `base`, `small`, and `medium`) to transcribe audio files into text. The transcriptions are stored in the `Transcription` folder. 

- The `Whisper.py` file performs transcription and calculates the **latency** for each model.
- The `WER.py` file computes the **Word Error Rate (WER)** for the outputs of the four models.

## Environment Configuration

The project requires **Python** version **3.8 to 3.11**. 

### Installing Whisper

To download and install (or update to) the latest release of Whisper, run the following command:
```bash
pip install -U openai-whisper
```

Alternatively, to install the latest commit from the repository along with its Python dependencies:
```bash
pip install git+https://github.com/openai/whisper.git
```

To update the package to the latest version of this repository, please run:
```bash
pip install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git
```

### Installing FFMPEG
Whisper also requires the FFmpeg command-line tool to be installed on your system, which is available from most package managers:

```bash
# on Ubuntu or Debian
sudo apt update && sudo apt install ffmpeg

# on Arch Linux
sudo pacman -S ffmpeg

# on MacOS using Homebrew (https://brew.sh/)
brew install ffmpeg

# on Windows using Chocolatey (https://chocolatey.org/)
choco install ffmpeg

# on Windows using Scoop (https://scoop.sh/)
scoop install ffmpeg
```
### Installing the jiwer Package
To calculate the Word Error Rate (WER), the project uses the jiwer Python package. Install it using the following command:
```bash
pip install jiwer
```



