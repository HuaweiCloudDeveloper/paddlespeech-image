import gradio as gr
import paddle
from paddlespeech.cli.asr.infer import ASRExecutor
from paddlespeech.cli.text.infer import TextExecutor
 
print(f"Current device: {paddle.device.get_device()}")
 
# 初始化 ASR 和 TextExecutor
text_punc = TextExecutor()
asr = ASRExecutor()
 
def process_audio(audio_file):
    # 进行语音识别
    asr_result = asr(audio_file=audio_file)
    print(f"ASR Result: {asr_result}")
    
    # 进行文本加标点符号处理
    result = text_punc(text=asr_result)
    print(f"Punctuation Result: {result}")
    
    return asr_result, result
 
# 创建 Gradio 接口
demo = gr.Interface(
    fn=process_audio,
    inputs=gr.Audio(type="filepath"),  # 输入类型为音频文件路径
    outputs=[
        gr.Textbox(label="ASR Result"),  # 输出 ASR 结果
        gr.Textbox(label="Punctuation Result")  # 输出加标点符号的结果
    ],
    title="语音识别与文本加标点符号",
    description="上传音频文件，进行语音识别并添加标点符号。"
)
 
# 启动 Gradio 应用
if __name__ == "__main__":
demo.launch(server_name="0.0.0.0", server_port=7863)
