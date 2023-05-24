
import gradio as gr
import time
from autogpt.trans_utils.trans_util import translate_chinese_to_english

NOTE_TXT = "【您可以这么提问】：\n" \
           "＊怎么提高我的店铺质量分数？\n"
MAX_BOXES = 20

def run(user_task: str =None):
    from autogpt.main import run_auto_gpt
    for value in run_auto_gpt(
        continuous=True,
        continuous_limit=None,
        ai_settings=None,
        skip_reprompt=False,
        speak=False,
        debug=False,
        gpt3only=False,
        gpt4only=False,
        memory_type=None,
        browser_name=None,
        allow_downloads=False,
        skip_news=False,
        workspace_directory=None,
        install_plugin_deps=False,
        user_task=user_task
    ):
        yield value

def stream_chat(question, history=None, box_size=20):



    question = translate_chinese_to_english(question)

    if history is None:
        history = []

    content = ""
    for value in run(question):
        time.sleep(1)
        if len(content) > 0 and len(history) > 0:
            # history中去掉最后一个元素
            history.pop()

        updates = []
        delta_content = value.__str__()
        delta_content = " " if delta_content is None else delta_content
        content = content + delta_content

        history.append((question, content))
        for question1, content1 in history:
            updates.append(gr.update(visible=True, value="用户：" + question1))
            updates.append(gr.update(visible=True, value="智能助手：" + content1))
        if len(updates) < box_size:
            updates = updates + [gr.Textbox.update(visible=False)] * (box_size - len(updates))
        updates.append(gr.Textbox.update(value=""))
        yield [history] + updates


def stream_chat1(question, history=None, box_size=20):
    for value in stream_chat(question, history):
        yield value

def start():
    with gr.Blocks() as demo:
        state = gr.State([])
        text_boxes = []

        note = gr.Textbox(show_label=False,
                          placeholder=NOTE_TXT,
                          value=NOTE_TXT,
                          lines=5,
                          interactive=False).style(container=False)

        for i in range(MAX_BOXES):
            if i % 2 == 0:
                text_boxes.append(gr.Markdown(visible=False, label="Ask a Question："))
            else:
                text_boxes.append(gr.Markdown(visible=False, label="Reply："))

        with gr.Row():
            with gr.Column(scale=4):
                txt = gr.Textbox(show_label=False, placeholder="Enter text and press enter", lines=3).style(
                    container=False)
            with gr.Column(scale=1):
                button = gr.Button("Generate")
        button.click(stream_chat1, [txt, state], [state] + text_boxes + [txt])
    demo.queue().launch(share=True, inbrowser=True)
