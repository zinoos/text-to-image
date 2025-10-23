from flask import Flask, render_template, request, send_from_directory
from diffusers import AutoPipelineForText2Image
import torch, time
from pathlib import Path

app = Flask(__name__, template_folder="templates")
IMG_DIR = Path(__file__).parent / "img"
IMG_DIR.mkdir(exist_ok=True)

pipe = AutoPipelineForText2Image.from_pretrained(
    "stabilityai/sdxl-turbo",
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
).to("cuda" if torch.cuda.is_available() else "cpu")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    prompt = request.form.get("prompt", "").strip()
    if not prompt:
        return render_template("index.html", error="Enter a prompt")

    image = pipe(prompt, num_inference_steps=1, guidance_scale=0.0).images[0]
    filename = f"{int(time.time()*1000)}.png"
    image.save(IMG_DIR / filename)
    return render_template("index.html", image_url=f"/img/{filename}")

@app.route("/img/<path:filename>")
def img(filename):
    return send_from_directory(IMG_DIR, filename)

if __name__ == "__main__":
    app.run()
