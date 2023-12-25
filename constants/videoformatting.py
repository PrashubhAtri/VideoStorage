# FrameSize to Resolution mapping
_FrameSizes = {
    "1080": (1920, 1080),
    "720": (1280, 720),
    "test": (30, 30)
}
_FrameRates = {
    "30": 30,
    "24": 24,
    "test": 1
}

# User Specific Resolution and framerate
_outputDefaultResolution = "720"
_outputDeafultFrameRate = "24"

# Frame size exposed
FrameSize = _FrameSizes[_outputDefaultResolution]
FrameRate = _FrameRates[_outputDeafultFrameRate]

"""
Input Signature => (ENV, Quality, Frames, Colour)
Output signature => (FrameSize, FrameRate, No. of Channels)
"""

def variables(ENV, quality=None, frames=None, colour=False):
    if ENV == "prod":
        FS = FrameSize if quality == None else _FrameSizes[quality]
        FR = FrameRate if frames == None else _FrameRates[frames]
        C = 3 if colour else 1
    elif ENV == "test":
        FS = _FrameSizes["test"]
        FR = _FrameRates["test"]
        C = 3 if colour else 1
    else:
        return -1
    return (FS, FR, C)
