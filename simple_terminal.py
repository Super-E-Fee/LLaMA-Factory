import gradio as gr
import subprocess

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout or result.stderr
    except Exception as e:
        return str(e)

iface = gr.Interface(
    fn=run_command,
    inputs="text",
    outputs="text",
    title="Remote Terminal"
)
iface.launch(share=True)