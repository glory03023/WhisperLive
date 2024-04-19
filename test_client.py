import argparse
from whisper_live.client import TranscriptionClient

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('--host', '-o',
                      type=str,
                      default="127.0.0.1",
                      help="Websocket host to request.")
  parser.add_argument('--port', '-p',
                      type=int,
                      default=9090,
                      help="Websocket port to request.")
  parser.add_argument('--language', '-l',
                      type=str,
                      default="en",
                      help="language to transcribe audio.")
  parser.add_argument('--model', '-m',
                      type=str,
                      default="small.en",
                      help="model to transcribe audio.")
  parser.add_argument('--vad', '-v',
                      action="store_false",
                      help="Boolean for vad. True if use vad.")
  parser.add_argument('--audio', '-a',
                      type=str,
                      default="assets/jfk.flac",
                      help="audio path to submit for transcribe.")

  args = parser.parse_args()

  client = TranscriptionClient(
    args.host,
    args.port,
    lang=args.language,
    translate=False,
    model=args.model,
    use_vad=args.vad,
  )

  client(args.audio)