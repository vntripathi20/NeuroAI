"""NeuroAI Streamlit app. Outline only — no implementation yet; see AI_USAGE_LOG.md for AI-use disclosure."""


import features  # my own module for feature extraction
import streamlit as st
import numpy as np
import pandas as pd
import librosa.display
import parselmouth
import matplotlib.pyplot as plt
import soundfile as sf
import tempfile

# --- MatPlotLib configuration ---
plt.rcParams.update({
    "figure.facecolor": "#1a1a19",
    "axes.facecolor": "#1a1a19",
    "axes.edgecolor": "#383835",
    "axes.labelcolor": "#c3c2b7",
    "xtick.color": "#c3c2b7",
    "ytick.color": "#c3c2b7",
    "text.color": "#ffffff",
    "grid.color": "#2c2c2a",
})

# --- Streamlit app layout ---
st.set_page_config(page_title="NeuroAI", 
                   layout="wide",
                   page_icon="🧠")

tab1, tab2, tab3 = st.tabs(["🎙️ Voice Lab", "🔬 Research", "ℹ️ About & Limitations"])

# --- Tab 1: Voice Lab ---
with tab1:
    st.title("🧠 NeuroAI Voice Lab")
    st.caption("Explore your voice and see how acoustic features like pitch, jitter, shimmer, and HNR are measured.")
    st.divider()

    # - Audio input: let the user record or upload a short voice clip.
    uploaded = st.file_uploader("Upload a short clip", type=["wav", "mp3"])
    st.caption("Recommend a 5-10 second clip of sustained sound sound (something like 'ahhh') or a short sentence.")
    recorded = st.audio_input("...or record one")  # built into Streamlit, uses the mic

    audio_source = recorded or uploaded

    if audio_source is not None:
        with st.spinner("Analyzing your voice..."):
            with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_file:
                temp_file.write(audio_source.read())
                temp_file_path = temp_file.name
            y, sr = features.load_audio(temp_file_path)

            # - Plots: waveform, pitch contour, spectrogram.
            fig, ax = plt.subplots()
            t = np.linspace(0, len(y) / sr, num=len(y))
            ax.plot(t, y)
            ax.set_xlabel("Time (s)")
            ax.set_ylabel("Amplitude")
            st.pyplot(fig)

            # Pitch contour plot
            pitch_times, pitch_values = features.extract_pitch(y, sr)
            fig, ax = plt.subplots()
            ax.plot(pitch_times, pitch_values)
            ax.set_xlabel("Time (s)")
            ax.set_ylabel("Pitch (Hz)")
            st.pyplot(fig)

            # Spectrogram plot
            fig, ax = plt.subplots()
            D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
            img = librosa.display.specshow(D, sr=sr, x_axis="time", y_axis="log", ax=ax)
            fig.colorbar(img, ax=ax, format="%+2.0f dB")
            st.pyplot(fig)

            # - Metric cards: jitter, shimmer, HNR, and other summary numbers at a glance.
            jitter, shimmer, hnr = features.extract_voice_quality(y, sr)

            with st.container(border=True):
                col1, col2, col3 = st.columns(3)
                col1.metric("Jitter", f"{jitter:.4f}")
                col2.metric("Shimmer", f"{shimmer:.4f}")
                col3.metric("HNR", f"{hnr:.2f} dB")

            # - Explanations: plain-English description of what each metric means.
            with st.expander("What do these metrics mean?"):
                st.write(
                    """
                    - **Jitter**: Variation in pitch period; higher values indicate more irregularity.
                    - **Shimmer**: Variation in amplitude; higher values indicate more irregularity.
                    - **HNR (Harmonics-to-Noise Ratio)**: Ratio of harmonic sound to noise; higher values indicate a clearer voice.
                    """
                )
    else:
        st.info("Please upload or record a short voice clip to see the analysis.")

# -- Tab 3: About & Limitations ---
with tab3:
    st.header("About NeuroAI")
    st.write(
        """
        NeuroAI is a student led and educational tool developed to analyze voice recordings and exploring whether acoustic features of
        speech (pitch, jitter, shimmer, HNR) show measurable patterns, built
        for the Congressional App Challenge.

        By Ved Tripathi, 2026
        """
    )
    st.warning(
        "NeuroAI is a research and education project only. "
        "It is NOT a medical diagnostic tool and shouldn't be used to "
        "diagnose or assess any health condition."
    )

    with open("AI_USAGE_LOG.md") as f:
        ai_usage_log = f.read()

    with st.expander("AI use disclosure"):
        st.markdown(ai_usage_log)



# --- Tab 2: Research ---
# - Leakage comparison: side-by-side results from model.participant_level_split()
#   vs. model.recording_level_split(), to show why the split method matters.
# - Saved results: display previously saved metrics/plots from results/ instead
#   of recomputing every time.


