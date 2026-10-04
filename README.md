# DeskFlip World Clock

DeskFlip is a dual-time-zone flip clock built to repurpose an older iPad as a desk clock while also working as a small Streamlit portfolio project.

## What it does

- Shows two time zones side by side in landscape and stacked in portrait.
- Lets you choose the left/first and right/second clocks independently.
- Defaults to Philippines (Asia/Manila) and United Kingdom (Europe/London).
- Includes day/light and night/dark themes.
- Supports 12-hour and 24-hour time.
- Lets you show or hide seconds.
- Saves your clock choices and theme locally on the device.
- Uses lightweight HTML/CSS/ES5-style JavaScript for better compatibility with older Safari.
- Includes a Streamlit wrapper for modern browsers and a standalone GitHub Pages version for the old iPad.

## Project structure

~~~text
deskflip-world-clock/
|-- .streamlit/
|   |-- config.toml
|-- docs/
|   |-- .nojekyll
|   |-- index.html
|-- .gitignore
|-- README.md
|-- requirements.txt
|-- streamlit_app.py
~~~

## Run the Streamlit version locally

~~~bash
python -m venv .venv
~~~

On Windows PowerShell:

~~~powershell
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run streamlit_app.py
~~~

On macOS/Linux:

~~~bash
source .venv/bin/activate
pip install -r requirements.txt
streamlit run streamlit_app.py
~~~

## Test the standalone version locally

From the repository root:

~~~bash
python -m http.server 8000 --directory docs
~~~

Then open http://localhost:8000 in a browser.

## Best version for the old iPad

Use the GitHub Pages version, not the Streamlit URL. Current Streamlit uses a modern browser frontend, while the standalone page avoids that dependency.

To publish it:

1. Open this repository on GitHub.
2. Go to Settings -> Pages.
3. Under Build and deployment, choose Deploy from a branch.
4. Choose branch main and folder /docs.
5. Click Save.
6. After GitHub finishes publishing, open:

~~~text
https://narseva.github.io/deskflip-world-clock/
~~~

## Set it up on the iPad

1. Open the GitHub Pages URL in Safari.
2. Tap Share -> Add to Home Screen.
3. Name it DeskFlip.
4. Launch it from the Home Screen.
5. Tap SET to choose the two clocks independently.
6. Rotate the iPad to switch between portrait and landscape layouts.
7. In iPad settings, set Auto-Lock -> Never while using it as a desk clock.

## Streamlit Community Cloud deployment

1. Sign in to Streamlit Community Cloud using GitHub.
2. Create a new app from NarsEva/deskflip-world-clock.
3. Use branch main.
4. Use streamlit_app.py as the entrypoint.
5. Deploy.

The GitHub Pages URL is the recommended URL for the iPad itself; the Streamlit deployment is mainly useful as a portfolio/demo version.
