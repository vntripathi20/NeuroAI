"""Acoustic feature extraction for NeuroAI. Turns a short voice recording into pitch and voice-quality measurements for the Voice Lab page."""


def load_audio(path):
    """Load an audio file from disk and return the waveform samples and sample rate."""
    # TODO: I will implement this
    pass


def extract_pitch(y, sr):
    """Estimate the pitch (fundamental frequency) contour of a waveform."""
    # TODO: I will implement this
    pass


def extract_voice_quality(y, sr):
    """Estimate jitter, shimmer, and harmonics-to-noise ratio (HNR) of a waveform."""
    # TODO: I will implement this
    pass


def extract_features(path):
    """Load an audio file and return its full set of extracted acoustic features."""
    # TODO: I will implement this
    pass
