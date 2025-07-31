import paddle
from paddlespeech.cli.asr.infer import ASRExecutor
from paddlespeech.cli.text.infer import TextExecutor
 
print(f"Current device: {paddle.device.get_device()}")
 
# 语音识别
asr = ASRExecutor()
asr_result = asr(audio_file="zh.wav")
print(asr_result)
 
# 标点恢复
text_punc = TextExecutor() 
result = text_punc(text=asr_result)
print(result)
