# Copyright (c) 2024 iiPython

# Modules
import uvicorn

# Launch app
def launch_dev() -> None:
    uvicorn.run("authentication:app", reload = True)

if __name__ == "__main__":
    launch_dev()
