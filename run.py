import os

while True:
    try:
        os.system('python -m vall_e.train yaml=config/ko/ar.yml')
    except RuntimeError:
        continue
    except KeyboardInterrupt:
        break