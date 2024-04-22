from pydub import AudioSegment
from pydub.silence import split_on_silence
import speech_recognition as sr


def split_audio_into_sentences(audio_file, output_path, min_silence_len=500, silence_thresh=-40):
    # Load audio file
    audio = AudioSegment.from_mp3(audio_file)

    # Split audio on silence
    segments = split_on_silence(audio, min_silence_len=min_silence_len, silence_thresh=silence_thresh)

    r = sr.Recognizer()
    output_files = []

    for i, segment in enumerate(segments):
        # Export segment to a temporary file
        segment_filename = f"{output_path}/temp_segment_{i}.wav"
        segment.export(segment_filename, format="wav")

    return output_files


if __name__ == "__main__":
    input_audio_file = ""
    output_path = ""
    output_segments = split_audio_into_sentences(input_audio_file, output_path=output_path)
    print(f"Saved segments: {output_segments}")
