from whisper_live.client import TranscriptionClient

client = TranscriptionClient(
  "127.0.0.1",
  9090,
  lang="en",
  translate=False,
  model="small.en",
  use_vad=False,
)

client("D:\\Work\\ASR\\WhisperLive\\assets\\jfk.flac")