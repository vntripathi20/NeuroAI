"""Acoustic feature extraction for NeuroAI. Turns a short voice recording into pitch and voice-quality measurements for the Voice Lab page."""
import librosa
import parselmouth

def load_audio(path):
    """Load an audio file from disk and return the waveform samples and sample rate."""
    y, sr = librosa.load(path, sr=None)  # Load at native sample rate
    return y, sr


def extract_pitch(y, sr):
    """Estimate the pitch (fundamental frequency) contour of a waveform."""
    f0, voiced_flag, voiced_probs = librosa.pyin(
        y,
        fmin=librosa.note_to_hz('C2'),
        fmax=librosa.note_to_hz('C7'),
        sr=sr
    )
    times = librosa.times_like(f0, sr=sr)
    return times, f0


def extract_voice_quality(y, sr):
    """Estimate jitter, shimmer, and harmonics-to-noise ratio (HNR) of a waveform."""
    sound = parselmouth.Sound(y, sr)

    point_process = parselmouth.praat.call(
        sound, "To PointProcess (periodic, cc)", 75, 500
    )

    jitter = parselmouth.praat.call(
        point_process, "Get jitter (local)", 0, 0, 0.0001, 0.02, 1.3
    )
    shimmer = parselmouth.praat.call(
        [sound, point_process], "Get shimmer (local)", 0, 0, 0.0001, 0.02, 1.3, 1.6
    )
    harmonicity = parselmouth.praat.call(
        sound, "To Harmonicity (cc)", 0.01, 75, 0.1, 1.0
    )
    hnr = parselmouth.praat.call(harmonicity, "Get mean", 0, 0)

    return jitter, shimmer, hnr

def extract_features(path):
    """Load an audio file and return its full set of extracted acoustic features."""
    # TODO: I will implement this
    pass
