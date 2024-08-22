# NSFW Image detection playground

<https://huggingface.co/Falconsai/nsfw_image_detection>
<https://pytorch.org/get-started/locally/>
<https://developer.nvidia.com/cuda-toolkit-archive>

Устанавливаем на Windows:

- git
- `git lfs install`
- cuda 12.1 (похоже идет в комплекте с torch)
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

В планах:

- ~~починить работу на GPU~~
- Упаковать в контейнер (кубер) c поддержкой GPU
- Снять бенчмарки с GPU и с CPU
- Написать основную логику: обработка очередей, обработка картинок по url, многопоточность, метрики
