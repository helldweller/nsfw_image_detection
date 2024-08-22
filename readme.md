# NSFW Image detection playground

<https://huggingface.co/Falconsai/nsfw_image_detection>

Устанавливаем на Windows:

- git
- `git lfs install`
- cuda <https://developer.nvidia.com/cuda-downloads?target_os=Windows&target_arch=x86_64&target_version=11&target_type=exe_local>
- python
- pip
- `pip install virtualenv`
- `git clone https://github.com/helldweller/nsfw_image_detection.git`
- `python -m venv .venv`
- `.venv\Scripts\activate`
- `pip install -r requirements.txt --require-virtualenv`

Репозиторий с файлами модели добавлен через сабмодули <https://huggingface.co/Falconsai/nsfw_image_detection>

`git submodule update --init --remote`

Убираем warnings

```powershell
$Env:TF_ENABLE_ONEDNN_OPTS = "0"
$Env:HF_HUB_DISABLE_SYMLINKS_WARNING = "1"
Get-ChildItem env:
```

Запуск

```powershell
python.exe .\main.py
```
