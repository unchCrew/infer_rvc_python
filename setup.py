from setuptools import find_packages, setup

setup(
    name="infer_rvc_python",
    version="1.1.0",
    description="Python wrapper for fast inference with rvc",
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    python_requires=">=3.10",
    author="R3gm",
    url="https://github.com/R3gm/infer_rvc_python",
    license="MIT",
    packages=find_packages(),
    package_data={'': ['*.txt', '*.rep', '*.pickle']},
    include_package_data=True,
    install_requires=[
        "torch",
        "torchaudio",
        "gradio",
        "praat-parselmouth>=0.4.3",
        "pyworld==0.3.2",
        "faiss-cpu==1.7.3",
        "torchcrepe==0.0.20",
        "ffmpeg-python>=0.2.0",
        "fairseq @ git+https://github.com/One-sixth/fairseq.git",
        "typeguard==4.2.0",
        "soundfile",
        "librosa",
        "numpy",
    ],
    extras_require={
        "all": [
            "scipy",
            "numba==0.56.4",
            "edge-tts"
        ]
    },
)
